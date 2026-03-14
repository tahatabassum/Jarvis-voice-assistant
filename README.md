# 🤖 J.A.R.V.I.S — Voice Assistant (Python)

> A Python-based voice assistant inspired by Iron Man's J.A.R.V.I.S — wake word activated, capable of opening websites and playing YouTube songs using voice commands.

---

## 📌 Features

- 🎙️ **Wake Word Activation** — Say "Jarvis" to activate the assistant
- 🌐 **Open Websites** — Open popular websites using voice commands
- 🎵 **Play YouTube Songs** — Play any song on YouTube with your voice
- 🔊 **Text-to-Speech** — Responds back to you with a synthesized voice
- 🛑 **Voice Shutdown** — Say "Goodbye Jarvis" to stop the assistant

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.x | Core language |
| `speech_recognition` | Converts voice to text |
| `pyttsx3` | Text-to-speech engine |
| `pywhatkit` | Plays YouTube songs |
| `webbrowser` | Opens URLs in the browser |

---

## 📂 Project Structure

```
jarvis/
│
├── main.py           # Main assistant logic (wake word, commands, TTS)
├── special_sites.py  # Dictionary of websites and their URLs
└── README.md         # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

### 2. Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 pywhatkit pyaudio
```

> ⚠️ **PyAudio Note:** On Windows, if `pip install pyaudio` fails, try:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```
> On Linux: `sudo apt-get install portaudio19-dev` then `pip install pyaudio`

### 3. Run the Assistant

```bash
python main.py
```

---

## 🗣️ Voice Commands

| Command | What It Does |
|---|---|
| `"Jarvis"` | Activates the assistant |
| `"Open YouTube"` | Opens YouTube in browser |
| `"Open GitHub"` | Opens GitHub in browser |
| `"Open Gmail"` | Opens Gmail in browser |
| `"Open Google"` | Opens Google in browser |
| `"Open ChatGPT"` | Opens ChatGPT in browser |
| `"Open Gemini"` | Opens Google Gemini in browser |
| `"Play [song name]"` | Plays a song on YouTube |
| `"Goodbye Jarvis"` | Shuts down the assistant |

---

## 🌐 Supported Sites (special_sites.py)

You can extend the assistant by adding more sites to `special_sites.py`:

```python
special_sites = {
    "gemini": "https://gemini.google.com",
    "github": "https://github.com",
    "youtube": "https://youtube.com",
    "gmail": "https://mail.google.com",
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "linkedin": "https://linkedin.com",
    "chat gpt": "https://chatgpt.com"
}
```

To add a new site, simply add a key-value pair:
```python
"stackoverflow": "https://stackoverflow.com"
```

---

## 🔧 Configuration

In `main.py`, you can adjust the following settings:

```python
r.energy_threshold = 300      # Mic sensitivity (increase in noisy environments)
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female voice
engine.setProperty('rate', 180)            # Speech speed (words per minute)
```

---

## 🚀 How It Works

```
1. Microphone listens continuously
2. When "Jarvis" is heard → assistant activates
3. Next voice input is processed as a command
4. Command is matched (open site / play song / exit)
5. Assistant responds with TTS and performs the action
6. "Goodbye Jarvis" → assistant shuts down
```

---

## 🔮 Future Improvements

- [ ] Add Wikipedia search integration
- [ ] Add weather updates via API
- [ ] Add alarm/reminder functionality
- [ ] Integrate with OpenAI API for smart Q&A
- [ ] Build a GUI dashboard with PyQt or Tkinter
- [ ] Add conversation memory/context

---

## 🙋‍♂️ Author

**[Your Name]**
- GitHub: [tahatabassum2](https://github.com/tahatabassum)
- LinkedIn: [your-linkedin](https://www.linkedin.com/in/tahatabassum2/)


> ⭐ If you found this project helpful, give it a star on GitHub!
