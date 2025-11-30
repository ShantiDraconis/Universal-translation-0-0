"""
Dictionary 0/0 Search for Universal Translation 0/0.

Provides search functionality for the universal dictionary.
"""

from typing import Optional

from universal_translation_00.dict00.loader import Dict00Loader, DictEntry
from universal_translation_00.dict00.scoring import PhoneticScorer


class Dict00Search:
    """
    Search interface for Dictionary 0/0.

    Supports:
    - Exact phoneme search
    - Fuzzy phoneme search
    - Semantic search
    - Multi-criteria search
    """

    def __init__(self) -> None:
        """Initialize the search engine."""
        self.loader = Dict00Loader()
        self.scorer = PhoneticScorer()

    def search_by_phoneme(
        self, phoneme: str, max_results: int = 10
    ) -> list[dict]:
        """
        Search for entries matching a phoneme.

        Args:
            phoneme: The phoneme to search for
            max_results: Maximum number of results

        Returns:
            List of matching entry dictionaries
        """
        # Exact match first
        exact = self.loader.get_by_phoneme(phoneme)
        if exact:
            return [e.to_dict() for e in exact[:max_results]]

        # Fuzzy search
        all_entries = self.loader.get_all_entries()
        scored: list[tuple[float, DictEntry]] = []

        for entry in all_entries:
            score = self.scorer.phoneme_similarity(phoneme, entry.phoneme)
            if score > 0.5:  # Threshold
                scored.append((score, entry))

        # Sort by score descending
        scored.sort(key=lambda x: x[0], reverse=True)

        return [e.to_dict() for _, e in scored[:max_results]]

    def search_by_meaning(
        self, query: str, language: str = "en", max_results: int = 10
    ) -> list[dict]:
        """
        Search for entries by meaning.

        Args:
            query: Search query
            language: Language ('en' or 'pt')
            max_results: Maximum results

        Returns:
            List of matching entry dictionaries
        """
        query = query.lower()
        all_entries = self.loader.get_all_entries()
        matches: list[DictEntry] = []

        for entry in all_entries:
            meaning = entry.meaning_en if language == "en" else entry.meaning_pt
            if query in meaning.lower():
                matches.append(entry)

        return [e.to_dict() for e in matches[:max_results]]

    def search_by_semantic_class(
        self, semantic_class: str, max_results: int = 50
    ) -> list[dict]:
        """
        Search for entries by semantic class.

        Args:
            semantic_class: The semantic class (e.g., 'human', 'ritual')
            max_results: Maximum results

        Returns:
            List of matching entry dictionaries
        """
        entries = self.loader.get_by_class(semantic_class)
        return [e.to_dict() for e in entries[:max_results]]

    def find_similar(
        self, phoneme: str, max_results: int = 5
    ) -> list[tuple[str, float]]:
        """
        Find phonemes similar to the given one.

        Args:
            phoneme: The reference phoneme
            max_results: Maximum results

        Returns:
            List of (phoneme, similarity) tuples
        """
        all_phonemes = self.loader.get_all_phonemes()
        scored: list[tuple[str, float]] = []

        for other in all_phonemes:
            if other != phoneme:
                score = self.scorer.phoneme_similarity(phoneme, other)
                scored.append((other, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:max_results]

    def multi_search(
        self,
        phoneme: Optional[str] = None,
        meaning: Optional[str] = None,
        semantic_class: Optional[str] = None,
        max_results: int = 10,
    ) -> list[dict]:
        """
        Multi-criteria search.

        Args:
            phoneme: Optional phoneme filter
            meaning: Optional meaning filter
            semantic_class: Optional class filter
            max_results: Maximum results

        Returns:
            List of matching entry dictionaries
        """
        all_entries = self.loader.get_all_entries()
        matches: list[DictEntry] = []

        for entry in all_entries:
            # Check phoneme
            if phoneme and not self._phoneme_matches(phoneme, entry.phoneme):
                continue

            # Check meaning
            if meaning:
                meaning_lower = meaning.lower()
                if (meaning_lower not in entry.meaning_en.lower() and
                    meaning_lower not in entry.meaning_pt.lower()):
                    continue

            # Check semantic class
            if semantic_class and entry.semantic_class != semantic_class.lower():
                continue

            matches.append(entry)

        return [e.to_dict() for e in matches[:max_results]]

    def _phoneme_matches(self, query: str, target: str) -> bool:
        """Check if phoneme matches (exact or partial)."""
        query = query.lower()
        target = target.lower()
        return query == target or query in target or target in query
