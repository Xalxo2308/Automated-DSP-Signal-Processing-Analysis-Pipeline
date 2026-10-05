import pytest
import numpy as np
from src.signal_generator import generate_multitone_signal, add_awgn
from src.filter_engine import design_sos_bandpass, apply_sos_filter

def test_signal_generation_length():
    fs, duration = 5000, 1.0
    t, sig = generate_multitone_signal(fs, duration, [120, 450], [1.0, 0.8])
    assert len(sig) == 5000

def test_awgn_power_addition():
    np.random.seed(42)
    _, sig = generate_multitone_signal(5000, 1.0, [120], [1.0])
    noisy_sig = add_awgn(sig, target_snr_db=10)
    assert np.var(noisy_sig) > np.var(sig)

def test_sos_filter_attenuation():
    fs = 5000
    t = np.linspace(0, 1.0, fs, endpoint=False)
    high_freq_noise = np.sin(2 * np.pi * 1000 * t)  # Out of passband tone
    sos = design_sos_bandpass(100, 140, fs, order=4)
    filtered = apply_sos_filter(high_freq_noise, sos)
    assert np.std(filtered) < 0.1 * np.std(high_freq_noise)