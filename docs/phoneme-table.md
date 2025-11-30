# Phoneme Table - Universal Translation Engine 0/0

This document provides a reference table of universal phonemes used
in the Universal Translation Engine.

## IPA Consonant Chart

### Plosives

| | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|---|---|---|---|---|---|---|---|---|---|---|
| Voiceless | p | | | t | | ʈ | c | k | q | ʔ |
| Voiced | b | | | d | | ɖ | ɟ | g | ɢ | |
| Aspirated | pʰ | | | tʰ | | ʈʰ | | kʰ | | |

### Nasals

| | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Uvular |
|---|---|---|---|---|---|---|---|
| | m | ɱ | n | ɳ | ɲ | ŋ | ɴ |

### Fricatives

| | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|---|---|---|---|---|---|---|---|---|---|
| Voiceless | ɸ | f | θ | s | ʃ | ʂ | ç | x | h |
| Voiced | β | v | ð | z | ʒ | ʐ | ʝ | ɣ | ɦ |

### Approximants

| | Labiodental | Alveolar | Retroflex | Palatal | Labial-velar |
|---|---|---|---|---|---|
| | ʋ | ɹ | ɻ | j | w |

### Laterals

| | Alveolar | Retroflex | Palatal | Velar |
|---|---|---|---|---|
| Approximant | l | ɭ | ʎ | ʟ |

### Trills

| | Bilabial | Alveolar | Uvular |
|---|---|---|---|
| | ʙ | r | ʀ |

## IPA Vowel Chart

### Cardinal Vowels

|  | Front | Central | Back |
|---|---|---|---|
| Close | i / y | ɨ / ʉ | ɯ / u |
| Close-mid | e / ø | ɘ / ɵ | ɤ / o |
| Open-mid | ɛ / œ | ɜ / ɞ | ʌ / ɔ |
| Open | a / ɶ | ä | ɑ / ɒ |

### Diphthongs (Common)

| Symbol | Example (English) |
|---|---|
| aɪ | price |
| eɪ | face |
| ɔɪ | choice |
| aʊ | mouth |
| oʊ | goat |

## Language Family Phoneme Inventory

### Indo-European

**Common consonants:** p, b, t, d, k, g, m, n, s, l, r
**Aspirated series:** pʰ, bʰ, tʰ, dʰ, kʰ, gʰ (Indic)
**Retroflex series:** ʈ, ɖ, ɳ, ʂ (Indic)

### Dravidian

**Common consonants:** p, b, t, d, k, g, m, n, ŋ, l, r, ɻ
**Retroflex series:** ʈ, ɖ, ɳ, ɭ, ɻ
**Gemination:** Doubled consonants are phonemic

### Tupi-Guarani

**Common consonants:** p, t, k, m, n, ŋ, s, ɾ, w, j
**Nasal vowels:** ã, ẽ, ĩ, õ, ũ
**Glottal stop:** ʔ (common)

### Afro-Asiatic (Semitic)

**Common consonants:** p, b, t, d, k, g, m, n, s, z, l, r
**Pharyngeals:** ʕ, ħ
**Emphatics:** tˤ, dˤ, sˤ (Arabic)
**Triconsonantal roots:** Core feature

### Sino-Tibetan

**Common consonants:** p, b, t, d, k, g, m, n, ŋ, s, l
**Aspirated series:** pʰ, tʰ, kʰ
**Tones:** Phonemic in most languages
**Initial clusters:** Common in Tibetan

## Phoneme to Universal Code Mapping

Each phoneme is assigned a Universal Phoneme Code:

| Code | IPA | Category | Features |
|---|---|---|---|
| P001 | p | Consonant | Voiceless bilabial plosive |
| P002 | b | Consonant | Voiced bilabial plosive |
| P003 | t | Consonant | Voiceless alveolar plosive |
| P004 | d | Consonant | Voiced alveolar plosive |
| P005 | k | Consonant | Voiceless velar plosive |
| P006 | g | Consonant | Voiced velar plosive |
| P007 | m | Consonant | Voiced bilabial nasal |
| P008 | n | Consonant | Voiced alveolar nasal |
| P009 | ŋ | Consonant | Voiced velar nasal |
| P010 | f | Consonant | Voiceless labiodental fricative |
| P011 | v | Consonant | Voiced labiodental fricative |
| P012 | s | Consonant | Voiceless alveolar fricative |
| P013 | z | Consonant | Voiced alveolar fricative |
| P014 | ʃ | Consonant | Voiceless postalveolar fricative |
| P015 | h | Consonant | Voiceless glottal fricative |
| P016 | l | Consonant | Voiced alveolar lateral |
| P017 | r | Consonant | Voiced alveolar trill |
| P018 | j | Consonant | Voiced palatal approximant |
| P019 | w | Consonant | Voiced labial-velar approximant |
| V001 | a | Vowel | Open central |
| V002 | e | Vowel | Mid front |
| V003 | i | Vowel | Close front |
| V004 | o | Vowel | Mid back |
| V005 | u | Vowel | Close back |
| V006 | ə | Vowel | Mid central (schwa) |
| V007 | ã | Vowel | Nasal open central |

## X-SAMPA Equivalents

For ASCII-only environments:

| IPA | X-SAMPA | Description |
|---|---|---|
| ʃ | S | Voiceless postalveolar fricative |
| ʒ | Z | Voiced postalveolar fricative |
| θ | T | Voiceless dental fricative |
| ð | D | Voiced dental fricative |
| ŋ | N | Velar nasal |
| ɲ | J | Palatal nasal |
| ʔ | ? | Glottal stop |
| ɹ | r\ | Alveolar approximant |
| ə | @ | Schwa |
| ɛ | E | Open-mid front |
| ɔ | O | Open-mid back |
| æ | { | Near-open front |
| ɑ | A | Open back |
| ː | : | Long |
| ˈ | " | Primary stress |
| ˌ | % | Secondary stress |

## Phonetic Features

### Place of Articulation

| Feature | Description | Examples |
|---|---|---|
| Bilabial | Both lips | p, b, m |
| Labiodental | Lip + teeth | f, v |
| Dental | Tongue + teeth | θ, ð |
| Alveolar | Tongue + alveolar ridge | t, d, n, s, z, l |
| Postalveolar | Behind alveolar ridge | ʃ, ʒ |
| Retroflex | Curled tongue tip | ʈ, ɖ, ɳ |
| Palatal | Tongue + hard palate | c, ɟ, ɲ, j |
| Velar | Tongue + soft palate | k, g, ŋ |
| Glottal | Vocal folds | h, ʔ |

### Manner of Articulation

| Feature | Description | Examples |
|---|---|---|
| Plosive | Complete closure | p, t, k, b, d, g |
| Nasal | Nasal airflow | m, n, ŋ |
| Fricative | Turbulent airflow | f, s, ʃ, h |
| Approximant | Close but no friction | j, w, ɹ |
| Lateral | Air around sides | l |
| Trill | Vibration | r |
| Tap/Flap | Single contact | ɾ |

### Voicing

| Feature | Description | Examples |
|---|---|---|
| Voiceless | No vocal fold vibration | p, t, k, f, s |
| Voiced | Vocal fold vibration | b, d, g, v, z, m, n |

## Data Files

Full phoneme data available in:
- `universal_translation/datasets/universal/universal_phonemes.csv`
- `universal_translation/mappings/phoneme_map.json`
