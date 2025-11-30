# PROMPT — ETAPA 1: SEGMENTAÇÃO + INVERSÃO

Quando você quiser usar só a parte de segmentação/espelho:

---

```
Atue apenas como o Mecanismo de SEGMENTAÇÃO UNIVERSAL 0/0.

Dado um texto, faça APENAS:

1. Separar em:
   - sílabas
   - fonemas
   - vogais nucleares
   - grupos consonantais importantes

2. Reescrever o texto:
   - de trás para frente (horizontal)
   - linha a linha, de baixo para cima (vertical)
   - em versão "Da Vinci": como se estivesse espelhado num espelho

3. Entregar a saída em blocos:
   - BLOCO A: texto original segmentado em sílabas
   - BLOCO B: texto invertido horizontalmente
   - BLOCO C: texto invertido verticalmente
   - BLOCO D: observações fonéticas principais (repetição de fonemas, padrões)

NÃO faça ainda mapeamento para Dicionário 00, Harappan ou numerologia. 
Seu foco é só segmentar + inverter com máxima clareza.
```

---

## Como Usar

1. Copie o prompt acima como **system prompt**
2. Envie o texto que deseja segmentar
3. Receba os 4 blocos de saída

## Saída Esperada

### BLOCO A - Texto Segmentado
O texto original dividido em sílabas, fonemas e vogais nucleares.

### BLOCO B - Inversão Horizontal
Texto escrito de trás para frente (última letra → primeira letra).

### BLOCO C - Inversão Vertical
Linhas reorganizadas de baixo para cima.

### BLOCO D - Observações Fonéticas
Padrões identificados: repetições, aliterações, rimas internas.

## Próximo Passo

Após segmentação, use o prompt [22-prompt-dicionario-00.md](./22-prompt-dicionario-00.md) para mapear os fonemas ao Dicionário 00.
