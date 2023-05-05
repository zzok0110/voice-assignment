#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import librosa
import matplotlib.pyplot as plt
import scipy
import pylab as plt 
# function to identify vowels
def voweldetector(wavfile): #use the frequency of the first formant to jugde the vowel
    #<code here>
    def get_max_amp_without_numpy(fft):
        max = 0
        for i in range(len(fft)):
            if fft[i] > max:
                max = fft[i]
        return list(fft).index(max)
    a,sr=librosa.load(wavfile)
    fft_a=scipy.fft.fft(a)[0:len(a)//2]
    xf = scipy.fft.fftfreq(len(a), 1 / sr)[0:len(a)//2]
    max_freq=get_max_amp_without_numpy(fft_a)
    max_freq=xf[max_freq]
    print(f"The frequency of this vowel's first formant is {max_freq}")
    if max_freq>750:
        plt.xlim(0,2000)
        plt.xlabel("Frequency(Hz)")
        plt.ylabel("Amplitude")
        plt.title("Spectrum of I")
        plt.plot(xf,fft_a)
        plt.savefig("spectrum of i.svg")
        print("This is the i vowel") 
    else:
        plt.xlim(0,2000)
        plt.xlabel("Frequency(Hz)")
        plt.ylabel("Amplitude")
        plt.title("Spectrum of O")
        plt.plot(xf,fft_a)
        plt.savefig("spectrum of o.svg")
        print("This is the o vowel") 

if __name__ == '__main__':
    path1 = 'o.wav'
    voweldetector(path1)
    path2='i.wav'
    voweldetector(path2)


# In[ ]:




