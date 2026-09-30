"""
This script loads an EEG EDF file, prints basic info, 
and saves plots as PNG files instead of opening GUI windows.
"""

import mne
import matplotlib.pyplot as plt
import os

# ---------------------------
# 1. EDF file path
# ---------------------------
edf_file = "chb01_01.edf"

if not os.path.isfile(edf_file):
    raise FileNotFoundError(f"EDF file not found: {edf_file}")

# ---------------------------
# 2. Load EEG data
# ---------------------------
raw = mne.io.read_raw_edf(edf_file, preload=True)

# ---------------------------
# 3. Print basic info
# ---------------------------
print("EEG file info:")
print(raw.info)
print("Channels:", raw.ch_names)
print(f"Duration (s): {raw.n_times / raw.info['sfreq']:.2f}")

# ---------------------------
# 4. Plot raw EEG signals
# ---------------------------
raw_fig = raw.plot(duration=10, n_channels=10, scalings='auto', show=False)
raw_fig.savefig("raw_eeg_plot.png")  # save as PNG
print("Raw EEG plot saved as raw_eeg_plot.png")

# ---------------------------
# 5. Plot Power Spectral Density (PSD)
# ---------------------------
psd_fig = raw.plot_psd(fmax=70, average=True, show=False)
psd_fig.savefig("eeg_psd_plot.png")
print("PSD plot saved as eeg_psd_plot.png")

# ---------------------------
# 6. Optional: plot a single channel manually
# ---------------------------
data, times = raw[:, :]
plt.figure(figsize=(12, 4))
plt.plot(times, data[0])
plt.title(f"EEG Channel: {raw.ch_names[0]}")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (µV)")
plt.tight_layout()
plt.savefig("single_channel_plot.png")
print("Single channel plot saved as single_channel_plot.png")