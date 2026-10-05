import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import butter, sosfilt


class SignalProcessor:

    def __init__(self, sampling_rate: int = 5000, duration: float = 1.0):
        self.fs = sampling_rate
        self.t = np.linspace(
            0, duration, int(sampling_rate * duration), endpoint=False
        )
        self.raw_signal = None
        self.noisy_signal = None
        self.filtered_signal = None

    def generate_multitone(
        self, freqs: list[float], amplitudes: list[float]
    ) -> np.ndarray:
        """Synthesize multi-tone carrier signal."""
        signal = np.zeros_like(self.t)
        for f, a in zip(freqs, amplitudes):
            signal += a * np.sin(2 * np.pi * f * self.t)
        self.raw_signal = signal
        return signal

    def add_awgn(self, snr_db: float) -> np.ndarray:
        """Inject Additive White Gaussian Noise based on target SNR."""
        sig_power = np.mean(self.raw_signal**2)
        noise_power = sig_power / (10 ** (snr_db / 10))
        noise = np.random.normal(
            0, np.sqrt(noise_power), size=self.raw_signal.shape
        )
        self.noisy_signal = self.raw_signal + noise
        return self.noisy_signal

    def apply_bandpass(
        self, lowcut: float, highcut: float, order: int = 4
    ) -> np.ndarray:
        """Apply Second-Order Sections (SOS) Butterworth Bandpass Filter."""
        nyq = 0.5 * self.fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], btype="band", output="sos")
        self.filtered_signal = sosfilt(sos, self.noisy_signal)
        return self.filtered_signal

    def compute_fft(self, data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Compute single-sided FFT magnitude spectrum."""
        N = len(data)
        yf = fft(data)
        xf = fftfreq(N, 1 / self.fs)[: N // 2]
        magnitude = (2.0 / N) * np.abs(yf[0 : N // 2])
        return xf, magnitude


def main():
    dsp = SignalProcessor(sampling_rate=5000, duration=1.0)
    dsp.generate_multitone(freqs=[120.0, 450.0], amplitudes=[1.0, 0.7])
    dsp.add_awgn(snr_db=5.0)
    dsp.apply_bandpass(lowcut=80.0, highcut=160.0, order=4)

    freqs, noisy_mag = dsp.compute_fft(dsp.noisy_signal)
    _, filtered_mag = dsp.compute_fft(dsp.filtered_signal)

    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    axes[0].plot(
        freqs, noisy_mag, color="crimson", alpha=0.7, label="Noisy Input"
    )
    axes[0].set_title("Raw Spectrum (Signal + 5dB AWGN)")
    axes[0].set_ylabel("Magnitude")
    axes[0].grid(True, linestyle="--", alpha=0.6)
    axes[0].legend()

    axes[1].plot(
        freqs,
        filtered_mag,
        color="navy",
        label="Filtered Spectrum (120 Hz Isolated)",
    )
    axes[1].set_title("Output Spectrum Post Bandpass Filter")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Magnitude")
    axes[1].grid(True, linestyle="--", alpha=0.6)
    axes[1].legend()

    plt.tight_layout()
    output_path = "dsp_spectrum_analysis.png"
    plt.savefig(output_path, dpi=300)
    print(
        f"\n[SUCCESS] Script executed! Analysis plot saved as '{output_path}'."
    )


if __name__ == "__main__":
    main()