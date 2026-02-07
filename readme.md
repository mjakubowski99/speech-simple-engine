# Speech Engine - Real-time Speech Recognition API

A FastAPI-based sample web application providing real-time speech-to-text transcription using Vosk speech recognition engine.

## Prerequisites

- Python 3.8 or higher
- `wget` (for downloading the model)
- Microphone access (for testing)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd speech-engine
```

### 2. Create virtual environment

```bash
python3 -m venv venv
```

### 3. Activate virtual environment

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Download Vosk model

This is a model recognizing english language.
```bash
mkdir -p models/ && cd models/ && \
wget https://alphacephei.com/vosk/models/vosk-model-en-us-0.22-lgraph.zip && \
unzip vosk-model-en-us-0.22-lgraph.zip && \
cd ..
```
You can download any model you want from this website: https://alphacephei.com/vosk/models

**Note:** The model will be extracted to `models/vosk-model-en-us-0.22-lgraph/`

## Usage

### Start the application

```bash
python main.py
```

The server will start on `http://localhost:9000`

### Access the web interface

Open your browser and navigate to:
```
http://localhost:9000/static
```

### WebSocket Endpoint

**URL:** `ws://localhost:9000/ws`

**Connection:**
- Accepts binary audio data (PCM16, 16kHz sample rate)
- Sends JSON messages with transcription results

**Message Format:**

**Partial Results:**
```json
{
  "type": "partial",
  "text": "partial transcription text"
}
```

**Final Results:**
```json
{
  "type": "final",
  "text": "final transcription text"
}
```

Default settings in `main.py`:
- **Model Path:** `models/vosk-model-en-us-0.22-lgraph`
- **Sample Rate:** 16000 Hz
- **Host:** `0.0.0.0`
- **Port:** `9000`

To modify these settings, edit the constants in `main.py`.
