import numpy as np
import sounddevice as sd
import argparse
import time

# Parameters
num_channels = 8
sample_rate = 16000     # Hz

# Parse arguments
parser = argparse.ArgumentParser(description="Record audio as array")
parser.add_argument('-o', 
                    action='store',
                    default="rec_out.npy",
                    dest='output_file',
                    help="Filename to store array")
parser.add_argument('-t', 
                    action='store',
                    type=float,
                    default=1.0,
                    dest='duration',
                    help="Time (in seconds) to record")
parser.add_argument('-f',
                    action='store',
                    type=int,
                    default=16000,
                    dest='sample_rate',
                    help="Sample rate (Hz)")
args = parser.parse_args()
print("Setting up recording with:")
print(args.sample_rate, "Hz")
print(args.duration, "s")
print(args.output_file)
time.sleep(1.0)

# Do recording
print("Recording...")
rec = sd.rec(int(args.duration * args.sample_rate),
             samplerate=args.sample_rate,
             channels=num_channels)
sd.wait()
print("Done!")

# Save array
print("Saving to", args.output_file)
np.save(args.output_file, rec)