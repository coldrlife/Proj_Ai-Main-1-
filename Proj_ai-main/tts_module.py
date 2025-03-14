from gtts import gTTS
import os

def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Play the audio file

# Example usage
if __name__ == "__main__":
    text_to_speech("Hello, this is a text-to-speech example.")