"""
universal_translation/api/server_fastapi.py

FastAPI server exposing the Universal Translation Engine 0/0.

This module provides a REST API with endpoints for:
- Text translation
- Harappan decoding
- Numerological analysis
- Symbolic meaning extraction

Run with:
    uvicorn universal_translation.api.server_fastapi:app --reload

Example requests:
    POST /translate {"text": "Hello world"}
    POST /harappan/decode {"sign_ids": [1, 8, 15]}
    POST /numerology {"text": "Om"}
"""

from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from universal_translation.api.translate import (
    translate,
    decode_harappan,
    analyze_numerology,
    get_symbolic_meaning,
    search_harappan_signs,
    get_universal_phrase,
)

app = FastAPI(
    title="Universal Translation Engine 0/0",
    description="""
A modular framework for universal translation integrating phonemes,
Harappan signs, multiple linguistic families, symbolic analysis and numerology.

The Universal Translation Engine implements a 10-stage pipeline:
1. Segmentation + Inversion
2. Dictionary 00 mapping
3. Harappan projection
4. 12 Language families
5. Symbolic 0/0 decoding
6. Archaeo-cosmological analysis
7. Numerology
8. Multiple translation
9. Final diagram
10. Universal phrase
    """,
    version="0.1.0",
)


# Request/Response Models
class TranslationRequest(BaseModel):
    """Request model for text translation."""

    text: str = Field(..., description="Input text to translate")
    mode: str = Field(
        default="standard",
        description="Translation mode: 'standard', 'full', or 'simple'",
    )


class HarappanDecodeRequest(BaseModel):
    """Request model for Harappan decoding."""

    sign_ids: List[int] = Field(
        ...,
        description="List of Mahadevan sign indices (1-417)",
    )


class NumerologyRequest(BaseModel):
    """Request model for numerological analysis."""

    text: str = Field(..., description="Input text to analyze")


class SearchRequest(BaseModel):
    """Request model for Harappan sign search."""

    query: str = Field(..., description="Search query")


class UniversalPhraseRequest(BaseModel):
    """Request model for universal phrase generation."""

    text: str = Field(..., description="Input text")


# Endpoints
@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Universal Translation Engine 0/0",
        "version": "0.1.0",
        "endpoints": [
            "/translate",
            "/harappan/decode",
            "/harappan/search",
            "/numerology",
            "/symbolic",
            "/universal-phrase",
        ],
    }


@app.post("/translate")
async def translate_endpoint(req: TranslationRequest):
    """
    Translate text using the Universal Translation Engine.

    - **text**: Input text to translate
    - **mode**: Translation mode (standard/full/simple)
    """
    try:
        return translate(req.text, req.mode)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/harappan/decode")
async def harappan_decode_endpoint(req: HarappanDecodeRequest):
    """
    Decode a sequence of Harappan sign IDs.

    - **sign_ids**: List of Mahadevan indices (1-417)
    """
    # Validate sign IDs
    for sid in req.sign_ids:
        if not 1 <= sid <= 417:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid sign ID: {sid}. Must be between 1 and 417.",
            )

    try:
        return decode_harappan(req.sign_ids)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/harappan/search")
async def harappan_search_endpoint(req: SearchRequest):
    """
    Search for Harappan signs matching a query.

    - **query**: Search query (matches description and category)
    """
    try:
        results = search_harappan_signs(req.query)
        return {"query": req.query, "results": results, "count": len(results)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/numerology")
async def numerology_endpoint(req: NumerologyRequest):
    """
    Perform numerological analysis on text.

    - **text**: Input text to analyze
    """
    try:
        return analyze_numerology(req.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/symbolic")
async def symbolic_endpoint(req: NumerologyRequest):
    """
    Get symbolic/archetypal meanings for text.

    - **text**: Input text to analyze
    """
    try:
        return get_symbolic_meaning(req.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/universal-phrase")
async def universal_phrase_endpoint(req: UniversalPhraseRequest):
    """
    Generate the Universal 0/0 phrase for text.

    This returns the final output of the 10-stage pipeline.

    - **text**: Input text
    """
    try:
        phrase = get_universal_phrase(req.text)
        return {"input": req.text, "universal_phrase": phrase}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "Universal Translation Engine 0/0"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
