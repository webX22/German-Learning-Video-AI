from flask import Flask, render_template, request, jsonify
import subprocess
import os
import uuid

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

QWEN_PYTHON = r"C:\AI-Video\.venv\Scripts\python.exe"
QWEN_SCRIPT = os.path.join(BASE_DIR, "generate_audio.py")

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        dialogue = data.get("manualDialogue", "").strip()

        if not dialogue:
            return jsonify({
                "success": False,
                "message": "Please enter a dialogue first."
            }), 400

        voice_a = data.get("voiceA", "serena")
        voice_b = data.get("voiceB", "ryan")

        job_id = str(uuid.uuid4())[:8]

        output_a = os.path.join(
            OUTPUT_DIR,
            f"{job_id}_character_A.wav"
        )

        output_b = os.path.join(
            OUTPUT_DIR,
            f"{job_id}_character_B.wav"
        )

        # Split dialogue into lines.
        lines = [
            line.strip()
            for line in dialogue.splitlines()
            if line.strip()
        ]

        if len(lines) < 2:
            return jsonify({
                "success": False,
                "message": "Please enter at least two dialogue lines."
            }), 400

        # Character A = odd lines
        # Character B = even lines
        text_a = " ".join(lines[0::2])
        text_b = " ".join(lines[1::2])

        print("Generating Character A...")
        subprocess.run(
            [
                QWEN_PYTHON,
                QWEN_SCRIPT,
                text_a,
                output_a,
                voice_a
            ],
            check=True
        )

        print("Generating Character B...")
        subprocess.run(
            [
                QWEN_PYTHON,
                QWEN_SCRIPT,
                text_b,
                output_b,
                voice_b
            ],
            check=True
        )

        return jsonify({
            "success": True,
            "message": "German voices generated successfully!",
            "job_id": job_id,
            "character_a": output_a,
            "character_b": output_b
        })

    except subprocess.CalledProcessError as e:
        print("Qwen error:", e)

        return jsonify({
            "success": False,
            "message": "Qwen TTS failed. Check the Flask terminal."
        }), 500

    except Exception as e:
        print("Error:", e)

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )