# PROMPT — ETAPA 3: HARAPPAN (417 SIGNOS)

---

```
Atue como o módulo HARAPPAN 00 (417 signos).

Entrada: sílabas/fonemas e, se possível, os tokens 00 já sugeridos.

Para cada sílaba:
1. Associe ao signo Harappan mais provável (ou a 2–3 candidatos).
2. Para cada signo, informe:
   - ID ou nome do signo (quando houver convenção)
   - valor numérico (seu sistema simbólico pro Harappan)
   - valor geométrico (forma básica, ex: linha, espiral, cruz, etc.)
   - valor cosmológico (terra, água, fogo, ar, vazio, mãe, etc.)
   - possível significado proto-sumério ou proto-dravídico

3. Entregue:
   - uma tabela Sílabas → Signos Harappan
   - um mini-mapa: quais signos se repetem mais e o que isso sugere.

Não faça tradução de línguas modernas aqui; foco = Harappan + cosmologia.
```

---

## Como Usar

1. Execute primeiro:
   - [Etapa 1 - Segmentação](./21-prompt-segmentacao.md)
   - [Etapa 2 - Dicionário 00](./22-prompt-dicionario-00.md)
2. Use este prompt com as sílabas e tokens 00 como entrada

## Formato de Entrada Esperado

```
Sílabas com tokens 00:
- a → A (origem)
- ma → MA (mãe)
- ni → NI (ser)
- pa → PA (pai/protetor)
```

## Formato de Saída Esperado

### Tabela Sílabas → Signos Harappan

| Sílaba | Token 00 | Signo Harappan | ID | Valor Numérico | Valor Geométrico | Valor Cosmológico | Proto-Sumério |
|--------|----------|----------------|-----|----------------|------------------|-------------------|---------------|
| a      | A        | ☉ (sol)        | H1  | 1              | círculo          | origem            | AN (céu)      |
| ma     | MA       | 𐨀 (mãe)       | H47 | 7              | curva            | água/terra        | AMA           |
| ...    | ...      | ...            | ... | ...            | ...              | ...               | ...           |

### Mini-Mapa de Signos Recorrentes

```
Signo H47 (mãe): 3 ocorrências → tema maternal dominante
Signo H1 (sol): 2 ocorrências → conexão com luz/origem
```

## Sobre os 417 Signos Harappan

Os signos da civilização do Vale do Indo (Harappan) são um sistema de escrita ainda não totalmente decifrado, datando de ~2600-1900 a.C. O sistema 0/0 propõe correspondências:

- **Geométricas**: formas básicas (círculo, linha, espiral, cruz)
- **Cosmológicas**: elementos e forças (água, fogo, mãe, pai)
- **Numéricas**: valores de 1 a 417
- **Fonéticas**: sons reconstruídos baseados em línguas dravídicas

## Próximo Passo

Após mapeamento Harappan, use o prompt [24-prompt-familias-linguisticas.md](./24-prompt-familias-linguisticas.md) para tradução nas 12 famílias linguísticas.
