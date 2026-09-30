# EEG Signal Processing & Analysis Pipeline

An ongoing project focused on processing, analyzing, and eventually classifying EEG (electroencephalography) signals for applications in brain-computer interfaces (BCIs).

## Project Status

**In Progress — Early Development**

The project was originally started around **January 2026** and has not received regular development updates since the initial work. Development is expected to resume as part of continued exploration into EEG signal processing and BCI technologies.

### Current Progress

* Loaded and inspected EEG recordings using Python and MNE
* Working with the **CHB-MIT Scalp EEG Database**
* Implemented initial EEG signal visualization
* Generated raw EEG signal plots
* Generated frequency-domain analysis using PSD
* Began exploring EEG preprocessing and noise reduction
* Initial project structure established in Python

## Technologies

* **Python**
* **MNE-Python**
* **NumPy**
* **Matplotlib**
* **SciPy**
* **TBD:** Additional machine learning and signal-processing libraries as development continues

## Dataset

This project uses EEG recordings from the **CHB-MIT Scalp EEG Database**, provided through PhysioNet.

The raw `.edf` EEG recordings are not included in this repository due to file size. The dataset can be accessed through the official PhysioNet database:

**Dataset:** https://physionet.org/content/chbmit/1.0.0/

The specific recording currently used during development is:

`chb01_01.edf`

The dataset is used for educational and research purposes as the project develops.

## Long-Term Goal

The long-term goal is to develop an **end-to-end EEG processing and analysis pipeline** capable of:

1. Loading and preprocessing raw EEG recordings
2. Filtering and removing common sources of noise and artifacts
3. Performing time-domain and frequency-domain analysis
4. Extracting meaningful features from neural signals
5. Applying machine learning techniques for signal classification
6. Evaluating model performance on EEG data
7. Exploring potential applications of the pipeline in **brain-computer interface (BCI)** systems

The final scope and technologies used may change as the project develops.

## Future Development

Planned areas of development include:

* [ ] Improve EEG preprocessing pipeline
* [ ] Implement band-pass and notch filtering
* [ ] Explore artifact removal techniques
* [ ] Perform additional frequency-domain analysis
* [ ] Implement feature extraction
* [ ] Experiment with machine learning classification
* [ ] Evaluate classification performance
* [ ] Investigate potential BCI applications

---
**Created:** January 2026
**Status:** In Progress
