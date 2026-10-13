# Automated DSP & Signal Processing Analysis Pipeline

A modular Python project demonstrating digital signal processing (DSP) through synthetic signal generation, additive white Gaussian noise (AWGN), frequency-domain analysis and Butterworth band-pass filtering.

The project explores how configurable signal-processing stages can be organised into a reproducible workflow, with applications in telecommunications, electronics and measurement systems.

## Project Overview

Digital signals can contain unwanted frequency components and noise that make analysis more difficult. This project uses a synthetic multi-tone signal to investigate signal generation, noise modelling, spectral analysis and frequency-selective filtering.

The implementation combines a configurable processing pipeline with modular source code, automated tests and spectrum visualisation.

## Key Features

- Multi-tone signal generation.
- AWGN noise modelling with a configurable signal-to-noise ratio (SNR).
- FFT-based frequency-domain analysis.
- Butterworth band-pass filter design using SciPy.
- YAML-based configuration.
- Modular Python implementation.
- Automated testing with pytest.
- Spectrum visualisation saved as a PNG image.

## Signal Processing Workflow

```text
Configuration (YAML)
        |
        v
Signal Generation
        |
        v
AWGN Noise Addition
        |
        v
Frequency-Domain Analysis
        |
        v
Butterworth Band-Pass Filtering
        |
        v
Spectrum Visualisation
        |
        v
Automated Testing
```

## Technical Approach

### 1. Signal Generation

Synthetic multi-tone signals provide a controlled environment for investigating frequency components and the effects of noise and filtering.

### 2. Noise Modelling

Additive white Gaussian noise (AWGN) is used to simulate noise affecting a signal. The target SNR is configurable, allowing different noise conditions to be investigated.

### 3. FFT-Based Analysis

The Fast Fourier Transform (FFT) converts a sampled signal into its frequency-domain representation. This makes it possible to inspect prominent frequency components before and after filtering.

### 4. Butterworth Filtering

A Butterworth band-pass filter is used to investigate frequency-selective signal processing. The filter parameters are defined through the project configuration.

The objective is to retain the desired frequency region while attenuating components outside the passband. Actual filter performance should be assessed using the generated spectrum and quantitative measurements.

### 5. Visualisation

The pipeline generates `dsp_spectrum_analysis.png`, providing a visual comparison of the signal's spectral characteristics before and after filtering.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core implementation |
| NumPy | Numerical computation |
| SciPy | Signal processing and filter design |
| Matplotlib | Spectrum visualisation |
| PyYAML | YAML configuration |
| pytest | Automated testing |

The complete dependency list is maintained in `requirements.txt`.

## Repository Structure

```text
Automated-DSP-Signal-Processing-Analysis-Pipeline/
├── src/                       # Modular DSP components
├── tests/                     # Automated tests
├── dsp_pipeline.py            # Pipeline execution script
├── dsp_config.yaml            # Processing configuration
├── dsp_spectrum_analysis.png  # Generated spectrum plot
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # Project documentation
```

## Getting Started

### Prerequisites

- Python 3
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Xalxo2308/Automated-DSP-Signal-Processing-Analysis-Pipeline.git
cd Automated-DSP-Signal-Processing-Analysis-Pipeline
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Run the pipeline

```bash
python3 dsp_pipeline.py
```

The pipeline generates `dsp_spectrum_analysis.png` when execution completes successfully.

### 5. Run the tests

```bash
python3 -m pytest
```

## Verification Results

The following results were observed during local verification on macOS with Apple Silicon and Python 3.13.5:

| Check | Result |
|---|---|
| Dependency installation | Successful |
| Pipeline execution | Successful |
| Spectrum plot generation | Successful |
| Automated tests | 3 passed |
| Test execution time | 0.66 seconds |

These results describe the tested local environment. Results may vary with changes to the source code, configuration, dependencies or execution environment.

## Engineering Applications

The concepts demonstrated in this project are relevant to:

- Telecommunications signal analysis.
- Noise and interference investigation.
- Frequency-domain analysis.
- Digital filter design.
- Electronic measurement systems.
- Reproducible engineering experiments.

## Potential Future Improvements

- Quantitative input/output SNR comparison.
- Measurement of target-tone retention and interference attenuation.
- Filter frequency-response visualisation.
- Experiments across different noise levels.
- Additional tests for edge cases and invalid configurations.
- Automated testing through GitHub Actions.
- Future integration with sampled data from an electronic data-acquisition system.

## Author

**Swati Clarice Xalxo**

Electronics, Telecommunications and Systems Engineering

[GitHub Profile](https://github.com/Xalxo2308)

---

*An engineering project exploring configurable, modular and testable digital signal processing using Python.*
