# Os 417 Signos Harappan - Mapeamento Fonético

## Introdução

Este documento descreve o mapeamento completo dos 417 signos do script Harappan (Civilização do Vale do Indo) para fonemas baseados em análise linguística cruzada.

## Metodologia de Mapeamento

Cada signo foi mapeado seguindo critérios:

1. **Forma Visual** → Grupo semântico
2. **Grupo Semântico** → Conjunto de fonemas candidatos
3. **Análise Cross-Linguística** → Fonema específico
4. **Cognatos** → Validação em Tamil, Chinês, Nórdico, Latim, Tupi

## Grupos Semânticos

### NUM_TALLY (H001-H040)

**Descrição**: Marcas de contagem, números, valores numéricos

**Fonemas**: ta, ti, tu, na, ni, nu, sa, si, su, wa, ya, ri

**Justificativa**: 
- "ta/ti/tu" aparecem em raízes de tempo/contagem globalmente
- "na/ni" são marcadores de pessoa/quantidade
- "sa/si/su" indicam processo/fluxo

| ID | Fonema | Campo Semântico | Tamil | Chinês |
|----|--------|----------------|-------|--------|
| H001 | ta | contagem | taṭṭu | 打 |
| H002 | ti | tempo | tiṇṇam | 體 |
| H003 | tu | medida | tuṇṭu | 度 |
| ... | ... | ... | ... | ... |

### CONTAINER (H041-H080)

**Descrição**: Jarros, recipientes, volume, medida

**Fonemas**: ka, ko, ku, ga, go, gu, ma, mo, mu, pa, po, pu

**Justificativa**:
- "ka/ga" são raízes de objeto/lugar em dravídico
- "ma" indica matéria/substância
- "pa" indica parte/porção

| ID | Fonema | Campo Semântico | Tamil | Chinês |
|----|--------|----------------|-------|--------|
| H041 | ka | objeto | kaḷ | 器 |
| H042 | ko | oco | koṭi | 口 |
| H043 | ku | interior | kuri | 庫 |
| ... | ... | ... | ... | ... |

### GRID_FIELD (H081-H110)

**Descrição**: Campos, grades, matrizes, padrões tecidos

**Fonemas**: ra, ri, ru, la, li, lu, re, le, ro, we

**Justificativa**:
- "ra/ri/ru" indicam linha/fluxo/ordem
- "la/li/lu" indicam nível/plano
- "we" indica tecer/caminho

### CHEVRON_MOUNTAIN (H111-H130)

**Descrição**: Formas angulares, montanhas, picos

**Fonemas**: ka, ki, ku, ha, hi, hu, ta, ti, tu

**Justificativa**:
- "k" sons indicam elevação/pico
- "h" sons indicam sopro/espírito
- "t" sons indicam ação/esforço

### CIRCLE_CYCLE (H131-H150)

**Descrição**: Sol, lua, ciclos, totalidade

**Fonemas**: so, su, sa, yo, ya, yu, o, u

**Justificativa**:
- "so/su" relacionados a sol/água em múltiplas línguas
- "yo/ya" indicam união/jugo
- Vogais "o/u" são naturalmente circulares (boca)

### OPERATOR_TRIDENT (H151-H190)

**Descrição**: Verbos, ações, conexões, operações

**Fonemas**: ta, ti, tu, da, di, du, sa, si, su, ra, ri, ru

**Justificativa**:
- "t/d" são marcadores verbais universais
- "s" indica processo
- "r" indica relação/regra

### HUMAN_AGENT (H191-H230)

**Descrição**: Pessoas, cargos, clãs, família

**Fonemas**: ma, mi, mu, na, ni, nu, ama, ani, anu, ima, ina, inu

**Justificativa**:
- "ma/ama" = mãe (universal)
- "na/ni" = eu/pessoa
- Padrões CVV para termos de parentesco

### ANIMAL_NONFISH (H231-H260)

**Descrição**: Animais totêmicos, criaturas, partes de animais

**Fonemas**: ga, gi, gu, pa, pi, pu, ra, ri, ru, ka, ki, ku

**Justificativa**:
- "ga" = garra/presa
- "pa" = pai/força (relacionado a animais de poder)
- "ra" = rei (animais totêmicos)

### PLANT_CROP (H261-H290)

**Descrição**: Plantas, colheitas, vegetação, agricultura

**Fonemas**: sa, si, su, ya, yi, yu, ka, ki, ku

**Justificativa**:
- "sa" = semente/seiva
- "ya/yi" = crescimento/broto
- "ka" = campo/cultivo

### ABSTRACT_LIGATURE (H291-H320)

**Descrição**: Conectores abstratos, partículas gramaticais

**Fonemas**: a, i, u, e, o, ha, hi, hu, ya, yi, yu

**Justificativa**:
- Vogais puras como partículas
- "h" como aspiração/ênfase
- "y" como conexão

### RITUAL_STANDARD (H321-H360)

**Descrição**: Estandartes rituais, marcas cerimoniais

**Fonemas**: tak, sak, ram, lam, kam, han, yum, kum

**Justificativa**:
- Padrões CVC são comuns em termos rituais
- Aparecem em mantras sânscritos e fórmulas rituais

### ARCH_BUILDING (H361-H390)

**Descrição**: Arquitetura, edifícios, estruturas urbanas

**Fonemas**: ko, ku, kal, kul, kar, tor, dom, mur

**Justificativa**:
- "kal/kul" = pedra/templo (Tamil, Latim)
- "dom" = casa (Latin domus)
- "mur" = muro (Latin murus)
- "tor" = torre (Latin turris)

### MISC_RARE (H391-H417)

**Descrição**: Signos raros, nomes próprios, exceções

**Fonemas**: a, ma, na, ra, ya, ta, sa, ka, la, pa, ga, ha, o, i, u

**Justificativa**:
- Fonemas básicos para máxima flexibilidade
- Usados para nomes próprios e termos especializados

## Tabela Completa

A tabela completa está disponível em:
- `data/raw/harappan_417_signs.csv`
- `data/processed/harappan_sign_index.json`

## Uso Prático

```python
from universal_translation_00.harappan import HarappanMapping

mapping = HarappanMapping()

# Buscar signo por ID
sign = mapping.get_sign("H001")
print(f"{sign.id}: {sign.phoneme} ({sign.group})")

# Buscar signos por fonema
signs = mapping.phoneme_to_signs("ta")
print(f"Signos com 'ta': {len(signs)}")

# Listar grupo
num_signs = mapping.get_signs_by_group("NUM")
print(f"Grupo NUM: {len(num_signs)} signos")
```

## Referências

1. Parpola, A. (1994). Deciphering the Indus Script
2. Mahadevan, I. (1977). The Indus Script: Texts, Concordance and Tables
3. Wells, B. (2011). An Introduction to Indus Writing
4. Rao, R. et al. (2009). Entropic Evidence for Linguistic Structure in the Indus Script
