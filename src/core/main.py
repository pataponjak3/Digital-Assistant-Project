from modules.sr.srm import SpeechRecognitionModule
from modules.ss.ssm import SpeechSynthesisModule

def main():
    print("Testing Speech Recognition Module...")
    recognizer = SpeechRecognitionModule()
    synthesizer = SpeechSynthesisModule()

    while True:
        text = recognizer.recognize_speech()
        if text:
            print("You said:", text)
            synthesizer.synthesize_speech(f"You said: {text}")
        
        if text and text.lower() in ["exit", "quit", "stop"]:
            print ("Exiting test")
            synthesizer.synthesize_speech("Exiting test")
            break

    synthesizer.stop()

if __name__ == "__main__": main()