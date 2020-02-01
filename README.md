# PyRoomAcoustics Matrix Voice Test

A few tests to compare the simulated sound source localization (SSL) in [PyRoomAcoustics](https://github.com/LCAV/pyroomacoustics) vs. actual SSL using the 8-mic array on the [Matrix Voice](https://www.matrix.one/products/voice).

### How to Use
Follow the directions [here](https://www.hackster.io/matrix-labs/direction-of-arrival-for-matrix-voice-creator-using-odas-b7a15b) to install necessary drivers for the Matrix Voice on the Raspberry Pi.

Install sounddevice package on the Pi:

`python3 -m pip install sounddevice`

Copy *rec_test.py* to the Raspberry Pi. Use it with:

`python3 -o <name_of_output_file.npy> -t <seconds of recording> -f <sample rate in Hz>`

Copyt the resulting .npy file to your computer. Open *pyroomacoustics-sim-vs-real.ipynb* in Jupyter Notebook. Change `sound_array_path` to your recorded file. Change `sample_rate` to your sampling frequency. Run it.

Code in this repository is for demonstration purposes only. No warranty given.