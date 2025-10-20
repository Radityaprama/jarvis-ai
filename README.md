# Jarvis AI (Offline Version)

Project ini adalah **asisten suara offline** berbasis Python — bisa mengenali perintah suara dan merespons balik dengan suara (tanpa koneksi internet dan tanpa API key).  
Dibuat untuk berjalan **sepenuhnya di lokal**, tanpa tergantung pada OpenAI API atau layanan cloud lainnya.

---

## Fitur Utama
-  **Voice Recognition** — mengenali perintah suara dari microphone.  
-  **Text-to-Speech Offline** — menggunakan `pyttsx3` (suara bawaan Windows).  
-  **Command System** — bisa diperluas untuk menjalankan perintah (buka aplikasi, buka website, dll).  
-  **Tanpa API Key** — tidak butuh internet untuk berjalan.  

---

##  Teknologi yang Digunakan
- Python 3.9+
- `pyttsx3` → untuk text-to-speech
- `speech_recognition` → untuk input suara
- (Opsional) `pyaudio` → untuk akses mic
- (Opsional) `pocketsphinx` → mode pengenalan suara offline

---

## 🖥️ Cara Menjalankan
1. Clone repo ini:
   ```bash
   git clone https://github.com/Radityaprama/jarvis-ai.git
   cd jarvis-ai
