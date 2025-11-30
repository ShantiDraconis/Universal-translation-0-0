"""
FastAPI Web Application for Universal Translation 0/0.

Provides REST API and web interface for the translation engine.
"""

from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from universal_translation_00 import __version__
from universal_translation_00.core.pipeline_manager import UniversalTranslator
from universal_translation_00.harappan.mapping import HarappanMapping
from universal_translation_00.harappan.renderer import HarappanRenderer
from universal_translation_00.dict00.search import Dict00Search


# Create FastAPI app
app = FastAPI(
    title="Universal Translation 0/0",
    description="Cross-linguistic analysis system for Harappan phoneme reconstruction",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Initialize services
translator = UniversalTranslator()
harappan = HarappanMapping()
renderer = HarappanRenderer()
dict_search = Dict00Search()


# Request/Response models
class TranslateRequest(BaseModel):
    """Translation request model."""

    text: str
    include_etymology: bool = True


class TranslateResponse(BaseModel):
    """Translation response model."""

    original_text: str
    normalized_text: str
    phonetic_reading: str
    harappan_sequence: str
    metadata: dict


class SignResponse(BaseModel):
    """Harappan sign response model."""

    id: str
    group: str
    group_full: str
    phoneme: str
    semantic_field: str
    cognates: dict


class SignListResponse(BaseModel):
    """Response model for sign list."""

    id: str
    group: str
    group_full: str
    phoneme: str
    semantic_field: str
    tamil_root: str
    chinese_root: str
    norse_root: str
    latin_root: str
    tupi_root: str
    description: str


# API Routes
@app.get("/", response_class=HTMLResponse)
async def root() -> str:
    """Root endpoint with basic HTML interface."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Universal Translation 0/0</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #333; }
            .form-group { margin: 20px 0; }
            input[type="text"] { width: 100%; padding: 10px; font-size: 16px; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
            button:hover { background: #0056b3; }
            #result { margin-top: 20px; padding: 20px; background: #f5f5f5; border-radius: 5px; }
            pre { white-space: pre-wrap; }
        </style>
    </head>
    <body>
        <h1>🌍 Universal Translation 0/0</h1>
        <p>Motor de Tradução Universal - Harappan Phoneme Reconstruction</p>
        
        <div class="form-group">
            <input type="text" id="text" placeholder="Enter text to translate..." />
        </div>
        <button onclick="translate()">Translate</button>
        
        <div id="result"></div>
        
        <h2>API Documentation</h2>
        <ul>
            <li><a href="/docs">Swagger UI</a></li>
            <li><a href="/redoc">ReDoc</a></li>
        </ul>
        
        <script>
            async function translate() {
                const text = document.getElementById('text').value;
                const response = await fetch('/api/translate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({text: text})
                });
                const data = await response.json();
                document.getElementById('result').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
            }
        </script>
    </body>
    </html>
    """


@app.post("/api/translate", response_model=TranslateResponse)
async def api_translate(request: TranslateRequest) -> TranslateResponse:
    """Translate text to Harappan phonetic representation."""
    result = translator.translate(request.text)

    return TranslateResponse(
        original_text=result.original_text,
        normalized_text=result.normalized_text,
        phonetic_reading=result.phonetic_reading,
        harappan_sequence=result.harappan_sequence,
        metadata=result.metadata,
    )


@app.get("/api/sign/{sign_id}", response_model=SignResponse)
async def api_get_sign(sign_id: str) -> SignResponse:
    """Get information about a specific Harappan sign."""
    sign = harappan.get_sign(sign_id)

    if not sign:
        raise HTTPException(status_code=404, detail=f"Sign {sign_id} not found")

    return SignResponse(
        id=sign.id,
        group=sign.group,
        group_full=sign.group_full,
        phoneme=sign.phoneme,
        semantic_field=sign.semantic_field,
        cognates=sign.get_cognates(),
    )


@app.get("/api/signs", response_model=list[SignListResponse])
async def api_list_signs(
    group: Optional[str] = Query(None, description="Filter by group"),
    phoneme: Optional[str] = Query(None, description="Filter by phoneme"),
    limit: int = Query(50, le=417, description="Maximum results"),
) -> list[SignListResponse]:
    """List Harappan signs with optional filters."""
    if group:
        signs = harappan.get_signs_by_group(group)
    elif phoneme:
        signs = harappan.phoneme_to_signs(phoneme)
    else:
        signs = harappan.get_all_signs()

    return [s.to_dict() for s in signs[:limit]]


@app.get("/api/groups")
async def api_list_groups() -> list[str]:
    """List all semantic groups."""
    return harappan.get_all_groups()


@app.get("/api/phonemes")
async def api_list_phonemes() -> list[str]:
    """List all unique phonemes."""
    return harappan.get_all_phonemes()


@app.get("/api/search")
async def api_search(
    q: str = Query(..., description="Search query"),
    type: str = Query("phoneme", description="Search type: phoneme, meaning, semantic"),
) -> list[dict]:
    """Search the dictionary."""
    if type == "phoneme":
        return dict_search.search_by_phoneme(q)
    elif type == "meaning":
        return dict_search.search_by_meaning(q)
    elif type == "semantic":
        return dict_search.search_by_semantic_class(q)
    else:
        raise HTTPException(status_code=400, detail=f"Unknown search type: {type}")


@app.get("/api/stats")
async def api_stats() -> dict:
    """Get statistics about the Harappan mapping."""
    return harappan.get_statistics()


@app.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": __version__,
        "total_signs": len(harappan.get_all_signs()),
    }
