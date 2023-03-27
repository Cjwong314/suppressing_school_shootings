import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import wave
import os
import librosa
import numpy as np
import pickle
import matplotlib
import multiprocessing as mp


#audio recording and gunshot detection
def detect():
    #path where you stored trained model
    path="E:\\All Data\\study\\MS\\2\\machine learning\\Project"
    feature_length=880 #feature vector length
    CHUNK = 1024 #size of each data frame in which audio will be recorded
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 #recording channel
    RATE = 22050 #sampling rate
    RECORD_SECONDS =1
    name="save_training_2.pickle"
    load_training = open("E:\\All Data\study\\MS\\2\\machine learning\\Project\\"+name,'rb')
    clf = pickle.load(load_training) # LOAD TRAINED CLASSIFIER
    load_training.close()
    while(True):
        WAVE_OUTPUT_FILENAME = "background"+".wav"
        p = pyaudio.PyAudio()
        #opening stream for recording audio with given parameters
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        frames = []
        #here audio is recorded for time according to given parameters and data is stored in frames
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        stream.stop_stream() #stop the recording data stream
        stream.close() #close the stream
        p.terminate()
        #now open a wave file with a specified name to store the audio
        wf = wave.open(path+"\\"+WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close() #storing of audio is done till here
        
        #load audio using librosa package 
        y, sr = librosa.load(path+"\\"+WAVE_OUTPUT_FILENAME,duration=1)
        # extracting MFCC feature of audio
        S= librosa.feature.mfcc(y=y, sr=sr, hop_length=512, n_mfcc=20)
        S=np.reshape(S,np.product(S.shape))
        #making shape equal to 880 equal to feature vector length
        if S.shape[0]<feature_length:    
            S=np.concatenate((S[0:S.shape[0]],S[S.shape[0]-(feature_length-S.shape[0]):S.shape[0]]))
        else:
            S=S[0:feature_length]
        if clf.predict([S])==1:
            print ("Nogunshot")
        else:
            print ("Gunshot")

if __name__=='__main__':
    detect()