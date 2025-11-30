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
