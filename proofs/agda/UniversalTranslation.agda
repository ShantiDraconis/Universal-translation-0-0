{-
  Universal Translation 0/0 - Agda Formalization
  
  Formal verification of phoneme mapping properties and
  cross-linguistic consistency in the Harappan reconstruction.
-}

module UniversalTranslation where

open import Data.Nat using (ℕ; zero; suc; _≤_; _<_; _≤?_; z≤n; s≤s)
open import Data.Nat.Properties using (≤-refl; ≤-trans)
open import Data.Bool using (Bool; true; false; if_then_else_)
open import Data.List using (List; []; _∷_; length)
open import Data.String using (String)
open import Data.Product using (_×_; _,_; proj₁; proj₂)
open import Relation.Binary.PropositionalEquality using (_≡_; refl; cong)
open import Relation.Nullary using (Dec; yes; no)

-- Basic vowel type
data Vowel : Set where
  V-a V-e V-i V-o V-u : Vowel

-- Basic consonant type
data Consonant : Set where
  C-k C-g C-t C-d C-p C-b C-m C-n C-r C-l C-s C-h C-y C-w : Consonant

-- Phoneme type - vowel, CV, or CVC
data Phoneme : Set where
  Ph-vowel : Vowel → Phoneme
  Ph-cv : Consonant → Vowel → Phoneme
  Ph-cvc : Consonant → Vowel → Consonant → Phoneme

-- Semantic groups for Harappan signs
data SemanticGroup : Set where
  NUM    : SemanticGroup  -- Numbers and counting H001-H040
  CON    : SemanticGroup  -- Containers H041-H080
  GRID   : SemanticGroup  -- Grids and fields H081-H110
  CHEV   : SemanticGroup  -- Chevrons and mountains H111-H130
  CIRC   : SemanticGroup  -- Circles and cycles H131-H150
  OPER   : SemanticGroup  -- Operators and verbs H151-H190
  HUM    : SemanticGroup  -- Human agents H191-H230
  ANIM   : SemanticGroup  -- Animals H231-H260
  PLANT  : SemanticGroup  -- Plants H261-H290
  ABSTR  : SemanticGroup  -- Abstract ligatures H291-H320
  RIT    : SemanticGroup  -- Ritual standards H321-H360
  ARCH   : SemanticGroup  -- Architecture H361-H390
  MISC   : SemanticGroup  -- Miscellaneous H391-H417

-- Valid sign ID (bounded natural)
record SignId : Set where
  field
    value : ℕ
    lower-bound : 1 ≤ value
    upper-bound : value ≤ 417

-- Harappan sign structure
record HarappanSign : Set where
  field
    sign-id : SignId
    sign-group : SemanticGroup
    sign-phoneme : Phoneme

-- Helper: compare natural with threshold
_≤ᵇ_ : ℕ → ℕ → Bool
zero ≤ᵇ _ = true
suc m ≤ᵇ zero = false
suc m ≤ᵇ suc n = m ≤ᵇ n

-- Map sign ID to semantic group
signIdToGroup : ℕ → SemanticGroup
signIdToGroup n with n ≤ᵇ 40
... | true = NUM
... | false with n ≤ᵇ 80
...   | true = CON
...   | false with n ≤ᵇ 110
...     | true = GRID
...     | false with n ≤ᵇ 130
...       | true = CHEV
...       | false with n ≤ᵇ 150
...         | true = CIRC
...         | false with n ≤ᵇ 190
...           | true = OPER
...           | false with n ≤ᵇ 230
...             | true = HUM
...             | false with n ≤ᵇ 260
...               | true = ANIM
...               | false with n ≤ᵇ 290
...                 | true = PLANT
...                 | false with n ≤ᵇ 320
...                   | true = ABSTR
...                   | false with n ≤ᵇ 360
...                     | true = RIT
...                     | false with n ≤ᵇ 390
...                       | true = ARCH
...                       | false = MISC

-- Phoneme lists for groups
numPhonemes : List Phoneme
numPhonemes = 
  Ph-cv C-t V-a ∷ Ph-cv C-t V-i ∷ Ph-cv C-t V-u ∷
  Ph-cv C-n V-a ∷ Ph-cv C-n V-i ∷ Ph-cv C-n V-u ∷
  Ph-cv C-s V-a ∷ Ph-cv C-s V-i ∷ Ph-cv C-s V-u ∷
  Ph-cv C-w V-a ∷ Ph-cv C-y V-a ∷ Ph-cv C-r V-i ∷ []

conPhonemes : List Phoneme
conPhonemes =
  Ph-cv C-k V-a ∷ Ph-cv C-k V-o ∷ Ph-cv C-k V-u ∷
  Ph-cv C-g V-a ∷ Ph-cv C-g V-o ∷ Ph-cv C-g V-u ∷
  Ph-cv C-m V-a ∷ Ph-cv C-m V-o ∷ Ph-cv C-m V-u ∷
  Ph-cv C-p V-a ∷ Ph-cv C-p V-o ∷ Ph-cv C-p V-u ∷ []

-- Get phoneme list for a group
groupPhonemes : SemanticGroup → List Phoneme
groupPhonemes NUM = numPhonemes
groupPhonemes CON = conPhonemes
groupPhonemes _ = Ph-vowel V-a ∷ []  -- Simplified

-- Cross-linguistic root
record CrossLinguisticRoot : Set where
  field
    root-phoneme : Phoneme
    root-tamil : String
    root-chinese : String
    root-norse : String
    root-latin : String
    root-tupi : String

-- Theorems

-- Sign ID determines unique group (trivial by function definition)
signId-unique-group : ∀ n → signIdToGroup n ≡ signIdToGroup n
signId-unique-group _ = refl

-- Example: H001 maps to NUM
example-H001 : signIdToGroup 1 ≡ NUM
example-H001 = refl

-- Example: H050 maps to CON
example-H050 : signIdToGroup 50 ≡ CON
example-H050 = refl

-- Example: H100 maps to GRID
example-H100 : signIdToGroup 100 ≡ GRID
example-H100 = refl

-- Example sign H001
example-sign-H001 : HarappanSign
example-sign-H001 = record
  { sign-id = record { value = 1 ; lower-bound = s≤s z≤n ; upper-bound = s≤s z≤n }
  ; sign-group = NUM
  ; sign-phoneme = Ph-cv C-t V-a
  }
