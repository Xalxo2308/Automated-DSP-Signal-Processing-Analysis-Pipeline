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


from src.performance_metrics import (
    calculate_snr_db,
    calculate_tone_amplitude,
    calculate_tone_attenuation_db,
    calculate_tone_retention_percent,
)


def test_calculate_snr_db():
    reference = np.ones(1000)
    measured = reference + np.full(1000, 0.1)

    snr = calculate_snr_db(reference, measured)

    assert np.isclose(snr, 20.0)


def test_calculate_tone_amplitude():
    fs = 5000
    t = np.arange(fs) / fs
    signal = 1.5 * np.sin(2 * np.pi * 120 * t)

    amplitude = calculate_tone_amplitude(signal, fs, 120)

    assert np.isclose(amplitude, 1.5, atol=1e-10)


def test_calculate_tone_attenuation_db():
    fs = 5000
    t = np.arange(fs) / fs
    input_signal = np.sin(2 * np.pi * 450 * t)
    output_signal = 0.1 * input_signal

    attenuation = calculate_tone_attenuation_db(
        input_signal, output_signal, fs, 450
    )

    assert np.isclose(attenuation, 20.0, atol=1e-10)


def test_calculate_tone_retention_percent():
    fs = 5000
    t = np.arange(fs) / fs
    input_signal = np.sin(2 * np.pi * 120 * t)
    output_signal = 0.8 * input_signal

    retention = calculate_tone_retention_percent(
        input_signal, output_signal, fs, 120
    )

    assert np.isclose(retention, 80.0, atol=1e-10)
