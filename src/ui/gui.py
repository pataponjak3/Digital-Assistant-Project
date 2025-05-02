import tkinter as tk
from tkinter import messagebox
"""from modules.sr.srm import SpeechRecognitionModule
from modules.ss.ssm import SpeechSynthesisModule
from modules.nlp.keyword_intents import KeywordIntentRecognizer"""
from ..core.config import ModuleLoader
import threading

class AssistantGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Assistant")
        self.root.geometry("400x400")

        self.loader = ModuleLoader()
        self.recognizer = self.loader.load_module("sr")
        self.synthesizer = self.loader.load_module("ss")
        self.intent_recognizer = self.loader.load_module("nlp")

        self.label = tk.Label(self.root, text="Press the button and speak", font=("Arial", 12))
        self.label.pack(pady=20)

        self.result_text = tk.Text(self.root, height=5, width=40, font=("Arial", 10))
        self.result_text.pack(pady=10)

        self.intent_label = tk.Label(self.root, text="Intent: None", font=("Arial", 10))
        self.intent_label.pack(pady=10)

        self.listen_button = tk.Button(self.root, text="Start Listening", command=self.listen_and_display, font=("Arial", 12))
        self.listen_button.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def listen_and_display(self):
        def run_logic():
            spoken_text = self.recognizer.recognize_speech()
            if spoken_text:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, spoken_text)
                self.synthesizer.synthesize_speech(f"You said: {spoken_text}")

                intent_data = self.intent_recognizer.recognize_intent(spoken_text)
                if intent_data:
                    intent_str = f"Intent: {intent_data['intent']} | Value: {intent_data['value']}"
                    self.intent_label.config(text=intent_str)
                    self.synthesizer.synthesize_speech(f"This is the intent: {intent_data['intent']} with value: {intent_data['value']}")
                else:
                    self.intent_label.config(text="Intent: Not recognized")
                    self.synthesizer.synthesize_speech("I could not recognize your intent")
            else:
                messagebox.showwarning("Warning", "Could not recognize speech.")
        thread = threading.Thread(target=run_logic)
        thread.start()


    def on_close(self):
        self.synthesizer.stop()
        self.root.destroy()