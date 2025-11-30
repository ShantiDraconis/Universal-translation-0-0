# Universal Translation Engine 0/0

[![Tests](https://github.com/ShantiDraconis/Universal-translation-0-0/actions/workflows/tests.yml/badge.svg)](https://github.com/ShantiDraconis/Universal-translation-0-0/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Um framework modular para tradução universal, integrando fonemas universais, signos Harappan, múltiplas famílias linguísticas, análise simbólica e numerológica.

## 🌍 Visão Geral

O **Mecanismo Universal de Tradução 0/0** é uma ferramenta conceitual e computacional que busca:

- Decifrar padrões fonéticos universais
- Conectar línguas ancestrais e modernas
- Revelar significados simbólicos e arquetípicos
- Integrar sistemas de conhecimento diversos
- Fornecer uma API e CLI para análise linguística

## ⚡ Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/ShantiDraconis/Universal-translation-0-0.git
cd Universal-translation-0-0

# Instale o pacote
pip install -e .

# (Opcional) Instale dependências da API
pip install -e ".[api]"
```

## 🚀 Como Usar

### Opção 1: Python API

```python
from universal_translation.api.translate import translate, get_universal_phrase

# Tradução padrão
result = translate("Hello world")
print(result["tokens"])      # ['Hello', 'world']
print(result["numerology"])  # Análise numerológica

# Pipeline completo de 10 etapas
result = translate("Om mani padme hum", mode="full")
print(result["stage_10_universal"])

# Frase Universal
phrase = get_universal_phrase("fire water earth")
print(phrase)  # "Universal Translation 0/0: fire, water | elements | Root 4"
```

### Opção 2: CLI (Linha de Comando)

```bash
# Tradução básica
universal-translate "Hello world"

# Pipeline completo
universal-translate --mode full "Om mani padme hum"

# Decodificar signos Harappan
universal-translate --harappan 8 13 75

# Análise numerológica
universal-translate --numerology "Sacred text"

# Apenas a frase universal
universal-translate --phrase "fire water earth"
```

### Opção 3: API REST (FastAPI)

```bash
# Iniciar servidor
pip install -e ".[api]"
uvicorn universal_translation.api.server_fastapi:app --reload

# Endpoints disponíveis:
# POST /translate - Tradução de texto
# POST /harappan/decode - Decodificar signos Harappan
# POST /numerology - Análise numerológica
# POST /symbolic - Análise simbólica
# POST /universal-phrase - Frase Universal
```

### Opção 4: Prompts para LLMs

Use os prompts em `docs/pipelines/` com modelos de linguagem (ChatGPT, Claude, etc.):

| Etapa | Arquivo | Descrição |
|-------|---------|-----------|
| Master | [20-prompt-universal-0-0.md](docs/pipelines/20-prompt-universal-0-0.md) | Pipeline completo |
| 1 | [21-prompt-segmentacao.md](docs/pipelines/21-prompt-segmentacao.md) | Segmentação + Inversão |
| 2 | [22-prompt-dicionario-00.md](docs/pipelines/22-prompt-dicionario-00.md) | Mapeamento Dicionário 00 |
| 3 | [23-prompt-harappan.md](docs/pipelines/23-prompt-harappan.md) | Projeção Harappan |
| 4 | [24-prompt-familias-linguisticas.md](docs/pipelines/24-prompt-familias-linguisticas.md) | 12 Famílias Linguísticas |
| 5 | [25-prompt-decodificacao-simbolica.md](docs/pipelines/25-prompt-decodificacao-simbolica.md) | Decodificação 0/0 |
| 7 | [26-prompt-numerologia-astrologia.md](docs/pipelines/26-prompt-numerologia-astrologia.md) | Numerologia + Astrologia |
| 8-10 | [27-prompt-sintese-final.md](docs/pipelines/27-prompt-sintese-final.md) | Síntese Final |

## 📂 Estrutura do Repositório

```
Universal-translation-0-0/
├── README.md
├── LICENSE
├── CITATION.cff
├── pyproject.toml
├── requirements.txt
├── setup.py
│
├── universal_translation/          # 🐍 Pacote Python principal
│   ├── core/                       # Engines de tradução
│   │   ├── tokenizer.py           # Tokenização de texto
│   │   ├── phoneme_engine.py      # Motor de fonemas universais
│   │   ├── harappan_engine.py     # Decodificação Harappan
│   │   ├── numerology_engine.py   # Numerologia e 0/0
│   │   ├── semiotics_engine.py    # Análise semiótica
│   │   ├── embeddings.py          # Vetores de significado
│   │   └── pipeline.py            # Pipeline unificada
│   │
│   ├── mappings/                   # 📊 Mapeamentos JSON
│   │   ├── universal_map.json     # Mapa universal de conceitos
│   │   ├── harappan_map.json      # Mapa de signos Harappan
│   │   ├── phoneme_map.json       # Mapa de fonemas
│   │   └── numerology_map.json    # Mapa numerológico
│   │
│   ├── datasets/                   # 📁 Datasets
│   │   ├── harappan/              # Signos Harappan (417 + 694)
│   │   └── universal/             # Fonemas, raízes, símbolos
│   │
│   ├── api/                        # 🔌 API e CLI
│   │   ├── translate.py           # Interface de tradução
│   │   ├── server_fastapi.py      # Servidor REST
│   │   └── cli.py                 # Interface de linha de comando
│   │
│   ├── evaluation/                 # 📏 Avaliação
│   │   ├── metrics.py             # Métricas de avaliação
│   │   ├── human_review_protocol.md
│   │   └── scoring_system.yaml
│   │
│   └── utils/                      # 🔧 Utilitários
│       ├── loaders.py             # Carregadores de dados
│       ├── validators.py          # Validadores
│       └── converters.py          # Conversores
│
├── docs/                           # 📚 Documentação
│   ├── pipelines/                 # Prompts para LLMs
│   ├── architecture.md            # Arquitetura do sistema
│   ├── api.md                     # Documentação da API
│   ├── data-standards.md          # Padrões de dados
│   ├── harappan-sign-list.md      # Lista de signos
│   ├── phoneme-table.md           # Tabela de fonemas
│   └── numerology-table.md        # Tabela de numerologia
│
├── tests/                          # ✅ Testes (68 testes)
│
├── examples/                       # 📓 Notebooks de exemplo
│   ├── notebook_translation.ipynb
│   ├── harappan_decoding.ipynb
│   └── universal_prompt_demo.ipynb
│
├── .github/workflows/              # 🔄 CI/CD
│   ├── tests.yml
│   ├── validate-data.yml
│   └── build.yml
│
└── harappan-00-universal/          # 🏛️ Dados Harappan originais
    └── data/
        ├── harappan_signs/        # CSV/JSON dos signos
        └── mappings/              # Mapeamentos linguísticos
```

## 🔮 O Pipeline de 10 Etapas

O motor de tradução implementa um pipeline completo de 10 etapas:

| Etapa | Nome | Descrição |
|-------|------|-----------|
| 1 | Segmentação | Tokenização, sílabas, inversão |
| 2 | Fonemas | Mapeamento fonético universal (IPA) |
| 3 | Harappan | Projeção pictográfica (417 signos) |
| 4 | Famílias | 12 famílias linguísticas |
| 5 | Simbólico | Arquétipos e operador 0/0 |
| 6 | Arqueocosmo | Proto-língua e padrões ancestrais |
| 7 | Numerologia | Pitagórica, cabalística |
| 8 | Traduções | Literal, arquetípica, energética |
| 9 | Diagrama | Métricas e visualização |
| 10 | Universal | Frase síntese final |

## 🧬 Componentes do Sistema

### Motor de Tradução (`universal_translation/core/`)
- **tokenizer.py** - Segmentação de texto em tokens, sílabas, fonemas
- **phoneme_engine.py** - Mapeamento para fonemas universais (IPA)
- **harappan_engine.py** - Decodificação dos 417 signos Harappan
- **numerology_engine.py** - Análise numerológica (Pitágoras, Gematria)
- **semiotics_engine.py** - Análise semiótica e arquetípica
- **pipeline.py** - Orquestração do pipeline de 10 etapas

### Dados Harappan (`harappan-00-universal/`)
- 417 signos Mahadevan (CSV/JSON)
- 694 variantes Wells
- Mapeamentos para Tupi, Hebraico, Sânscrito

### Operador 0/0
Conceito central: **I = 0/0** representa a indeterminação criativa - o ponto onde origem e fim se encontram.

```python
# O 0/0 normaliza valores para uma escala de potencial
from universal_translation.core.numerology_engine import normalize_to_zero_over_zero
value = normalize_to_zero_over_zero(42)  # Retorna valor em [0, 1]
```

## 📖 Exemplos de Uso

### Análise de Mantra (Python)

```python
from universal_translation.core.pipeline import full_pipeline

result = full_pipeline("Om mani padme hum")
print(result["stage_7_numerology"])
print(result["stage_10_universal"])
```

### Decodificação Harappan

```python
from universal_translation.api.translate import decode_harappan

# Decodificar sequência: Peixe (8), Touro (13), Lótus (75)
result = decode_harappan([8, 13, 75])
for sign in result["decoded_signs"]:
    print(f"{sign['mahadevan_id']}: {sign['category']} -> {sign['universal_code']}")
```

### Análise Numerológica

```python
from universal_translation.core.numerology_engine import analyze_phrase

result = analyze_phrase("Universal")
print(f"Valor: {result['total_value']}, Raiz: {result['total_root']}")
print(f"Significado: {result['phrase_meaning']['archetype']}")
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Áreas de interesse:

- Expansão do Dicionário 00
- Mapeamento de novos signos Harappan
- Adição de famílias linguísticas
- Refinamento dos prompts
- Melhorias nos engines de tradução
- Novos datasets e mapeamentos

### Executando Testes

```bash
pip install -e ".[dev]"
pytest tests/ -v
```

## 📚 Documentação

- [Arquitetura do Sistema](docs/architecture.md)
- [API Reference](docs/api.md)
- [Padrões de Dados](docs/data-standards.md)
- [Lista de Signos Harappan](docs/harappan-sign-list.md)
- [Tabela de Fonemas](docs/phoneme-table.md)
- [Tabela de Numerologia](docs/numerology-table.md)

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📑 Citação

Se você usar este projeto em sua pesquisa, por favor cite:

```bibtex
@software{universal_translation_0_0,
  title = {Universal Translation Engine 0/0},
  author = {Draconis, Shanti},
  year = {2025},
  url = {https://github.com/ShantiDraconis/Universal-translation-0-0}
}
```

## 🙏 Agradecimentos

Este projeto é inspirado em:
- Linguística comparada e estudos de proto-línguas
- Corpus de Mahadevan (1977) para signos Harappan
- Tradições sagradas diversas
- Numerologia pitagórica e simbolismo universal

## 🔗 Referências

1. Mahadevan, I. (1977). *The Indus Script: Texts, Concordance and Tables*
2. Wells, B. (2006). *Indus Signs: A List of Sign Types*
3. Parpola, A. (1994). *Deciphering the Indus Script*
---

**"A voz do som primordial atravessando os povos e restaurando a linguagem mãe."**

*Tradução Universal 0/0*
