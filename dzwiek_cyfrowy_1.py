import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

#zad 1.

fs = 44100
sine_time = 1
frequency = 2

def generate_sine(freq, time, phase = 0):
    return np.array(np.sin(2 * np.pi * freq * np.arange(0,time, 1 / fs) - phase, dtype =np.float32))

#zad 2.
time_vec = np.arange(0, sine_time, 1/fs)

sine = generate_sine(frequency, sine_time)

plt.plot(time_vec, sine)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

#zad 3.

sine_reversed = generate_sine(frequency, sine_time, np.pi)

sine_add = sine + sine_reversed

plt.plot(time_vec, sine_add)

#skalowanie osi:
ax= plt.gca()
ax.set_ylim([-1, 1])


plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

#zad. 4.


#zad. 5.
sine1 = generate_sine(500, 2)
sd.play(sine1, fs)
sd.wait()

#zad. 6.

def normalize_signal(signal):
    min_val = np.min(signal)
    max_val = np.max(signal)
    if max_val == min_val:
        return np.zeros_like(signal)
    normalized_signal = (signal - min_val) / (max_val - min_val)
    normalized_signal *= 2
    normalized_signal -= 1
    return normalized_signal

sine2 = generate_sine(800, 2)
sine_mix = sine1 + sine2
sine_mix = normalize_signal(sine_mix)

sd.play(sine_mix, fs)
sd.wait()