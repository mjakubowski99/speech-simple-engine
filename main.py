import sounddevice as sd 
import json 
from vosk import Model, KaldiRecognizer

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles

MODEL_PATH = "models/vosk-model-en-us-0.22-lgraph"
SAMPLE_RATE = 16000

model = Model(MODEL_PATH)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.websocket("/ws")
async def asr_ws(ws: WebSocket):
    await ws.accept()

    rec = KaldiRecognizer(model, SAMPLE_RATE)
    rec.SetWords(True)

    try:
        while True:
            data = await ws.receive_bytes()

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if result.get("text"):
                    await ws.send_text(json.dumps({
                        "type": "final",
                        "text": result["text"]
                    }))
            else:
                partial = json.loads(rec.PartialResult())
                if partial.get("partial"):
                    await ws.send_text(json.dumps({
                        "type": "partial",
                        "text": partial["partial"]
                    }))

    except Exception:
        await ws.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)
