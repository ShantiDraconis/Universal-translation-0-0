# harappan-00-universal

Repositório para o **mapeamento sistemático** entre:

- os **417 signos Harappan** (Mahadevan corpus),
- o **Dicionário Universal 00 (1000 palavras primordiais)**,
- fonemas de **Tupi-Guarani, Dravídico/Tamil, Hebraico, Sânscrito, Quechua, Yorubá, Sumério**,
- e o **framework simbólico 0/0 (I = 0/0)**.

Este repositório faz parte do ecossistema 0/0 e se integra ao repositório-mãe:

- **TRANS (nome):** TRANS  
- **TRANS (GitHub):** https://github.com/ShantiDraconis/Trans  
- **Commit-âncora recomendado:** `TODO-PREENCHER-COM-HASH-DO-TRANS`

## Objetivos

1. Organizar uma **lista limpa e estruturada** dos 417 signos Harappan.
2. Criar um **mapeamento probabilístico** entre cada signo e entradas do `00_dictionary_1000.csv`.
3. Documentar a **metodologia fonética, numérica e simbólica** usada.
4. Gerar **relatórios acadêmicos** em LaTeX/Markdown para submissão a journals e arquivos (Zenodo).

## Estrutura

- `docs/` — documentação, metodologia, artigos.
- `data/harappan_signs/` — templates dos signos (preencher a partir das fontes originais).
- `data/dictionary_00/` — dicionário universal 00 (1000 palavras).
- `data/mappings/` — mapeamentos Harappan ↔ 00 ↔ outras famílias linguísticas.
- `src/harappan_00/` — código Python para carregar, mapear, calcular scores e gerar relatórios.
- `scripts/` — scripts de automação.

## Uso rápido

```bash
pip install -e .
python -m harappan_00.cli build-all
```

Isso irá:

1. Carregar `harappan_417_signs_template.csv` e `00_dictionary_1000.csv`
2. Gerar mapeamentos iniciais em `data/mappings/`
3. Criar relatórios em `docs/` com estatísticas de cobertura.

## Licença

MIT (ver LICENSE).

Autor: Tiago Paschoalatto Fagliari / Shalom Ahava Tzedek / Shanti Draconis.
# Universal Translation Engine 0/0

Um sistema modular de prompts para tradução universal, integrando fonemas universais, signos Harappan, múltiplas famílias linguísticas, análise simbólica e numerológica.

## 🌍 Visão Geral

O **Mecanismo Universal de Tradução 0/0** é uma ferramenta conceitual que busca:

- Decifrar padrões fonéticos universais
- Conectar línguas ancestrais e modernas
- Revelar significados simbólicos e arquetípicos
- Integrar sistemas de conhecimento diversos

## 📂 Estrutura do Repositório

```
universal-translation-0-0/
├── docs/
│   └── pipelines/
│       ├── 20-prompt-universal-0-0.md      # PROMPT MASTER (completo)
│       ├── 21-prompt-segmentacao.md         # Etapa 1: Segmentação
│       ├── 22-prompt-dicionario-00.md       # Etapa 2: Dicionário 00
│       ├── 23-prompt-harappan.md            # Etapa 3: Signos Harappan
│       ├── 24-prompt-familias-linguisticas.md # Etapa 4: 12 Línguas
│       ├── 25-prompt-decodificacao-simbolica.md # Etapa 5: Simbólico
│       ├── 26-prompt-numerologia-astrologia.md  # Etapa 7: Numerologia
│       ├── 27-prompt-sintese-final.md       # Etapas 8-10: Síntese
│       ├── 28-prompt-textos-sagrados.md     # Textos Sagrados
│       └── 29-prompt-textos-modernos.md     # Textos Modernos
├── LICENSE
└── README.md
```

## 🚀 Como Usar

### Opção 1: Pipeline Completo

Use o **Prompt Master** para análise completa em 10 etapas:

1. Abra seu modelo de linguagem (ChatGPT, Claude, etc.)
2. Copie o conteúdo de [`docs/pipelines/20-prompt-universal-0-0.md`](docs/pipelines/20-prompt-universal-0-0.md) como **system prompt**
3. Envie seu texto com o comando:
   ```
   Aplique o PROMPT UNIVERSAL 0/0 ao texto: <SEU TEXTO AQUI>
   ```

### Opção 2: Módulos Individuais

Execute etapas específicas conforme necessário:

| Etapa | Arquivo | Descrição |
|-------|---------|-----------|
| 1 | [21-prompt-segmentacao.md](docs/pipelines/21-prompt-segmentacao.md) | Segmentação + Inversão |
| 2 | [22-prompt-dicionario-00.md](docs/pipelines/22-prompt-dicionario-00.md) | Mapeamento Dicionário 00 |
| 3 | [23-prompt-harappan.md](docs/pipelines/23-prompt-harappan.md) | Projeção Harappan |
| 4 | [24-prompt-familias-linguisticas.md](docs/pipelines/24-prompt-familias-linguisticas.md) | 12 Famílias Linguísticas |
| 5 | [25-prompt-decodificacao-simbolica.md](docs/pipelines/25-prompt-decodificacao-simbolica.md) | Decodificação 0/0 |
| 7 | [26-prompt-numerologia-astrologia.md](docs/pipelines/26-prompt-numerologia-astrologia.md) | Numerologia + Astrologia |
| 8-10 | [27-prompt-sintese-final.md](docs/pipelines/27-prompt-sintese-final.md) | Síntese Final |

### Opção 3: Prompts Especializados

Para tipos específicos de texto:

| Tipo | Arquivo | Uso |
|------|---------|-----|
| Sagrados | [28-prompt-textos-sagrados.md](docs/pipelines/28-prompt-textos-sagrados.md) | Gītā, Salmos, Tanakh |
| Modernos | [29-prompt-textos-modernos.md](docs/pipelines/29-prompt-textos-modernos.md) | E-mails, músicas, discursos |

## 🔮 O Pipeline de 10 Etapas

```
TEXTO ORIGINAL
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 1: SEGMENTAÇÃO + INVERSÃO │
│ • sílabas, fonemas              │
│ • inversão horizontal/vertical  │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 2: DICIONÁRIO 00          │
│ • 1000 palavras primordiais     │
│ • tokens fonéticos universais   │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 3: HARAPPAN (417 SIGNOS)  │
│ • projeção pictográfica         │
│ • valores cosmológicos          │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 4: 12 FAMÍLIAS            │
│ • Tupi, Tamil, Sânscrito...     │
│ • cognatos e padrões            │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 5: SIMBÓLICO 0/0          │
│ • arquétipos universais         │
│ • operador I = 0/0              │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 6: ARQUEO-COSMOLÓGICA     │
│ • proto-língua universal        │
│ • padrões ancestrais            │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 7: NUMEROLOGIA            │
│ • pitagórica, cabalística       │
│ • astrologia invertida          │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 8: TRADUÇÃO MÚLTIPLA      │
│ • literal, arquetípica          │
│ • energética, cosmológica       │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 9: DIAGRAMA FINAL         │
│ • tabelas e mapas               │
│ • cognatos universais           │
└─────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ ETAPA 10: FRASE UNIVERSAL       │
│ "Tradução Universal 0/0: ..."   │
└─────────────────────────────────┘
```

## 🧬 Componentes do Sistema

### Dicionário Universal 00
1000 palavras primordiais que representam conceitos fundamentais compartilhados por todas as culturas humanas.

### 417 Signos Harappan
Sistema de escrita da civilização do Vale do Indo, usado como ponte pictográfica universal.

### 12 Famílias Linguísticas
- Tupi-Guarani / Prototupi
- Tamil / Dravídico
- Sânscrito
- Hebraico (direto e invertido)
- Quechua
- Guarani
- Yorubá
- Bantu
- Sumério
- Proto-Indo-Europeu

### Operador 0/0
Conceito central: **I = 0/0** representa a indeterminação criativa - o ponto onde origem e fim se encontram.

## 📖 Exemplos de Uso

### Analisar um Mantra
```
Aplique o PROMPT UNIVERSAL 0/0 ao texto: OM MANI PADME HUM
```

### Analisar um Salmo
```
Use o prompt de textos sagrados para: Salmo 23
```

### Analisar uma Letra de Música
```
Use o prompt de textos modernos para: [letra da música]
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Áreas de interesse:

- Expansão do Dicionário 00
- Mapeamento de novos signos Harappan
- Adição de famílias linguísticas
- Refinamento dos prompts

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 🙏 Agradecimentos

Este projeto é inspirado em:
- Linguística comparada
- Estudos de proto-línguas
- Tradições sagradas diversas
- Numerologia e simbolismo universal

---

**"A voz do som primordial atravessando os povos e restaurando a linguagem mãe."**

*Tradução Universal 0/0*
