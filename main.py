import sys
import speech_recognition as sr
import pyaudio
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit, QFileDialog

class AudioToText(QWidget):
    def __init__(self):
        super().__init__()

        # initialize the recognizer
        self.recognizer = sr.Recognizer()

        # set up the UI
        self.initUI()

    def initUI(self):
        # set up the UI components
        self.record_button = QPushButton('Record', self)
        self.record_button.move(20, 20)
        self.record_button.clicked.connect(self.record_audio)

        self.upload_button = QPushButton('Upload', self)
        self.upload_button.move(120, 20)
        self.upload_button.clicked.connect(self.upload_audio)

        self.text_box = QTextEdit(self)
        self.text_box.setGeometry(20, 70, 360, 240)

        self.status_label = QLabel(self)
        self.status_label.setGeometry(20, 330, 360, 30)

        # set up the window
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Audio to Text Converter')
        self.show()

    def record_audio(self):
        # set up the audio source
        with sr.Microphone() as source:
            self.status_label.setText('Listening...')
            audio = self.recognizer.listen(source)

        try:
            # convert audio to text
            text = self.recognizer.recognize_google(audio)
            self.text_box.setText(text)
            self.status_label.setText('Done')
        except sr.UnknownValueError:
            self.status_label.setText('Error: Could not understand audio')
        except sr.RequestError as e:
            self.status_label.setText('Error: {0}'.format(e))

    def upload_audio(self):
        # open file dialog to select audio file
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Audio File', '.', 'Audio files (*.wav *.mp3)')

        if file_name:
            # set up the audio source
            with sr.AudioFile(file_name) as source:
                self.status_label.setText('Converting...')
                audio = self.recognizer.record(source)

            try:
                # convert audio to text
                text = self.recognizer.recognize_google(audio)
                self.text_box.setText(text)
                self.status_label.setText('Done')
            except sr.UnknownValueError:
                self.status_label.setText('Error: Could not understand audio')
            except sr.RequestError as e:
                self.status_label.setText('Error: {0}'.format(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AudioToText()
    sys.exit(app.exec())