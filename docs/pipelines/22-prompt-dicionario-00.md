# PROMPT — ETAPA 2: DICIONÁRIO 00 (1000 PALAVRAS)

---

```
Atue como o módulo DICIONÁRIO 00 do Mecanismo 0/0.

Entrada: uma lista de sílabas/fonemas já segmentados.

Para cada sílaba/fonema:
1. Busque no Dicionário Universal 00 (1000 palavras primordiais) os 3–4 tokens mais próximos.
2. Para cada candidato:
   - explique a proximidade fonética (som)
   - explique a proximidade simbólica (significado)
   - explique a proximidade energética (sensação / qualidade)

3. Entregue uma tabela com colunas:
   - Sílaba/Fonema
   - Candidato 1 (token_00) + gloss_pt + gloss_en
   - Candidato 2 …
   - Notas simbólicas
   - Sugestão do "melhor encaixe" 0/0 para aquela sílaba

Não faça Harappan, nem numerologia aqui. 
Aqui o objetivo é apenas: FONEMA → TOKENS 00 + EXPLICAÇÃO.
```

---

## Como Usar

1. Primeiro execute o prompt de [Segmentação (Etapa 1)](./21-prompt-segmentacao.md)
2. Copie a lista de sílabas/fonemas gerada
3. Use este prompt com a lista como entrada

## Formato de Entrada Esperado

```
Lista de sílabas: [a, ma, ni, pa, dme, hum]
```

## Formato de Saída Esperado

| Sílaba | Candidato 1 | Candidato 2 | Candidato 3 | Notas Simbólicas | Melhor Encaixe |
|--------|-------------|-------------|-------------|------------------|----------------|
| a      | A (origem/mãe) | AH (respiração) | AN (céu) | Som primordial | A (origem) |
| ma     | MA (mãe) | MU (água) | AMA (grande mãe) | Vibração maternal | MA (mãe) |
| ...    | ...         | ...         | ...         | ...              | ...            |

## Conceitos do Dicionário 00

O Dicionário Universal 00 contém 1000 palavras primordiais que representam:
- **Elementos básicos**: água, fogo, terra, ar, vazio
- **Relações familiares**: mãe, pai, irmão, filho
- **Ações primitivas**: ir, vir, dar, pegar
- **Estados**: ser, estar, viver, morrer
- **Cosmos**: sol, lua, estrela, céu, terra

## Próximo Passo

Após mapeamento ao Dicionário 00, use o prompt [23-prompt-harappan.md](./23-prompt-harappan.md) para projetar sobre os 417 signos Harappan.
