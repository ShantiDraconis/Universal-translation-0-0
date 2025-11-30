# Universal Translation 0/0 - Motor de Tradução Universal

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 🌍 Visão Geral

O **Motor de Tradução Universal 0/0** é um sistema de análise linguística cruzada para reconstrução dos fonemas Harappan através de análise fonética comparativa entre Tamil, Chinês Arcaico, Nórdico Antigo, Latim, Tupi e outras famílias linguísticas.

Este projeto cria uma **Pedra de Roseta moderna** para o script do Vale do Indo (Harappan), mapeando os 417 signos para fonemas baseados em raízes fonéticas universais que aparecem em múltiplas famílias linguísticas.

## 🎯 Objetivos

1. **Mapear todos os 417 signos Harappan** para fonemas baseados em análise linguística cruzada
2. **Identificar raízes fonéticas universais** que aparecem em múltiplas famílias linguísticas
3. **Criar um sistema de tradução** que conecta significados semânticos globais
4. **Formalizar matematicamente** as relações fonéticas em Lean, Coq, Isabelle e Agda
5. **Fornecer ferramentas práticas** (CLI, API, Web) para pesquisa e experimentação

## 📊 Metodologia

### Raízes Fonéticas Globais

Os fonemas são atribuídos baseados em sons que aparecem com significados similares em múltiplas línguas:

| Fonema | Significado Global | Exemplos |
|--------|-------------------|----------|
| ma/ama | mãe, pessoa, origem, matéria | Tamil "amma", Latim "māter", Português "mãe" |
| na/ni | eu, pessoa, alguém, ser | Tamil "naan", Tibetano "na" (eu) |
| ka/ga | pedra, casa, lugar, objeto sólido | Raízes dravídicas "ka", Austronésias "ka" |
| ta/ti/tu | bater, cortar, fazer, tempo | Inglês "to do", "take" |
| sa/si/su | sopro, espírito, fluxo, sacro | Latim "spiritus", Chinês 水/苏 |
| ra/ri/ru | correr, fluxo, linha, rei/ordem | Egípcio "ra", Espanhol "río" |

### Grupos Semânticos Harappan

Os 417 signos são organizados em grupos semânticos:

| Grupo | Range | Descrição | Fonemas Principais |
|-------|-------|-----------|-------------------|
| NUM_TALLY | H001-H040 | Contagem, números | ta, ti, tu, na, ni, sa, si, su, wa, ya, ri |
| CONTAINER | H041-H080 | Jarros, recipientes | ka, ko, ku, ga, go, gu, ma, mo, mu, pa, po, pu |
| GRID_FIELD | H081-H110 | Campos, grades | ra, ri, ru, la, li, lu, re, le, ro, we |
| CHEVRON_MOUNTAIN | H111-H130 | Montanhas, picos | ka, ki, ku, ha, hi, hu, ta, ti, tu |
| CIRCLE_CYCLE | H131-H150 | Sol, lua, ciclos | so, su, sa, yo, ya, yu, o, u |
| OPERATOR_TRIDENT | H151-H190 | Verbos, ações | ta, ti, tu, da, di, du, sa, si, su, ra, ri, ru |
| HUMAN_AGENT | H191-H230 | Pessoas, cargos | ma, mi, mu, na, ni, nu, ama, ani, anu |
| ANIMAL_NONFISH | H231-H260 | Animais totêmicos | ga, gi, gu, pa, pi, pu, ra, ri, ru, ka, ki, ku |
| PLANT_CROP | H261-H290 | Plantas, colheitas | sa, si, su, ya, yi, yu, ka, ki, ku |
| ABSTRACT_LIGATURE | H291-H320 | Conectores, partículas | a, i, u, e, o, ha, hi, hu, ya, yi, yu |
| RITUAL_STANDARD | H321-H360 | Estandartes rituais | tak, sak, ram, lam, kam, han, yum, kum |
| ARCH_BUILDING | H361-H390 | Arquitetura | ko, ku, kal, kul, kar, tor, dom, mur |
| MISC_RARE | H391-H417 | Nomes próprios, raros | a, ma, na, ra, ya, ta, sa, ka, la, pa, ga, ha |

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/ShantiDraconis/Universal-translation-0-0.git
cd Universal-translation-0-0

# Instale as dependências
pip install -e .

# Ou com dependências de desenvolvimento
pip install -e ".[dev,notebooks]"
```

## 💻 Uso

### CLI (Linha de Comando)

```bash
# Traduzir texto
universal-translate-00 translate "texto em qualquer idioma"

# Buscar signo Harappan
universal-translate-00 search H001

# Listar todos os signos de um grupo
universal-translate-00 list-group NUM

# Analisar fonema
universal-translate-00 analyze-phoneme ta
```

### Python API

```python
from universal_translation_00 import UniversalTranslator
from universal_translation_00.harappan import HarappanMapping

# Inicializar tradutor
translator = UniversalTranslator()

# Traduzir texto
result = translator.translate("água primordial")

# Buscar signo Harappan
harappan = HarappanMapping()
sign = harappan.get_sign("H001")
print(f"H001: {sign.phoneme} ({sign.group})")
```

### Web API

```bash
# Iniciar servidor
make run-web

# Ou diretamente
uvicorn universal_translation_00.web.app:app --reload
```

Acesse `http://localhost:8000` para a interface web.

## 📁 Estrutura do Projeto

```
universal-translation-0-0/
├── docs/                    # Documentação
│   ├── overview/           # Visão geral e arquitetura
│   ├── theory/             # Teoria linguística
│   ├── languages/          # Documentação por idioma
│   └── pipelines/          # Pipelines de tradução
├── data/                    # Dados
│   ├── raw/                # Dados brutos (CSV, TSV)
│   ├── processed/          # Dados processados (JSON)
│   └── examples/           # Exemplos de textos
├── src/                     # Código fonte
│   └── universal_translation_00/
│       ├── core/           # Tokenizer, normalizer
│       ├── dict00/         # Dicionário universal
│       ├── harappan/       # Mapeamento Harappan
│       ├── languages/      # Módulos por idioma
│       ├── translation/    # Pipeline de tradução
│       ├── cli/            # Interface de linha de comando
│       └── web/            # API web
├── proofs/                  # Provas formais
│   ├── lean/               # Lean 4
│   ├── coq/                # Coq
│   ├── isabelle/           # Isabelle/HOL
│   └── agda/               # Agda
├── tests/                   # Testes
├── notebooks/               # Jupyter notebooks
└── latex/                   # Documentação acadêmica
```

## 🧪 Testes

```bash
# Executar todos os testes
make test

# Ou com pytest diretamente
pytest tests/ -v
```

## 📚 Documentação

- [Visão 0/0](docs/overview/01-vision-0-0.md)
- [Arquitetura](docs/overview/02-architecture.md)
- [Universais Fonêmicos](docs/theory/10-phonemic-universals.md)
- [417 Signos Harappan](docs/theory/11-harappan-417-signs.md)

## 🔬 Provas Formais

O projeto inclui formalizações matemáticas em:

- **Lean 4**: Provas de consistência do sistema fonético
- **Coq**: Verificação de mapeamentos
- **Isabelle/HOL**: Teoria de tipos para linguística
- **Agda**: Provas construtivas

## 📖 Citação

Se você usar este software em sua pesquisa, por favor cite:

```bibtex
@software{universal_translation_00,
  author = {Draconis, Shanti},
  title = {Universal Translation 0/0 - Motor de Tradução Universal},
  year = {2025},
  url = {https://github.com/ShantiDraconis/Universal-translation-0-0}
}
```

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia nosso guia de contribuição antes de enviar PRs.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

Este projeto é inspirado em pesquisas de linguística comparativa, análise fonética universal, e estudos sobre o script do Vale do Indo. Agradecemos a todos os pesquisadores que contribuíram para o campo.

---

*"A linguagem primordial não é feita de palavras, mas de sons que ressoam através de todas as culturas."*
