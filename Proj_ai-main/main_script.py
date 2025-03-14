from brainu import Brainu
from tts_module import text_to_speech

def main():
    print("Starting the AI Project...")
    brainu = Brainu()
    brainu.run()
    text_to_speech("The AI system has finished running.")

if __name__ == "__main__":
    main()