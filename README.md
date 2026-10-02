# 🇩🇪 German Learning Video AI

<p align="center">
  <strong>A local AI-powered web application for creating German learning dialogue content.</strong>
</p>

<p align="center">
  Generate German dialogue audio locally using <strong>Qwen3-TTS</strong> through a simple Flask web interface.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-black)
![Qwen3--TTS](https://img.shields.io/badge/Qwen3--TTS-Local-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

---

## 📌 Project Overview

**German Learning Video AI** is a local AI project designed to help create German-learning conversations.

The project is designed around a simple workflow:

```text
Choose / Enter Dialogue
        ↓
Local Flask Web Interface
        ↓
Qwen3-TTS
        ↓
German Character A Voice
        +
German Character B Voice
        ↓
WAV Audio Files
```

The long-term goal is to turn these conversations into complete German-learning videos containing:

* 🇩🇪 German dialogue
* 🇬🇧 English translations
* 👤 Multiple characters
* 🗣️ Local AI voices
* 👄 Lip synchronization
* 🎬 Vertical 9:16 videos
* 📝 Bilingual subtitles
* 🎨 AI-generated characters
* 🌐 A completely local web interface

> **Current status:** The Flask interface and Qwen3-TTS integration are working. Video/lip-sync automation is planned for the next development stage.

---

# ✨ Current Features

### 🌐 Local Web Interface

The application runs locally using Flask.

```text
http://127.0.0.1:5000
```

No public server is required.

### 🗣️ Local German AI Voices

The project uses:

**Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice**

Available speakers include:

```text
aiden
dylan
eric
ono_anna
ryan
serena
sohee
uncle_fu
vivian
```

### 👥 Two Character Voices

The application can generate separate audio for:

```text
Character A
Character B
```

### 📝 Manual Dialogue

You can enter your own German conversation manually.

Example:

```text
Guten Tag! Wie geht es Ihnen?
Mir geht es sehr gut, danke. Und Ihnen?
Auch sehr gut. Was machen Sie heute?
Ich gehe heute ins Restaurant.
```

### 💻 Completely Local

The current system is designed to run on your own Windows PC.

No:

* ❌ ngrok
* ❌ paid API
* ❌ cloud TTS API
* ❌ online voice generation

is required for the current Qwen TTS workflow.

---

# 🖥️ Requirements

## Hardware

The application can run on relatively modest hardware, although AI generation can be slow.

Example development system:

```text
CPU: Intel Core i5-7400
RAM: 16 GB
GPU: AMD Radeon RX 580 8 GB
OS: Windows 11
```

Qwen TTS is currently running through the local Python environment.

> GPU acceleration depends on your specific PyTorch/DirectML configuration. CPU execution is also possible but slower.

---

# 📦 Software Requirements

Install the following:

* Windows 10/11
* Python 3.12
* Git
* FFmpeg
* SoX
* Qwen3-TTS
* Flask

---

# 🚀 Installation — A to Z

## 1. Clone the repository

Open PowerShell:

```powershell
git clone https://github.com/webX22/German-Learning-Video-AI.git
```

Enter the project:

```powershell
cd German-Learning-Video-AI
```

---

# 2. Create the Python virtual environment

Create a dedicated environment:

```powershell
py -3.12 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Your terminal should now look similar to:

```text
(.venv) PS C:\...\German-Learning-Video-AI>
```

---

# 3. Upgrade pip

Run:

```powershell
python -m pip install --upgrade pip
```

---

# 4. Install Flask

Install Flask:

```powershell
python -m pip install flask
```

Verify:

```powershell
python -c "import flask; print('Flask:', flask.__version__)"
```

You should see a Flask version such as:

```text
Flask: 3.1.3
```

---

# 5. Install Qwen3-TTS

The project uses Qwen3-TTS locally.

Install the required package:

```powershell
python -m pip install -U qwen-tts
```

You may also need:

```powershell
python -m pip install soundfile
```

Verify the installation:

```powershell
python -c "from qwen_tts import Qwen3TTSModel; print('Qwen3-TTS OK')"
```

Expected:

```text
Qwen3-TTS OK
```

---

# 6. Download the Qwen model

The first time Qwen is used, Hugging Face will download the model automatically.

The current model is:

```text
Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice
```

The model will be cached locally.

You do not need to manually download the model every time.

---

# 7. Install FFmpeg

FFmpeg is required for the future video-generation pipeline and is also useful for processing audio/video.

Verify:

```powershell
ffmpeg -version
```

If FFmpeg is installed correctly, you should see its version information.

---

# 8. Install SoX

SoX is useful for audio processing.

Verify:

```powershell
sox --version
```

Example:

```text
SoX v14.4.2
```

---

# 🧪 Test Qwen TTS Before Starting the Web App

Before using Flask, test Qwen directly.

Run:

```powershell
python generate_audio.py "Guten Tag! Wie geht es Ihnen heute?" test.wav serena
```

The terminal should eventually show:

```text
Loading Qwen TTS...
Generating German voice with speaker: serena
Audio created: test.wav
```

You should now have:

```text
test.wav
```

in the project directory.

Open the file and verify that you can hear the German voice.

---

# 🌐 Start the Web Application

Once Qwen works correctly, start Flask:

```powershell
python app.py
```

You should see:

```text
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# 🎛️ Using the Web Interface

The interface allows you to enter a German conversation.

For example:

```text
Guten Tag! Wie geht es Ihnen?
Mir geht es sehr gut, danke. Und Ihnen?
Auch sehr gut.
Was machen Sie heute?
Ich gehe heute ins Restaurant.
```

Select the desired voices.

Example:

```text
Character A → Serena
Character B → Ryan
```

Then click:

```text
GENERATE VIDEO
```

> At the current development stage, the web application generates the Character A and Character B audio files. Full automatic video generation is part of the next development stages.

---

# 🎙️ Available Qwen Voices

| Speaker  | ID         |
| -------- | ---------- |
| Aiden    | `aiden`    |
| Dylan    | `dylan`    |
| Eric     | `eric`     |
| Anna     | `ono_anna` |
| Ryan     | `ryan`     |
| Serena   | `serena`   |
| Sohee    | `sohee`    |
| Uncle Fu | `uncle_fu` |
| Vivian   | `vivian`   |

When using the API/script, use the **ID**, not `male` or `female`.

Correct:

```text
serena
```

Incorrect:

```text
female
```

---

# 📁 Project Structure

```text
German-Learning-Video-AI/
│
├── app.py
│
├── generate_audio.py
│
├── templates/
│   └── index.html
│
├── output/
│   └── generated audio files
│
├── .gitignore
│
└── README.md
```

The following directories/files are intentionally excluded from Git:

```text
.venv/
output/
*.wav
*.mp4
*.pth
*.safetensors
```

This keeps the GitHub repository small and prevents AI models and generated media from being uploaded.

---

# 🧠 How the Current System Works

The browser sends the dialogue to Flask:

```text
Browser
   ↓
Flask /generate
   ↓
Parse dialogue
   ↓
Character A text
Character B text
   ↓
Qwen3-TTS
   ↓
Character A WAV
Character B WAV
```

The generated files are saved in:

```text
output/
```

Each generation receives a unique job ID.

Example:

```text
96b82331_character_A.wav
96b82331_character_B.wav
```

---

# 🎬 Planned Video Pipeline

The project is being developed toward the following pipeline:

```text
             ┌──────────────────┐
             │  German Topic    │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │ German Dialogue  │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │    Qwen3-TTS     │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │ Character Audio  │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │     Wav2Lip      │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │ Talking Character│
             │      Video       │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │ Bilingual Subs   │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │     FFmpeg       │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │ Final 9:16 MP4   │
             └──────────────────┘
```

---

# 🔮 Planned Features

## Phase 1 — Current

* [x] Flask web interface
* [x] Manual German dialogue
* [x] Qwen3-TTS integration
* [x] Character A voice
* [x] Character B voice
* [x] Local WAV generation

## Phase 2

* [ ] Built-in German topics
* [ ] A1 / A2 / B1 / B2 levels
* [ ] Automatic dialogue generation
* [ ] Multiple dialogue lengths
* [ ] Better character voice selection

Example topics:

```text
Restaurant
Shopping
Airport
Hotel
Doctor
Work
Travel
Daily Routine
School
Job Interview
Supermarket
Train Station
```

## Phase 3

* [ ] Generate individual audio per dialogue line
* [ ] Character A/B turn management
* [ ] Automatic timing
* [ ] Automatic subtitle timing

## Phase 4

* [ ] Wav2Lip integration
* [ ] Automatic lip synchronization
* [ ] Character A video
* [ ] Character B video

## Phase 5

* [ ] ComfyUI character generation
* [ ] Generate new characters from the web interface
* [ ] Character consistency
* [ ] Different environments

## Phase 6

* [ ] Automatic bilingual subtitles
* [ ] German large text
* [ ] English translation underneath
* [ ] 9:16 vertical video
* [ ] Camera movement
* [ ] Final MP4 preview

## Phase 7

* [ ] Background processing
* [ ] Generation progress
* [ ] Job IDs
* [ ] Browser video preview
* [ ] Download generated video
* [ ] One-click complete generation

---

# ⚡ Performance Notes

AI generation can be slow on lower-end hardware.

For example, the project can work with:

```text
16 GB RAM
RX 580 8 GB
```

but generation speed depends heavily on:

* Model
* CPU
* GPU backend
* VRAM available to PyTorch
* Resolution
* Video length
* Number of characters
* Number of dialogue lines

For this reason, the project is designed to generate the content locally without requiring an expensive cloud API.

---

# 🛠️ Troubleshooting

## Flask does not start

Check that the virtual environment is activated:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then:

```powershell
python app.py
```

---

## `ModuleNotFoundError: flask`

Install Flask:

```powershell
python -m pip install flask
```

---

## `ModuleNotFoundError: qwen_tts`

Install Qwen TTS:

```powershell
python -m pip install -U qwen-tts
```

---

## Unsupported Qwen speaker

If you see:

```text
Unsupported speakers: ['female']
```

the application is sending an invalid speaker ID.

Use one of:

```text
aiden
dylan
eric
ono_anna
ryan
serena
sohee
uncle_fu
vivian
```

---

## `flash-attn is not installed`

You may see:

```text
Warning: flash-attn is not installed.
Will only run the manual PyTorch version.
```

This does not necessarily mean Qwen failed.

If audio is successfully generated, the system is working.

---

## Port 5000 is already in use

Stop the existing Flask process with:

```text
CTRL+C
```

Then restart:

```powershell
python app.py
```

---

# 🔐 Privacy

The current application is designed to run locally.

Your dialogue is processed by the local application and local AI models.

The project does not require a public URL or ngrok.

Do not add private API keys, passwords, tokens, or personal information to the repository.

---

# 📜 License

This project is intended as an open-source learning and development project.

Before redistributing models, model weights, generated assets, or third-party components, check their individual licenses and usage restrictions.

The source code of this project can be licensed separately from the AI models it uses.

---

# 👨‍💻 Development

Created by **webX22**.

GitHub:

**https://github.com/webX22/German-Learning-Video-AI**

---

# ⭐ Project Goal

The final goal is a simple local application where the user can:

```text
1. Open the website
        ↓
2. Choose a German topic
        ↓
3. Choose language level
        ↓
4. Choose two characters
        ↓
5. Generate dialogue
        ↓
6. Generate German AI voices
        ↓
7. Generate talking characters
        ↓
8. Add German + English subtitles
        ↓
9. Create a vertical 9:16 video
        ↓
10. Watch the final video
```

All from one local web interface.

<p align="center">
  <strong>🇩🇪 Learn German. Create conversations. Generate videos locally. 🚀</strong>
</p>
