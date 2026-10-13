# Automated DSP & Signal Processing Analysis Pipeline

A Python-based digital signal processing (DSP) project for signal generation, noise analysis, frequency-domain inspection and digital filtering. The project explores how signal-processing techniques can be combined into a repeatable analysis workflow using NumPy and SciPy.

## Overview

Digital signals can be corrupted by noise and unwanted frequency components, making it difficult to identify the information of interest. This project implements a signal-processing workflow to investigate signal characteristics, introduce controlled noise, analyse frequency content and apply digital filters.

The project focuses on fundamental DSP concepts relevant to telecommunications, electronics and measurement systems.

## Engineering Objectives

- Generate and analyse synthetic test signals.
- Investigate signal behaviour in the time and frequency domains.
- Introduce additive white Gaussian noise (AWGN) under a controlled SNR condition.
- Apply Fast Fourier Transform (FFT) analysis to inspect frequency components.
- Implement Butterworth filtering to isolate desired frequency content.
- Compare signal characteristics before and after filtering.
- Produce plots that support interpretation of the processing results.

## Signal Processing Workflow

```text
Signal Generation
       |
       v
Time-Domain Analysis
       |
       v
AWGN Noise Addition
       |
       v
SNR and Frequency Analysis
       |
       v
FFT-Based Spectral Inspection
       |
       v
Butterworth Digital Filtering
       |
       v
Filtered Signal Analysis
       |
       v
Visualisation and Interpretation
```

## Technical Implementation

### 1. Signal Generation

Synthetic multi-tone signals provide a controlled input for investigating frequency-domain behaviour.

An example test signal discussed in this project combines components at 120 Hz and 450 Hz. Synthetic signals make it possible to examine known frequency components and study the effects of noise and filtering.

### 2. Noise Modelling

Additive white Gaussian noise (AWGN) is used to investigate the effect of noise on signal quality.

A 5 dB SNR condition is an example scenario used in the project's signal-processing workflow. SNR provides a way to describe the relative power of the desired signal and noise.

### 3. Frequency-Domain Analysis

The Fast Fourier Transform (FFT) converts a sampled signal from its time-domain representation into a frequency-domain representation.

This analysis helps identify dominant frequency components and examine how noise and filtering affect the observed spectrum.

### 4. Digital Filtering

Butterworth filters are used to investigate frequency-selective signal processing. SciPy's signal-processing functionality, including second-order-section filtering with `sosfilt`, supports filter implementation.

The filtering stage is intended to retain the frequency content of interest while attenuating unwanted components. Actual attenuation depends on the filter design, cutoff frequencies, order and input signal.

### 5. Visualisation

Plots are used to inspect signal behaviour at different stages of the pipeline, including the time-domain waveform and frequency spectrum.

Visual comparisons help connect the mathematical principles of DSP with the observed signal behaviour.

## Technology Stack

| Technology | Application |
|---|---|
| Python | Implementation and workflow automation |
| NumPy | Numerical computation and array operations |
| SciPy | Digital filter design and signal processing |
| FFT | Frequency-domain analysis |
| Matplotlib, if used in the implementation | Signal and spectrum visualisation |

## Example Analysis Scenario

The project explores a multi-tone signal containing 120 Hz and 450 Hz components, with an example AWGN condition of 5 dB SNR.

The workflow examines the signal spectrum and applies frequency-selective filtering to investigate the retention of a target component.

The purpose of this scenario is to demonstrate DSP methodology. Quantitative performance claims should be based on measured results from the actual implementation.

## Relevance to Engineering

The methods demonstrated in this project are relevant to:

- Telecommunications signal analysis
- Electronic measurement and instrumentation
- Noise and interference analysis
- Digital filter design
- Frequency-domain inspection
- Automated engineering analysis workflows

The concepts also provide a foundation for more advanced signal-acquisition systems in which analogue conditioning and ADC sampling feed digital processing software.

## Skills Demonstrated

- Python-based numerical computing
- Fundamental digital signal processing
- FFT and spectral analysis
- AWGN noise modelling
- Signal-to-noise ratio analysis
- Butterworth filter implementation
- Technical plotting and interpretation
- Structured signal-processing workflows

## Repository Contents

The repository contains the implementation files for the DSP analysis pipeline. Refer to the source files and any included dependency or configuration files for the exact implementation details.

## Getting Started

Python and the required scientific-computing libraries are needed to run the project.

1. Clone the repository:

   ```bash
   git clone https://github.com/Xalxo2308/Automated-DSP-Signal-Processing-Analysis-Pipeline.git
   ```

2. Enter the project directory:

   ```bash
   cd Automated-DSP-Signal-Processing-Analysis-Pipeline
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependencies used by the implementation:

   ```bash
   python3 -m pip install numpy scipy matplotlib
   ```

   Matplotlib is needed only if the project uses it for plotting. Install any additional dependencies specified by the repository.

5. Run the project's Python entry-point script or notebook. Check the repository files to identify the correct filename and execution command.

## Future Improvements

Potential extensions include:

- Automated comparison of noisy and filtered signal spectra.
- Quantitative measurements of SNR before and after filtering.
- Filter-response and frequency-response plots.
- Parameterised experiments across multiple noise levels.
- Automated report generation for repeatable DSP experiments.
- Integration with sampled data from an external data-acquisition system.

## Author

**Swati Clarice Xalxo**

Electronics, Telecommunications and Systems Engineering

GitHub: [@Xalxo2308](https://github.com/Xalxo2308)

---

*This project is intended for engineering learning, experimentation and demonstration of digital signal processing principles.*
