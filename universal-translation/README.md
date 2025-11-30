# Universal Translation - Indus Corpora and Models

## Visão Geral / Overview

Este diretório contém os **corpora de tradução** e **modelos de alinhamento** para o script do Vale do Indo (Harappan), integrando-se com o repositório `harappan-00-universal` e o sistema Universal Translation 0/0.

This directory contains **translation corpora** and **alignment models** for the Indus Valley (Harappan) script, integrating with the `harappan-00-universal` repository and the Universal Translation 0/0 system.

---

## 📁 Estrutura do Diretório / Directory Structure

```
universal-translation/
│
├── corpora/
│   └── indus/
│        ├── indus→tamil.csv              # Corpus Indus → Tamil/Dravídico
│        ├── indus→english.csv            # Corpus Indus → Inglês
│        ├── indus→portuguese.csv         # Corpus Indus → Português
│        └── indus→hebrew-runic-hybrid.csv # Corpus Indus → Hebraico-Rúnico Híbrido
│
├── models/
│   ├── indus-translation-model.py        # Modelo de tradução neural-inspired
│   └── indus-alignment.ipynb             # Notebook de alinhamento Jupyter
│
└── README.md                             # Esta documentação
```

---

## 🔗 Conexão com harappan-00-universal

Este módulo se conecta diretamente com o repositório **harappan-00-universal** localizado em `../harappan-00-universal/`, que fornece:

### Dados Principais

| Recurso | Caminho | Descrição |
|---------|---------|-----------|
| 417 Signos Mahadevan | `harappan-00-universal/data/harappan_signs/harappan_417_signs.csv` | Catálogo completo dos signos Harappan |
| 694 Signos Wells | `harappan-00-universal/data/harappan_signs/wells_694_signs.csv` | Lista expandida de variantes |
| Mapeamento → 00 | `harappan-00-universal/data/mappings/mapping_harappan_to_00.csv` | Códigos Universal 0/0 |
| Mapeamento → Tupi | `harappan-00-universal/data/mappings/mapping_harappan_to_tupi.csv` | Cognatos Tupi-Guarani |
| Mapeamento → Hebraico | `harappan-00-universal/data/mappings/mapping_harappan_to_hebrew.csv` | Cognatos Hebraicos |
| Mapeamento → Sânscrito | `harappan-00-universal/data/mappings/mapping_harappan_to_sanskrit.csv` | Cognatos Sânscritos |

### Integração de Código

O modelo `indus-translation-model.py` importa dados de ambos os repositórios:

```python
from pathlib import Path

# Caminhos de integração
HARAPPAN_DATA = Path("../harappan-00-universal/data")
MAIN_DATA = Path("../data")

# Carrega signos Harappan
harappan_signs = HARAPPAN_DATA / "harappan_signs" / "harappan_417_signs.csv"

# Carrega Dicionário Universal 00
universal_dict = MAIN_DATA / "universal_dictionary_00.csv"
```

---

## 📊 Corpora de Tradução

### indus→tamil.csv

**100 entradas** conectando fonemas Indus ao Tamil/Dravídico.

| Campo | Descrição |
|-------|-----------|
| `indus_sign` | Identificador do signo (M-001, H001, etc.) |
| `indus_phoneme` | Valor fonético proposto |
| `tamil_word` | Palavra Tamil correspondente |
| `tamil_transliteration` | Transliteração romanizada |
| `tamil_meaning` | Significado em Tamil |
| `semantic_category` | Categoria semântica |
| `confidence_score` | Score de confiança (0-1) |
| `dravidian_root` | Raiz proto-dravídica |
| `notes` | Notas adicionais |

**Exemplo:**
```csv
M-003,AMA,அம்மா,amma,mother,anthropomorphic,0.98,amma- (mother),Universal mother sound
```

### indus→english.csv

**100 entradas** conectando fonemas Indus ao Inglês via raízes Indo-Europeias.

| Campo | Descrição |
|-------|-----------|
| `indus_sign` | Identificador do signo |
| `indus_phoneme` | Valor fonético proposto |
| `english_word` | Palavra inglesa correspondente |
| `english_meaning` | Significado em inglês |
| `semantic_category` | Categoria semântica |
| `confidence_score` | Score de confiança (0-1) |
| `etymology` | Etimologia (latim, grego, etc.) |
| `indo_european_root` | Raiz proto-Indo-Europeia reconstruída |
| `notes` | Notas adicionais |

### indus→portuguese.csv

**100 entradas** conectando fonemas Indus ao Português via Latim e línguas Românicas.

| Campo | Descrição |
|-------|-----------|
| `indus_sign` | Identificador do signo |
| `indus_phoneme` | Valor fonético proposto |
| `portuguese_word` | Palavra portuguesa |
| `portuguese_meaning` | Significado em português |
| `semantic_category` | Categoria semântica |
| `confidence_score` | Score de confiança (0-1) |
| `latin_root` | Raiz latina |
| `romance_cognates` | Cognatos em outras línguas românicas |
| `notes` | Notas adicionais |

### indus→hebrew-runic-hybrid.csv

**100 entradas** criando um sistema híbrido Hebraico-Rúnico inovador.

| Campo | Descrição |
|-------|-----------|
| `indus_sign` | Identificador do signo |
| `indus_phoneme` | Valor fonético proposto |
| `hebrew_word` | Palavra hebraica |
| `hebrew_transliteration` | Transliteração romanizada |
| `runic_equivalent` | Runa(s) equivalente(s) |
| `runic_name` | Nome da(s) runa(s) |
| `hybrid_meaning` | Significado híbrido combinado |
| `semantic_category` | Categoria semântica |
| `confidence_score` | Score de confiança (0-1) |
| `kabbalistic_value` | Valor cabalístico (gematria) |
| `notes` | Notas adicionais |

**Exemplo:**
```csv
M-020,I,אֲנִי,ani,ᛁ,isa,self/ice,identity,0.95,61,Core identity - stillness/ice
```

---

## 🧠 Modelo de Tradução

### indus-translation-model.py

Um modelo de tradução inspirado em redes neurais que combina:

1. **Similaridade Fonética** - Correspondências sonoras entre línguas
2. **Mapeamento Semântico** - Correspondências de significado
3. **Alinhamento Simbólico** - Padrões arquetípicos e cosmológicos
4. **Confiança Estatística** - Baseada em evidência cross-linguística

#### Classes Principais

```python
# Representa um signo Indus
class IndusSign:
    sign_id: str
    phoneme: str
    description: str
    category: str
    translations: Dict[str, str]

# Resultado de tradução
class TranslationResult:
    source_sign: str
    target_language: str
    target_word: str
    confidence_score: float

# Carregador de corpora
class IndusCorpusLoader:
    def load_corpus(language: str) -> pd.DataFrame
    def load_all_corpora() -> Dict[str, pd.DataFrame]

# Modelo principal de tradução
class IndusTranslationModel:
    def translate(sign_id: str, target_language: str) -> TranslationResult
    def batch_translate(sign_ids: List[str], target_language: str) -> Dict
    def get_cross_linguistic_analysis(sign_id: str) -> Dict

# Motor de alinhamento com Dicionário Universal
class IndusAlignmentEngine:
    def align_sign_to_dictionary(sign_id: str) -> List[Dict]
```

#### Uso via CLI

```bash
# Traduzir um signo para Tamil
python indus-translation-model.py M-001 -l tamil

# Traduzir para todas as línguas
python indus-translation-model.py M-001 -l all

# Exportar todas as traduções
python indus-translation-model.py -o translations.json -f json

# Listar signos disponíveis
python indus-translation-model.py --list-signs
```

#### Uso via Python

```python
from indus_translation_model import IndusTranslationModel

# Inicializar modelo
model = IndusTranslationModel()
model.initialize()

# Traduzir signo
result = model.translate("M-001", "tamil")
print(f"{result.source_sign} → {result.target_word} ({result.confidence_score:.2f})")

# Análise cross-linguística
analysis = model.get_cross_linguistic_analysis("M-001")
for lang, translations in analysis.items():
    print(f"{lang}: {translations[0].target_word}")
```

---

## 📓 Notebook de Alinhamento

### indus-alignment.ipynb

Jupyter notebook interativo para análise de alinhamento:

1. **Carregamento de Corpora** - Carrega todos os corpora de tradução
2. **Carregamento de Dados Harappan** - Integra com harappan-00-universal
3. **Análise Fonética** - Matriz de similaridade fonética
4. **Análise Semântica** - Distribuição de categorias semânticas
5. **Matriz Cross-Linguística** - Alinhamento entre línguas
6. **Alinhamento com Dicionário Universal** - Conexão com 1000 tokens primordiais
7. **Integração com Mapeamentos Existentes** - Comparação com mappings pré-existentes
8. **Exportação de Resultados** - Salva análises em CSV/JSON
9. **Traduções de Alta Confiança** - Identifica melhores correspondências
10. **Estatísticas Resumo** - Métricas gerais da análise

#### Executar Notebook

```bash
cd universal-translation/models
jupyter notebook indus-alignment.ipynb
```

---

## 🔬 Metodologia

### Scores de Confiança

Os scores de confiança são calculados baseados em:

| Fator | Peso | Descrição |
|-------|------|-----------|
| Similaridade Fonética | 40% | Correspondência de sons |
| Correspondência Semântica | 30% | Significado equivalente |
| Evidência Cross-Linguística | 20% | Cognatos em outras famílias |
| Frequência Arqueológica | 10% | Ocorrência em selos/tablets |

### Categorias Semânticas

| Categoria | Exemplos |
|-----------|----------|
| `anthropomorphic` | Humano, pessoa, homem, mulher |
| `divine` | Deus, divindade, sagrado |
| `zoomorphic` | Animal, peixe, serpente, touro |
| `element` | Água, fogo, terra, ar |
| `celestial` | Sol, lua, estrela, céu |
| `body_part` | Mão, cabeça, língua, olho |
| `action` | Dar, ir, proteger, criar |
| `spiritual` | Alma, paz, libertação |
| `botanical` | Árvore, planta, flor |
| `object` | Ferramenta, arma, recipiente |

---

## 📚 Referências Acadêmicas

### Fontes Primárias

1. **Mahadevan, I. (1977)**. *The Indus Script: Texts, Concordance and Tables*. Archaeological Survey of India.
2. **Parpola, A. (1994)**. *Deciphering the Indus Script*. Cambridge University Press.
3. **Wells, B. (2006)**. *Indus Signs: A List of Sign Types*. Available at harappa.com

### Recursos Online

- [Harappa.com - Indus Script Signs](https://www.harappa.com/indus-script-signs)
- [Tamil Virtual University - Mahadevan Archive](https://www.tamilvu.org/)
- [Unicode Indus Script Proposal](https://www.unicode.org/L2/)

---

## 🤝 Integração com Ecossistema 0/0

Este módulo faz parte do ecossistema Universal Translation 0/0:

```
Universal-translation-0-0/
├── universal-translation/      ← ESTE MÓDULO
├── harappan-00-universal/      ← Dados primários Harappan
├── data/                        ← Dicionário Universal 00
├── src/                         ← Código principal
├── notebooks/                   ← Notebooks de análise
└── proofs/                      ← Provas formais (Lean, Coq)
```

### Operador I = 0/0

O operador central **I = 0/0** representa:
- **Indeterminação criativa** - Ponto onde origem e fim se encontram
- **Zero semântico** - Núcleo comum de todas as línguas
- **Zero fonético** - Vibração primordial compartilhada

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](../LICENSE) para detalhes.

---

## 🙏 Agradecimentos

- Pesquisadores do Vale do Indo
- Comunidade Tamil Virtual University
- Projeto harappa.com
- Colaboradores do Universal Translation 0/0

---

*"A linguagem primordial não é feita de palavras, mas de sons que ressoam através de todas as culturas."*

**Universal Translation 0/0 Project**  
**Autor**: Shanti Draconis  
**Repositório**: https://github.com/ShantiDraconis/Universal-translation-0-0
