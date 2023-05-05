#!/usr/bin/env python
# coding: utf-8

# In[17]:


# load the .wav file contents
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import numpy as np
fs,data = wavfile.read("original.wav") #Reading recorded aodio file
length = len(data)/fs
dataf = np.fft.fft(data[:,0]) #using FFT to convert into frequency domain
fd = abs(dataf) #considering absolute values
x = fd[0:int((len(fd)/2)-1)] #half-samples consideration

# Amplified harmonics
k1 = int(len(dataf)/fs*1000) #index place for 1000Hz
k2 = int(len(dataf)/fs*10000) #index place for 20000Hz
dataf[k1:k2] = dataf[k1:k2]*10 #hamonics amplification
faxis = np.linspace(0, fs/2, len(x)) #frequency axis
plt.plot(faxis,20*np.log10(dataf[0:int(len(dataf)/2)-1]/len(dataf)))
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude in dB")
plt.title("Improved Frequency Domain")
plt.xscale("log")
plt.savefig("Improved Frequency Domain.svg")
plt.show()

enhanced = np.fft.ifft(dataf) #inverse fourier transform to transform to time domain
clr = np.real(enhanced) #real part extraction
audio = clr.astype(np.int16) #convert to 16 bit data
taxis = np.linspace(0, length, len(data)) #from start point(0) to end point(length = len(data)/fs)
plt.plot(taxis,clr) #plotting in time domain
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title(" Improved Time Domain")
plt.savefig("Improved Time Domain.svg")
plt.show()
wavfile.write('improved.wav',fs,audio)#saving enhanced audio file


# In[ ]:




