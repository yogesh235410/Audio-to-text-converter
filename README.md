Audio to Text Converter
Overview
The Audio to Text Converter is a Python application that allows users to convert spoken audio into written text. It uses the SpeechRecognition library to capture audio from the microphone or upload audio files, and then uses the Google Web Speech API to transcribe the audio into text.

Features
Record audio from the microphone and convert it to text.
Upload audio files (supported formats: WAV and MP3) and convert them to text.
Display the transcribed text in a text box.
Provide status updates (e.g., "Listening...", "Converting...", "Done", "Error: Could not understand audio", etc.) based on the conversion process.

Installation
Clone this repository to your local machine.
Install the required Python packages by running pip install -r requirements.txt.
Run the application by executing python main.py.

Usage
Recording Audio: Click the "Record" button to start recording audio from the microphone. Speak clearly and audibly into the microphone. Click the "Record" button again to stop recording.

Uploading Audio: Click the "Upload" button to open a file dialog. Select an audio file (WAV or MP3 format) from your local machine and click "Open". The application will convert the uploaded audio file to text.

Viewing Transcribed Text: The transcribed text will be displayed in the text box below the buttons. You can copy the text or save it as needed.

Contributing
If you'd like to contribute to this project, please follow these guidelines:

Fork this repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request to the main repository.
