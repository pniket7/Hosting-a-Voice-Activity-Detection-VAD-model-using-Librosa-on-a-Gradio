#!/usr/bin/env python
# coding: utf-8

# In[1]:


import librosa
import numpy as np
import soundfile as sf
import gradio as gr


# In[2]:


def apply_vad(audio_file):
    y, sr = librosa.load(audio_file.name, sr=16000) 
    silence_duration = 0.5  # in seconds
    silence_length = int(silence_duration * sr)
    energy_threshold = 0.4
    frame_length = int(0.02 * sr)  # 20ms
    energy = np.array([sum(abs(y[i:i+frame_length]**2)) for i in range(0, len(y)-frame_length, frame_length)])
    speech_segments = np.where(energy > energy_threshold)[0]
    silence_start = int(0.8 * sr)
    silence_end = int(0.96 * sr)
    speech_segments = np.insert(speech_segments, 1, silence_start)
    speech_segments = np.insert(speech_segments, 3, silence_end + silence_length)
    new_y = np.zeros_like(y)
    for i in range(len(speech_segments)):
        start = speech_segments[i] * frame_length
        end = (speech_segments[i] + 1) * frame_length
        new_y[start:end] = y[start:end]
    y_trimmed, _ = librosa.effects.trim(new_y)
    y_preemphasized = librosa.effects.preemphasis(y_trimmed)
    y_normalized = librosa.util.normalize(y_preemphasized)
    sr_new = 8000
    y_resampled = librosa.resample(y_normalized, orig_sr=sr, target_sr=sr_new)
    # pad audio to make it 1 second long
    duration = y_resampled.shape[0] / sr_new
    if duration != 1:
        if duration < 1:
            num_samples_to_pad = int((1 - duration) * sr_new)
            y_resampled = np.pad(y_resampled, (0, num_samples_to_pad), 'constant')
        else:
            y_resampled = librosa.util.fix_length(y_resampled, sr_new, mode='constant')
    new_audio_file_path = "/home/niket/Music/VAD Output/" + audio_file.name.split("/")[-1] + "_VAD.wav"
    sf.write(new_audio_file_path, y_resampled, sr_new)
    return new_audio_file_path, 1.0

def get_duration(audio_file):
    return 1.0


# In[3]:


iface = gr.Interface(
    apply_vad, 
    inputs=gr.inputs.File(label="Upload Audio File"),
    outputs=[
        gr.outputs.File(label="Download VAD Applied Audio File"),
        gr.outputs.Textbox(label="Duration of Output Audio (seconds)")],
    capture_session=True,
    title="Voice Activity Detection (VAD) using librosa"
)


# In[4]:


if __name__ == "__main__":
    iface.launch()


# In[ ]:




