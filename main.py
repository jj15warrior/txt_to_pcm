import os
import math
from scipy.io.wavfile import write
import numpy as np
from pydub import AudioSegment

samplerate = 44100
t = np.linspace(0., 1., samplerate)
oneletter_per_sample = 0.000226757

open("output.pcm", "w").close()

inp_txt = "qwerty TEST 123 ! [](){}\\|//?.,"



def gen_sinusoidal_data(frequency, amplitude, duration):
    return np.sin(2 * np.pi * np.arange(samplerate * duration) * frequency / samplerate) * amplitude


data = []

# stupid mode:

"""
for ch in inp_txt:
    for bit in str(bin(ord(ch))):
        if bit == "1":
            for elem in gen_sinusoidal_data(1500, 1, 0.02):
                data.append(elem)
        else:
            for elem in gen_sinusoidal_data(1000, 1, 0.02):
                data.append(elem)
"""

for ch in inp_txt:
    for elem in gen_sinusoidal_data(8 * ord(ch) + 500, 1, 0.02):
        data.append(math.floor(elem * 5000))

data = np.array(data)

write("output.pcm", samplerate, data.astype(np.int16))