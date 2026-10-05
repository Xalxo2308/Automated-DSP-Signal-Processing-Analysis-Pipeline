from scipy.signal import butter, sosfilt
import numpy as np

def design_sos_bandpass(low_cutoff: float, high_cutoff: float, fs: float, order: int = 4):
    """Designs a Butterworth bandpass filter using Second-Order Sections (SOS) for numerical stability."""
    nyquist = 0.5 * fs
    low = low_cutoff / nyquist
    high = high_cutoff / nyquist
    sos = butter(order, [low, high], btype='bandpass', output='sos')
    return sos

def apply_sos_filter(signal: np.ndarray, sos: np.ndarray) -> np.ndarray:
    """Applies Second-Order Section (SOS) digital filtering to time-series signal data."""
    return sosfilt(sos, signal)