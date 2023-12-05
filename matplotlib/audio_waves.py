import numpy as np
import matplotlib.pyplot as plt


def visualize_audio_waveform(audio_file,rate=None, duration=None, start=None):
    # Load the audio file
    if isinstance(audio_file,str):
        sample_rate, audio_signal = wav.read(audio_file)
    else:
        sample_rate = rate
        audio_signal = audio_file

    if not duration:
        duration = len(audio_signal) / sample_rate
        t = np.linspace(0, duration, len(audio_signal), endpoint=False)
    else:
        signal_length = int(np.floor(duration*sample_rate))
        t = np.linspace(0,int(np.ceil(duration)),signal_length)
        if not start:
            audio_signal = audio_signal[:signal_length]
        else: 
            start_point = int(np.floor(sample_rate*start))
            audio_signal = audio_signal[start_point:start_point+signal_length]

    # Plot the waveform
    plt.figure(figsize=(10, 4))
    plt.plot(t, audio_signal)
    plt.title("Audio Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return audio_signal
