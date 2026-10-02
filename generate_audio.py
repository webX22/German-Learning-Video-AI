import sys
import soundfile as sf

from qwen_tts import Qwen3TTSModel


MODEL_NAME = "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice"


def generate_voice(text, output_file, speaker):
    print("Loading Qwen TTS...")

    model = Qwen3TTSModel.from_pretrained(
        MODEL_NAME
    )

    print(f"Generating German voice with speaker: {speaker}")

    wavs, sample_rate = model.generate_custom_voice(
        text=text,
        language="German",
        speaker=speaker
    )

    # Qwen returns the generated waveform.
    # Save it ourselves.
    audio = wavs[0]

    sf.write(
        output_file,
        audio,
        sample_rate
    )

    print(f"Audio created: {output_file}")
    print(f"Sample rate: {sample_rate}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage:")
        print('python generate_audio.py "German text" output.wav speaker')
        sys.exit(1)

    text = sys.argv[1]
    output_file = sys.argv[2]
    speaker = sys.argv[3]

    generate_voice(text, output_file, speaker)