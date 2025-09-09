import speech_recognition as sr
#
class Transcriptions:
    @staticmethod
    def voice_to_text(folder_path, file_name):

        file_path=rf"{folder_path}\{file_name}"
        print(file_path)
        r = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            return text
