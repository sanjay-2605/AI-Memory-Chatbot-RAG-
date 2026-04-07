from utils.speech_to_text import transcribe_audio
from utils.text_to_speech import speak
from utils.llm import generate_response

def run_voice_assistant():
    print("Speak something... (audio.wav)")
    
    text = transcribe_audio("audio.wav")
    print("You said:", text)

    response = generate_response(text)
    print("AI:", response)

    speak(response)

if __name__ == "__main__":
    run_voice_assistant()
