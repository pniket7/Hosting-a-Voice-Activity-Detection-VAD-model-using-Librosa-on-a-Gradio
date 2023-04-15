**README**

**1. PROJECT NAME:**

- Voice Activity Detection (VAD) using Librosa library hosted on Gradio Interface.


**2. PROJECT OVERVIEW:**

- This code provides an implementation of Voice Activity Detection (VAD) using the librosa library in Python.
- It takes an audio file as input, applies VAD processing to detect speech segments, and generates an output audio file with only the speech segments retained.
- The output file is padded with zeros or trimmed to 1 second.

**3. DEPENDENCIES:**

The following dependencies need to be installed to run the code:

- librosa
- soundfile
- numpy
- gradio

You can install them using pip or conda package manager.


**4. USAGE:**

- Upload an audio file using the provided Gradio interface.
- The code applies VAD processing on the input audio file to detect speech segments.
- The output audio file with only the speech segments retained is generated.It is then padded with zeros of trimmed to make its duration 1 second before being made available to download.
- The output audio file along with its duration in seconds (1 second) is displayed in the Gradio output interface.


**5. FUNCTIONALITY:**

The code performs the following steps:

- Loads the input audio file using librosa with a sample rate of 16000 Hz.
- Applies VAD processing to detect speech segments based on energy thresholding.
- Trims the speech segments and pre-emphasizes the speech signal.
- Resamples the speech signal to a target sample rate of 8000 Hz.
- Pads or trims the output audio to make it 1 second long, if needed.
- Writes the output audio file to the specified output directory.
- Returns the path of the output audio file and the duration of the output audio in seconds.

**6. INTERFACE:**

The code provides a Gradio interface with the following inputs and outputs:

- Inputs:

File: Upload an audio file.

- Outputs:

File: Download the VAD applied audio file.

Textbox: Duration of the output audio (in seconds).

**7. LICENSE:**

- This project is licensed under the MIT LICENSE.

8\. **CONTACT INFORMATION:**

- For any questions or feedback, please contact:

Name- Niket Virendra Patil

Email- pniket7@gmail.com

