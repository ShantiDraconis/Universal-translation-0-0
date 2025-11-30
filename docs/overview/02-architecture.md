# Arquitetura do Sistema

## Visão Geral

O Motor de Tradução Universal 0/0 é composto por múltiplos módulos interconectados que processam texto de entrada através de várias camadas de análise.

```
┌─────────────────────────────────────────────────────────────┐
│                    ENTRADA DE TEXTO                          │
│         (qualquer idioma: Tamil, Latim, Chinês, etc.)       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE NORMALIZAÇÃO                    │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │ Tokenizer   │  │ Normalizer  │  │Transliterate│         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  CAMADA DE SEGMENTAÇÃO FONÉTICA             │
│  ┌─────────────────────────────────────────────┐           │
│  │          Phoneme Segmenter                   │           │
│  │   • CV patterns (ka, ta, ma, etc.)          │           │
│  │   • CVC patterns (tak, sak, ram, etc.)      │           │
│  │   • Vowels (a, i, u, e, o)                  │           │
│  └─────────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   CAMADA DE MAPEAMENTO                       │
│  ┌────────────────┐  ┌────────────────┐                    │
│  │ Dict00 Search  │  │ Harappan Map   │                    │
│  │   • Phoneme    │  │   • Sign ID    │                    │
│  │   • Semantic   │  │   • Group      │                    │
│  │   • Meaning    │  │   • Phoneme    │                    │
│  └────────────────┘  └────────────────┘                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE ANÁLISE                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Numerology│  │ Geometry │  │Etymology │  │ Symbolic │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE SAÍDA                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   Text   │  │   JSON   │  │   IPA    │  │ Harappan │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Módulos Principais

### 1. Core (`universal_translation_00.core`)

#### Tokenizer
Responsável por dividir texto em tokens, detectando automaticamente o script:
- Latin, Devanagari, Tamil, Chinese, Hebrew, Arabic, etc.

#### Normalizer
Normaliza texto através de:
- Unicode normalization (NFC)
- Transliteração de scripts não-latinos
- Remoção de diacríticos (opcional)

#### Phoneme Segmenter
Segmenta tokens em fonemas usando padrões:
- CV (Consoante + Vogal): ka, ta, ma, etc.
- CVC (Consoante + Vogal + Consoante): tak, ram, kum, etc.
- V (Vogal): a, i, u, e, o

### 2. Harappan (`universal_translation_00.harappan`)

#### Mapping
Mapeia fonemas para signos Harappan (H001-H417):
- Carrega dados do CSV
- Indexa por ID, fonema e grupo
- Busca por campo semântico

#### Numerics
Análise numerológica dos signos:
- Valor pitagórico
- Gematria cabalística
- Posição no grupo

#### Geometry
Análise geométrica e cosmológica:
- Classe de forma
- Elemento associado
- Zona cósmica

### 3. Dict00 (`universal_translation_00.dict00`)

#### Loader
Carrega o Dicionário Universal 0/0:
- Tokens fonéticos universais
- Significados em múltiplos idiomas
- Classes semânticas

#### Search
Busca no dicionário:
- Por fonema (exato e fuzzy)
- Por significado
- Por classe semântica

#### Scoring
Pontuação de similaridade fonética:
- Distância de Levenshtein
- Matching de features fonéticas
- Padrões CV

### 4. CLI (`universal_translation_00.cli`)

Interface de linha de comando:
- `translate`: Tradução de texto
- `search`: Busca de signos
- `list-group`: Lista signos por grupo
- `analyze-phoneme`: Análise de fonema
- `stats`: Estatísticas do sistema

### 5. Web (`universal_translation_00.web`)

API REST com FastAPI:
- `/api/translate`: Endpoint de tradução
- `/api/sign/{id}`: Busca de signo
- `/api/signs`: Lista de signos
- `/api/search`: Busca no dicionário

## Fluxo de Dados

```
Input Text
    │
    ├─► Tokenizer ─► Tokens (word, number, punct)
    │
    ├─► Normalizer ─► Normalized text
    │
    ├─► Segmenter ─► Phonemes (ta, ma, ka, ...)
    │
    ├─► HarappanMapping ─► Signs (H001, H047, ...)
    │
    ├─► Dict00Search ─► Dictionary entries
    │
    └─► TranslationResult
            │
            ├─► original_text
            ├─► normalized_text
            ├─► phonemes
            ├─► harappan_signs
            ├─► phonetic_reading
            └─► metadata
```

## Extensibilidade

O sistema é projetado para fácil extensão:

1. **Novos idiomas**: Adicionar módulo em `languages/`
2. **Novos signos**: Atualizar CSV em `data/raw/`
3. **Novas análises**: Adicionar módulo em `analysis/`
4. **Novas camadas**: Adicionar em `translation/`

## Verificação Formal

O sistema inclui provas formais em:
- **Lean 4**: Provas de consistência
- **Coq**: Verificação de mapeamentos
- **Isabelle/HOL**: Teoria de tipos
- **Agda**: Provas construtivas

Garantindo que:
- Cada ID mapeia para exatamente um grupo
- Grupos são mutuamente exclusivos
- Mapeamentos são determinísticos
