
import numpy as np


def calculate_snr_db(
    reference: np.ndarray,
    measured: np.ndarray,
) -> float:
    """Calculate SNR in dB using a clean reference and its measured version."""
    reference = np.asarray(reference, dtype=float)
    measured = np.asarray(measured, dtype=float)

    if reference.shape != measured.shape:
        raise ValueError("Reference and measured signals must have the same shape.")

    if reference.size == 0:
        raise ValueError("Signals must not be empty.")

    noise = measured - reference
    noise_power = np.mean(noise**2)
    signal_power = np.mean(reference**2)

    if signal_power == 0:
        raise ValueError("Reference signal must have non-zero power.")

    if noise_power == 0:
        return float("inf")

    return float(10 * np.log10(signal_power / noise_power))

def calculate_tone_amplitude(
    signal: np.ndarray,
    fs: float,
    frequency: float,
    skip_samples: int = 0,
) -> float:
    """Estimate tone amplitude after optionally skipping startup samples."""
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1 or signal.size == 0:
        raise ValueError("Signal must be a non-empty one-dimensional array.")

    if fs <= 0:
        raise ValueError("Sampling frequency must be positive.")

    if not 0 < frequency < fs / 2:
        raise ValueError("Frequency must be between 0 Hz and the Nyquist frequency.")

    if not isinstance(skip_samples, (int, np.integer)) or skip_samples < 0:
        raise ValueError("skip_samples must be a non-negative integer.")

    if skip_samples >= signal.size:
        raise ValueError("skip_samples must be smaller than the signal length.")

    signal = signal[skip_samples:]
    t = np.arange(skip_samples, skip_samples + signal.size) / fs

    sine_basis = np.sin(2 * np.pi * frequency * t)
    cosine_basis = np.cos(2 * np.pi * frequency * t)

    sine_component = 2 * np.mean(signal * sine_basis)
    cosine_component = 2 * np.mean(signal * cosine_basis)

    return float(np.hypot(sine_component, cosine_component))


def calculate_tone_attenuation_db(
    input_signal: np.ndarray,
    output_signal: np.ndarray,
    fs: float,
    frequency: float,
    skip_samples: int = 0,
) -> float:
    """Measure tone-amplitude reduction after optionally skipping startup samples."""
    if np.asarray(input_signal).shape != np.asarray(output_signal).shape:
        raise ValueError("Input and output signals must have the same shape.")

    input_amplitude = calculate_tone_amplitude(
        input_signal, fs, frequency, skip_samples
    )
    output_amplitude = calculate_tone_amplitude(
        output_signal, fs, frequency, skip_samples
    )

    if input_amplitude == 0:
        raise ValueError("Input tone amplitude must be non-zero.")

    if output_amplitude == 0:
        return float("inf")

    return float(20 * np.log10(input_amplitude / output_amplitude))


def calculate_tone_retention_percent(
    input_signal: np.ndarray,
    output_signal: np.ndarray,
    fs: float,
    frequency: float,
    skip_samples: int = 0,
) -> float:
    """Measure tone-amplitude retention after optionally skipping startup samples."""
    if np.asarray(input_signal).shape != np.asarray(output_signal).shape:
        raise ValueError("Input and output signals must have the same shape.")

    input_amplitude = calculate_tone_amplitude(
        input_signal, fs, frequency, skip_samples
    )
    output_amplitude = calculate_tone_amplitude(
        output_signal, fs, frequency, skip_samples
    )

    if input_amplitude == 0:
        raise ValueError("Input tone amplitude must be non-zero.")

    return float(100 * output_amplitude / input_amplitude)

