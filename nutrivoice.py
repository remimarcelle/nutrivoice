import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# George — clear, neutral voice. You can swap this out via the ElevenLabs voice library.
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"


def text_to_audio(text: str, filename: str = "output.mp3") -> str:
    """
    Converts a string of text to speech using the ElevenLabs API
    and saves the result as an MP3 file.

    Args:
        text (str): The content to convert to audio.
        filename (str): The name of the output MP3 file.

    Returns:
        str: The filename of the saved audio.
    """
    print("Converting text to audio...")

    audio = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_multilingual_v2",
    )

    save(audio, filename)
    print(f"Audio saved to: {filename}")
    return filename


def get_multiline_input() -> str:
    """
    Accepts multiline text input from the user.
    Press Enter on an empty line to finish.

    Returns:
        str: The full input as a single string.
    """
    print("Type or paste your content below.")
    print("Press Enter on an empty line when you are done.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    return " ".join(lines)


def main():
    print("=== NutriVoice: Nutrition Content to Audio ===\n")
    print("Use case: paste in a nutrition tip, meal summary, or health content")
    print("and this tool will read it back to you as a clear audio file.\n")

    text = get_multiline_input()

    if not text.strip():
        print("No text entered. Exiting.")
        return

    output_file = "nutrivoice_output.mp3"
    text_to_audio(text, output_file)

    print(f"\nDone. Open {output_file} to listen to your content.")


if __name__ == "__main__":
    main()
