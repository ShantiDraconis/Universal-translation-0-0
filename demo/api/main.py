from fastapi import FastAPI
from pydantic import BaseModel

from universal_translation.api.translate import translate

app = FastAPI(
    title="Universal Translation Engine 0/0 – Demo",
    description=(
        "Public demo API for symbolic universal translation: "
        "Harappan decoding, universal phonemes and 0/0 numerology."
    ),
    version="0.1.0",
)


class TranslationRequest(BaseModel):
    text: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/translate")
def translate_endpoint(req: TranslationRequest):
    """
    Run the full translation pipeline on a text string.
    """
    return translate(req.text)
