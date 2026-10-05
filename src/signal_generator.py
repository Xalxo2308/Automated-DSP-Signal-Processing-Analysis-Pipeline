import numpy as np

def generate_multitone_signal(fs: int, duration: float, freqs: list, amps: list) -> tuple[np.ndarray, np.ndarray]:
    """Synthesizes a time-domain multitone signal given sampling rate and frequency components."""
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    signal = np.zeros_like(t)
    for freq, amp in zip(freqs, amps):
        signal += amp * np.sin(2 * np.pi * freq * t)
    return t, signal

def add_awgn(signal: np.ndarray, target_snr_db: float) -> np.ndarray:
    """Injects Additive White Gaussian Noise (AWGN) to achieve a specified SNR in dB."""
    sig_power = np.mean(signal ** 2)
    sig_power_db = 10 * np.log10(sig_power)
    noise_power_db = sig_power_db - target_snr_db
    noise_power = 10 ** (noise_power_db / 10)
    noise = np.random.normal(0, np.sqrt(noise_power), signal.shape)
    return signal + noise