import math

import numpy as np
import pydub
import scipy.io.wavfile

samplerate = 44100


def read(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2 ** 15
    else:
        return a.frame_rate, y


# 882 = full wave
saved = 0
# data = read("output.mp3")
data = scipy.io.wavfile.read("output.pcm")
data = data[1]


def decodetable():
    pass


def generate_preindexed_sine_patterns(one_bit_length, frequency, amplitude=1):
    one_bit_length *= samplerate
    return np.sin(
        2 * np.pi * np.arange(one_bit_length) * frequency / samplerate) * amplitude


pre_calculated_sines = []
for i in range(255):
    tmparray = []
    for sinelement in generate_preindexed_sine_patterns(0.02, 8 * i + 500):
        tmparray.append(math.floor(sinelement * 5000))
    pre_calculated_sines.append(tmparray)

ret_string = ""
for i in range(len(data)):

    if i + 4 <= len(data):
        if i % 882 == 0:
            found = 0
            for eq_index in range(255):
                if data[i + 4] == pre_calculated_sines[eq_index][4]:
                    found = eq_index
            if found == 0:
                print("invalid sample error")
            else:
                ret_string += chr(found)
print(ret_string)
