"""
Indus Translation Model
=======================

A neural-inspired translation model for mapping Indus Valley (Harappan) script
to multiple target languages using phonetic, semantic, and symbolic correspondences.

This model integrates with the harappan-00-universal project and leverages the
Universal 0/0 translation framework to provide cross-linguistic mappings.

Part of the Universal Translation 0/0 Project
https://github.com/ShantiDraconis/Universal-translation-0-0
"""

import csv
import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd


@dataclass
class IndusSign:
    """Represents a single Indus Valley script sign."""
    
    sign_id: str
    phoneme: str
    description: str = ""
    category: str = ""
    frequency: str = "medium"
    confidence: float = 0.5
    translations: Dict[str, str] = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        """Convert sign to dictionary representation."""
        return {
            "sign_id": self.sign_id,
            "phoneme": self.phoneme,
            "description": self.description,
            "category": self.category,
            "frequency": self.frequency,
            "confidence": self.confidence,
            "translations": self.translations
        }


@dataclass
class TranslationResult:
    """Represents a translation result with confidence scores."""
    
    source_sign: str
    source_phoneme: str
    target_language: str
    target_word: str
    target_meaning: str
    confidence_score: float
    semantic_category: str
    notes: str = ""
    
    def __repr__(self) -> str:
        return f"TranslationResult({self.source_sign} → {self.target_language}: {self.target_word} [{self.confidence_score:.2f}])"


class IndusCorpusLoader:
    """Loads and manages the Indus translation corpora."""
    
    SUPPORTED_LANGUAGES = ["tamil", "english", "portuguese", "hebrew-runic-hybrid"]
    
    def __init__(self, corpora_path: Optional[Path] = None):
        """
        Initialize the corpus loader.
        
        Args:
            corpora_path: Path to the corpora directory. If None, uses default location.
        """
        if corpora_path is None:
            # Default to the corpora/indus directory relative to this file
            self.corpora_path = Path(__file__).parent.parent / "corpora" / "indus"
        else:
            self.corpora_path = Path(corpora_path)
        
        self._corpora: Dict[str, pd.DataFrame] = {}
        self._loaded = False
    
    def load_corpus(self, language: str) -> pd.DataFrame:
        """
        Load a specific language corpus.
        
        Args:
            language: Target language name (e.g., 'tamil', 'english')
            
        Returns:
            DataFrame containing the corpus data
        """
        if language not in self.SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {language}. Supported: {self.SUPPORTED_LANGUAGES}")
        
        if language in self._corpora:
            return self._corpora[language]
        
        # Construct filename with arrow character
        filename = f"indus→{language}.csv"
        filepath = self.corpora_path / filename
        
        if not filepath.exists():
            raise FileNotFoundError(f"Corpus file not found: {filepath}")
        
        df = pd.read_csv(filepath)
        self._corpora[language] = df
        return df
    
    def load_all_corpora(self) -> Dict[str, pd.DataFrame]:
        """Load all available corpora."""
        for lang in self.SUPPORTED_LANGUAGES:
            try:
                self.load_corpus(lang)
            except FileNotFoundError:
                print(f"Warning: Corpus not found for {lang}")
        self._loaded = True
        return self._corpora
    
    def get_available_languages(self) -> List[str]:
        """Get list of available languages with loaded corpora."""
        return list(self._corpora.keys())


class IndusTranslationModel:
    """
    Neural-inspired translation model for Indus Valley script.
    
    This model uses a multi-layer approach combining:
    1. Phonetic similarity (sound correspondences)
    2. Semantic mapping (meaning correspondences)
    3. Symbolic alignment (archetypal and cosmological patterns)
    4. Statistical confidence (based on cross-linguistic evidence)
    
    The model connects to the harappan-00-universal database for enhanced
    sign information and mappings.
    """
    
    def __init__(self, harappan_data_path: Optional[Path] = None):
        """
        Initialize the translation model.
        
        Args:
            harappan_data_path: Path to harappan-00-universal data directory
        """
        self.corpus_loader = IndusCorpusLoader()
        self.harappan_data_path = harappan_data_path
        self._signs_db: Dict[str, IndusSign] = {}
        self._initialized = False
        
        # Phonetic similarity weights for different language families
        self._phonetic_weights = {
            "tamil": 0.95,  # Dravidian - highest correlation with Indus
            "english": 0.75,  # Indo-European via Sanskrit cognates
            "portuguese": 0.70,  # Romance/IE with Tupi influence
            "hebrew-runic-hybrid": 0.85  # Semitic + Germanic fusion
        }
        
        # Semantic category weights
        self._category_weights = {
            "anthropomorphic": 0.90,
            "divine": 0.88,
            "zoomorphic": 0.92,
            "element": 0.85,
            "body_part": 0.80,
            "action": 0.75,
            "spiritual": 0.82,
            "celestial": 0.88,
            "object": 0.70,
            "botanical": 0.72
        }
    
    def initialize(self) -> None:
        """Initialize the model by loading all data sources."""
        # Load corpora
        self.corpus_loader.load_all_corpora()
        
        # Load harappan signs database if available
        if self.harappan_data_path:
            self._load_harappan_database()
        
        self._initialized = True
    
    def _load_harappan_database(self) -> None:
        """Load the harappan-00-universal signs database."""
        signs_path = self.harappan_data_path / "harappan_signs" / "harappan_417_signs.csv"
        if signs_path.exists():
            df = pd.read_csv(signs_path)
            for _, row in df.iterrows():
                sign = IndusSign(
                    sign_id=row.get("sign_id", ""),
                    phoneme=row.get("phonetic_value_proposed", ""),
                    description=row.get("description", ""),
                    category=row.get("category", ""),
                    frequency=row.get("frequency", "medium")
                )
                self._signs_db[sign.sign_id] = sign
    
    def translate(
        self,
        sign_id: str,
        target_language: str,
        include_alternatives: bool = False
    ) -> Union[TranslationResult, List[TranslationResult]]:
        """
        Translate an Indus sign to a target language.
        
        Args:
            sign_id: The Indus sign identifier (e.g., 'M-001', 'H001')
            target_language: Target language for translation
            include_alternatives: If True, return multiple possible translations
            
        Returns:
            TranslationResult or list of TranslationResults
        """
        if not self._initialized:
            self.initialize()
        
        # Normalize sign_id format
        normalized_id = self._normalize_sign_id(sign_id)
        
        # Get corpus for target language
        corpus = self.corpus_loader.load_corpus(target_language)
        
        # Find matching translations
        matches = corpus[corpus["indus_sign"] == normalized_id]
        
        if matches.empty:
            # Try phoneme-based lookup
            matches = self._phoneme_based_lookup(sign_id, corpus)
        
        results = self._create_translation_results(matches, target_language)
        
        if include_alternatives:
            return results
        return results[0] if results else None
    
    def _normalize_sign_id(self, sign_id: str) -> str:
        """Normalize sign ID to standard format."""
        sign_id = sign_id.upper().strip()
        # Convert H-style to M-style if needed
        if sign_id.startswith("H") and not sign_id.startswith("H-"):
            # Keep H format as is
            pass
        elif sign_id.startswith("M") and not sign_id.startswith("M-"):
            sign_id = f"M-{sign_id[1:].zfill(3)}"
        return sign_id
    
    def _phoneme_based_lookup(self, sign_id: str, corpus: pd.DataFrame) -> pd.DataFrame:
        """Look up translations based on phoneme similarity."""
        # Get phoneme from sign database
        if sign_id in self._signs_db:
            phoneme = self._signs_db[sign_id].phoneme
            return corpus[corpus["indus_phoneme"] == phoneme]
        return pd.DataFrame()
    
    def _create_translation_results(
        self,
        matches: pd.DataFrame,
        target_language: str
    ) -> List[TranslationResult]:
        """Create TranslationResult objects from matched rows."""
        results = []
        
        for _, row in matches.iterrows():
            # Determine target word column based on language
            word_col = self._get_word_column(target_language)
            meaning_col = self._get_meaning_column(target_language)
            
            result = TranslationResult(
                source_sign=row.get("indus_sign", ""),
                source_phoneme=row.get("indus_phoneme", ""),
                target_language=target_language,
                target_word=row.get(word_col, ""),
                target_meaning=row.get(meaning_col, row.get("semantic_category", "")),
                confidence_score=float(row.get("confidence_score", 0.5)),
                semantic_category=row.get("semantic_category", ""),
                notes=row.get("notes", "")
            )
            results.append(result)
        
        # Sort by confidence
        results.sort(key=lambda x: x.confidence_score, reverse=True)
        return results
    
    def _get_word_column(self, language: str) -> str:
        """Get the word column name for a language."""
        column_map = {
            "tamil": "tamil_word",
            "english": "english_word",
            "portuguese": "portuguese_word",
            "hebrew-runic-hybrid": "hebrew_word"
        }
        return column_map.get(language, f"{language}_word")
    
    def _get_meaning_column(self, language: str) -> str:
        """Get the meaning column name for a language."""
        column_map = {
            "tamil": "tamil_meaning",
            "english": "english_meaning",
            "portuguese": "portuguese_meaning",
            "hebrew-runic-hybrid": "hybrid_meaning"
        }
        return column_map.get(language, f"{language}_meaning")
    
    def batch_translate(
        self,
        sign_ids: List[str],
        target_language: str
    ) -> Dict[str, TranslationResult]:
        """
        Translate multiple signs at once.
        
        Args:
            sign_ids: List of sign identifiers
            target_language: Target language for translation
            
        Returns:
            Dictionary mapping sign_id to TranslationResult
        """
        results = {}
        for sign_id in sign_ids:
            result = self.translate(sign_id, target_language)
            if result:
                results[sign_id] = result
        return results
    
    def get_cross_linguistic_analysis(
        self,
        sign_id: str
    ) -> Dict[str, List[TranslationResult]]:
        """
        Get translations across all available languages.
        
        Args:
            sign_id: The Indus sign identifier
            
        Returns:
            Dictionary mapping language to list of translation results
        """
        results = {}
        for language in self.corpus_loader.SUPPORTED_LANGUAGES:
            try:
                translations = self.translate(sign_id, language, include_alternatives=True)
                if translations:
                    results[language] = translations
            except Exception as e:
                print(f"Warning: Could not translate to {language}: {e}")
        return results
    
    def calculate_phonetic_similarity(
        self,
        phoneme1: str,
        phoneme2: str
    ) -> float:
        """
        Calculate phonetic similarity between two phonemes.
        
        Uses a simplified Levenshtein-like distance normalized to [0, 1].
        
        Args:
            phoneme1: First phoneme string
            phoneme2: Second phoneme string
            
        Returns:
            Similarity score between 0 and 1
        """
        if phoneme1 == phoneme2:
            return 1.0
        
        # Simple character-based similarity
        max_len = max(len(phoneme1), len(phoneme2))
        if max_len == 0:
            return 0.0
        
        matches = sum(c1 == c2 for c1, c2 in zip(phoneme1.lower(), phoneme2.lower()))
        return matches / max_len
    
    def calculate_semantic_similarity(
        self,
        category1: str,
        category2: str
    ) -> float:
        """
        Calculate semantic similarity between categories.
        
        Args:
            category1: First semantic category
            category2: Second semantic category
            
        Returns:
            Similarity score between 0 and 1
        """
        if category1 == category2:
            return 1.0
        
        # Define category relationships
        related_categories = {
            ("divine", "spiritual"): 0.9,
            ("divine", "celestial"): 0.85,
            ("celestial", "element"): 0.7,
            ("anthropomorphic", "divine"): 0.6,
            ("zoomorphic", "divine"): 0.5,
            ("element", "botanical"): 0.6,
            ("action", "motion"): 0.95,
            ("body_part", "action"): 0.5
        }
        
        # Check both orderings
        pair1 = (category1.lower(), category2.lower())
        pair2 = (category2.lower(), category1.lower())
        
        if pair1 in related_categories:
            return related_categories[pair1]
        if pair2 in related_categories:
            return related_categories[pair2]
        
        return 0.3  # Default low similarity for unrelated categories
    
    def export_translations(
        self,
        output_path: Path,
        format: str = "json"
    ) -> None:
        """
        Export all translations to a file.
        
        Args:
            output_path: Path for output file
            format: Output format ('json' or 'csv')
        """
        if not self._initialized:
            self.initialize()
        
        all_translations = {}
        
        # Get all unique sign IDs from corpora
        all_signs = set()
        for df in self.corpus_loader._corpora.values():
            all_signs.update(df["indus_sign"].unique())
        
        for sign_id in all_signs:
            all_translations[sign_id] = {}
            for lang in self.corpus_loader.SUPPORTED_LANGUAGES:
                try:
                    result = self.translate(sign_id, lang)
                    if result:
                        all_translations[sign_id][lang] = {
                            "word": result.target_word,
                            "meaning": result.target_meaning,
                            "confidence": result.confidence_score
                        }
                except Exception:
                    pass
        
        if format == "json":
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(all_translations, f, indent=2, ensure_ascii=False)
        elif format == "csv":
            # Flatten for CSV export
            rows = []
            for sign_id, langs in all_translations.items():
                row = {"sign_id": sign_id}
                for lang, data in langs.items():
                    row[f"{lang}_word"] = data["word"]
                    row[f"{lang}_confidence"] = data["confidence"]
                rows.append(row)
            
            df = pd.DataFrame(rows)
            df.to_csv(output_path, index=False, encoding="utf-8")


class IndusAlignmentEngine:
    """
    Engine for aligning Indus signs with tokens from the Universal 0/0 Dictionary.
    
    Connects with harappan-00-universal for comprehensive sign-token alignment.
    """
    
    def __init__(self, dictionary_path: Optional[Path] = None):
        """
        Initialize the alignment engine.
        
        Args:
            dictionary_path: Path to universal_dictionary_00.csv
        """
        self.dictionary_path = dictionary_path
        self._dictionary: Optional[pd.DataFrame] = None
        self._model = IndusTranslationModel()
    
    def load_dictionary(self) -> pd.DataFrame:
        """Load the Universal 0/0 Dictionary."""
        if self._dictionary is not None:
            return self._dictionary
        
        if self.dictionary_path and self.dictionary_path.exists():
            self._dictionary = pd.read_csv(self.dictionary_path)
        else:
            # Try default location
            default_path = Path(__file__).parent.parent.parent / "data" / "universal_dictionary_00.csv"
            if default_path.exists():
                self._dictionary = pd.read_csv(default_path)
        
        return self._dictionary
    
    def align_sign_to_dictionary(
        self,
        sign_id: str,
        threshold: float = 0.6
    ) -> List[Dict]:
        """
        Find dictionary entries that align with an Indus sign.
        
        Args:
            sign_id: The Indus sign identifier
            threshold: Minimum alignment score (0-1)
            
        Returns:
            List of aligned dictionary entries with scores
        """
        dictionary = self.load_dictionary()
        if dictionary is None:
            return []
        
        alignments = []
        
        # Get cross-linguistic analysis
        translations = self._model.get_cross_linguistic_analysis(sign_id)
        
        for _, row in dictionary.iterrows():
            score = self._calculate_alignment_score(translations, row)
            if score >= threshold:
                alignments.append({
                    "token_id": row.get("token_id", ""),
                    "token": row.get("token", ""),
                    "semantic_core": row.get("semantic_core", ""),
                    "alignment_score": score,
                    "cosmological_category": row.get("cosmological_category", "")
                })
        
        # Sort by score
        alignments.sort(key=lambda x: x["alignment_score"], reverse=True)
        return alignments
    
    def _calculate_alignment_score(
        self,
        translations: Dict[str, List[TranslationResult]],
        dict_row: pd.Series
    ) -> float:
        """Calculate alignment score between translations and dictionary entry."""
        if not translations:
            return 0.0
        
        scores = []
        
        # Check Tamil cognate
        tamil_cognate = str(dict_row.get("tamil_cognate", "")).lower()
        if "tamil" in translations and tamil_cognate:
            for tr in translations["tamil"]:
                if tamil_cognate in tr.target_word.lower():
                    scores.append(tr.confidence_score * 1.2)  # Boost Tamil match
        
        # Check Sanskrit cognate
        sanskrit_cognate = str(dict_row.get("sanskrit_cognate", "")).lower()
        if sanskrit_cognate:
            for lang_results in translations.values():
                for tr in lang_results:
                    if sanskrit_cognate in tr.source_phoneme.lower():
                        scores.append(tr.confidence_score)
        
        # Semantic category alignment
        dict_category = str(dict_row.get("cosmological_category", "")).lower()
        for lang_results in translations.values():
            for tr in lang_results:
                if tr.semantic_category.lower() == dict_category:
                    scores.append(tr.confidence_score * 0.8)
        
        if not scores:
            return 0.0
        
        return min(1.0, np.mean(scores))


def main():
    """Main entry point for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Indus Translation Model - Translate Harappan script to multiple languages"
    )
    parser.add_argument(
        "sign_id",
        nargs="?",
        help="Indus sign identifier (e.g., M-001, H001)"
    )
    parser.add_argument(
        "-l", "--language",
        default="all",
        choices=["tamil", "english", "portuguese", "hebrew-runic-hybrid", "all"],
        help="Target language for translation"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path for batch export"
    )
    parser.add_argument(
        "-f", "--format",
        default="json",
        choices=["json", "csv"],
        help="Output format for batch export"
    )
    parser.add_argument(
        "--list-signs",
        action="store_true",
        help="List all available signs"
    )
    
    args = parser.parse_args()
    
    model = IndusTranslationModel()
    model.initialize()
    
    if args.list_signs:
        print("Available signs:")
        for sign_id in sorted(model._signs_db.keys()):
            sign = model._signs_db[sign_id]
            print(f"  {sign_id}: {sign.phoneme} ({sign.category})")
        return
    
    if args.output:
        print(f"Exporting translations to {args.output}...")
        model.export_translations(Path(args.output), args.format)
        print("Export complete!")
        return
    
    if not args.sign_id:
        parser.print_help()
        return
    
    if args.language == "all":
        print(f"\n{'='*60}")
        print(f"Cross-linguistic analysis for {args.sign_id}")
        print(f"{'='*60}\n")
        
        results = model.get_cross_linguistic_analysis(args.sign_id)
        for lang, translations in results.items():
            print(f"\n{lang.upper()}:")
            for tr in translations:
                print(f"  {tr.target_word} - {tr.target_meaning}")
                print(f"    Confidence: {tr.confidence_score:.2f}")
                print(f"    Category: {tr.semantic_category}")
    else:
        result = model.translate(args.sign_id, args.language)
        if result:
            print(f"\nTranslation of {args.sign_id} to {args.language}:")
            print(f"  Word: {result.target_word}")
            print(f"  Meaning: {result.target_meaning}")
            print(f"  Confidence: {result.confidence_score:.2f}")
            print(f"  Category: {result.semantic_category}")
        else:
            print(f"No translation found for {args.sign_id} in {args.language}")


if __name__ == "__main__":
    main()
