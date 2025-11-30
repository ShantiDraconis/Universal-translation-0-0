"""
Pipeline Manager for Universal Translation 0/0.

Orchestrates the complete translation pipeline from
input text to Harappan phonetic representation.
"""

from dataclasses import dataclass, field
from typing import Optional

from universal_translation_00.core.tokenizer import Tokenizer, Token
from universal_translation_00.core.phoneme_segmenter import PhonemeSegmenter, Phoneme
from universal_translation_00.core.normalizer import Normalizer
from universal_translation_00.harappan.mapping import HarappanMapping, HarappanSign
from universal_translation_00.dict00.search import Dict00Search


@dataclass
class TranslationResult:
    """Result of a universal translation."""

    original_text: str
    normalized_text: str
    tokens: list[Token]
    phonemes: list[Phoneme]
    harappan_signs: list[HarappanSign]
    dict00_matches: list[dict]
    phonetic_reading: str
    harappan_sequence: str
    metadata: dict = field(default_factory=dict)

    def __repr__(self) -> str:
        return (
            f"TranslationResult(\n"
            f"  original={self.original_text!r},\n"
            f"  phonetic={self.phonetic_reading!r},\n"
            f"  harappan={self.harappan_sequence!r}\n"
            f")"
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "original_text": self.original_text,
            "normalized_text": self.normalized_text,
            "phonetic_reading": self.phonetic_reading,
            "harappan_sequence": self.harappan_sequence,
            "tokens": [{"text": t.text, "type": t.token_type, "script": t.script} for t in self.tokens],
            "phonemes": [{"value": p.value, "class": p.phoneme_class} for p in self.phonemes],
            "harappan_signs": [s.to_dict() for s in self.harappan_signs],
            "metadata": self.metadata,
        }


class UniversalTranslator:
    """
    Main translation engine for Universal Translation 0/0.

    Coordinates:
    1. Text tokenization
    2. Phoneme segmentation
    3. Dictionary lookup
    4. Harappan mapping
    """

    def __init__(
        self,
        normalize: bool = True,
        transliterate: bool = True,
        include_etymology: bool = True,
    ) -> None:
        """
        Initialize the translator.

        Args:
            normalize: Whether to normalize input text
            transliterate: Whether to transliterate non-Latin scripts
            include_etymology: Whether to include etymological information
        """
        self.tokenizer = Tokenizer(normalize_unicode=normalize)
        self.segmenter = PhonemeSegmenter()
        self.normalizer = Normalizer(
            lowercase=True,
            transliterate=transliterate,
        )
        self.harappan = HarappanMapping()
        self.dict00 = Dict00Search()
        self.include_etymology = include_etymology

    def translate(self, text: str) -> TranslationResult:
        """
        Perform complete translation of input text.

        Args:
            text: The input text in any supported language

        Returns:
            TranslationResult with all analysis layers
        """
        # Normalize text
        normalized = self.normalizer.normalize(text)

        # Tokenize
        tokens = self.tokenizer.tokenize(normalized)
        word_tokens = [t for t in tokens if t.token_type == "word"]

        # Segment into phonemes
        all_phonemes: list[Phoneme] = []
        for token in word_tokens:
            phonemes = self.segmenter.segment(token.text)
            all_phonemes.extend(phonemes)

        # Map phonemes to Harappan signs
        harappan_signs: list[HarappanSign] = []
        for phoneme in all_phonemes:
            sign = self.harappan.phoneme_to_sign(phoneme.value)
            if sign:
                harappan_signs.append(sign)

        # Search dictionary for matches
        dict00_matches: list[dict] = []
        for phoneme in all_phonemes:
            matches = self.dict00.search_by_phoneme(phoneme.value, max_results=3)
            if matches:
                dict00_matches.extend(matches)

        # Build phonetic reading
        phonetic_reading = "-".join(p.value for p in all_phonemes)

        # Build Harappan sequence
        harappan_sequence = " ".join(s.id for s in harappan_signs)

        # Build metadata
        metadata = {
            "word_count": len(word_tokens),
            "phoneme_count": len(all_phonemes),
            "harappan_sign_count": len(harappan_signs),
            "unique_phonemes": len(set(p.value for p in all_phonemes)),
        }

        if self.include_etymology:
            metadata["etymology"] = self._get_etymology(all_phonemes)

        return TranslationResult(
            original_text=text,
            normalized_text=normalized,
            tokens=tokens,
            phonemes=all_phonemes,
            harappan_signs=harappan_signs,
            dict00_matches=dict00_matches,
            phonetic_reading=phonetic_reading,
            harappan_sequence=harappan_sequence,
            metadata=metadata,
        )

    def _get_etymology(self, phonemes: list[Phoneme]) -> dict[str, str]:
        """Get etymological roots for phonemes."""
        etymology: dict[str, str] = {}
        from universal_translation_00.config import UNIVERSAL_ROOTS

        for phoneme in phonemes:
            if phoneme.value in UNIVERSAL_ROOTS:
                root_info = UNIVERSAL_ROOTS[phoneme.value]
                etymology[phoneme.value] = root_info["meaning"]

        return etymology

    def translate_to_phonemes(self, text: str) -> list[str]:
        """
        Quick translation to phoneme list only.

        Args:
            text: Input text

        Returns:
            List of phoneme strings
        """
        normalized = self.normalizer.normalize(text)
        tokens = self.tokenizer.tokenize_words_only(normalized)

        phonemes: list[str] = []
        for token in tokens:
            segs = self.segmenter.get_syllables(token.text)
            phonemes.extend(segs)

        return phonemes

    def translate_to_harappan(self, text: str) -> list[str]:
        """
        Quick translation to Harappan IDs only.

        Args:
            text: Input text

        Returns:
            List of Harappan sign IDs
        """
        phonemes = self.translate_to_phonemes(text)
        signs: list[str] = []

        for phoneme in phonemes:
            sign = self.harappan.phoneme_to_sign(phoneme)
            if sign:
                signs.append(sign.id)

        return signs
