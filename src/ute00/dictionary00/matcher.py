"""
Root Matcher for UTE-0/0.

Matches words to primordial roots using phonetic similarity.
"""

from dataclasses import dataclass
from typing import List, Tuple

from ute00.dictionary00.roots import UniversalRoot, UniversalRoots


@dataclass
class RootMatch:
    """Result of matching a word to primordial roots."""

    word: str
    root: UniversalRoot
    similarity_score: float
    match_type: str  # phonetic, symbolic, cosmological


class RootMatcher:
    """
    Matches words to primordial roots.

    Uses three types of similarity:
    - Phonetic similarity
    - Symbolic similarity
    - Cosmological similarity
    """

    def __init__(self):
        """Initialize the root matcher."""
        self.roots = UniversalRoots()

    def match_word(self, word: str, top_n: int = 5) -> List[RootMatch]:
        """
        Find matching primordial roots for a word.

        Args:
            word: Word to match
            top_n: Number of top matches to return

        Returns:
            List of RootMatch results, sorted by similarity
        """
        matches = []

        for root in self.roots.ROOTS.values():
            # Calculate phonetic similarity
            phonetic_score = self._calculate_phonetic_similarity(word, root.root)
            if phonetic_score > 0:
                matches.append(
                    RootMatch(
                        word=word,
                        root=root,
                        similarity_score=phonetic_score,
                        match_type="phonetic",
                    )
                )

        # Sort by similarity score descending
        matches.sort(key=lambda m: m.similarity_score, reverse=True)
        return matches[:top_n]

    def _calculate_phonetic_similarity(self, word: str, root: str) -> float:
        """
        Calculate phonetic similarity between word and root.

        Uses a simple character overlap algorithm.

        Args:
            word: Word to compare
            root: Root to compare against

        Returns:
            Similarity score between 0 and 1
        """
        word = word.lower()
        # Remove asterisk from proto-form roots
        root = root.lstrip("*").lower()

        if not word or not root:
            return 0.0

        # Count matching characters
        word_chars = set(word)
        root_chars = set(root)
        common = word_chars & root_chars

        # Calculate Jaccard-like similarity
        union = word_chars | root_chars
        if not union:
            return 0.0

        similarity = len(common) / len(union)

        # Bonus for prefix match
        min_len = min(len(word), len(root))
        prefix_match = 0
        for i in range(min_len):
            if word[i] == root[i]:
                prefix_match += 1
            else:
                break

        prefix_bonus = prefix_match / max(len(word), len(root)) * 0.3

        return min(1.0, similarity + prefix_bonus)

    def find_by_meaning(self, meaning: str) -> UniversalRoot | None:
        """
        Find a root by its meaning.

        Args:
            meaning: Meaning to search

        Returns:
            UniversalRoot if found
        """
        return self.roots.get_root_by_meaning(meaning)

    def get_related_roots(self, root: UniversalRoot) -> List[UniversalRoot]:
        """
        Get roots related by semantic field.

        Args:
            root: Reference root

        Returns:
            List of related roots
        """
        return self.roots.get_roots_by_field(root.semantic_field)

    def analyze_etymology(self, word: str) -> List[Tuple[str, UniversalRoot]]:
        """
        Analyze possible etymological connections.

        Args:
            word: Word to analyze

        Returns:
            List of (language, root) tuples showing possible origins
        """
        matches = self.match_word(word, top_n=3)
        results = []

        for match in matches:
            for lang in match.root.related_languages:
                results.append((lang, match.root))

        return results
