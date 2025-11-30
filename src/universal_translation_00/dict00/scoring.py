"""
Phonetic Scoring for Universal Translation 0/0.

Provides similarity scoring between phonemes and entries.
"""


class PhoneticScorer:
    """
    Calculates phonetic similarity scores.

    Uses multiple metrics:
    - Levenshtein distance
    - Phonetic feature matching
    - Consonant/vowel patterns
    """

    # Phoneme classes for feature matching
    VOWELS = set("aeiouāēīōū")
    LABIALS = set("pbmw")
    DENTALS = set("tdnsz")
    VELARS = set("kgŋ")
    PALATALS = set("cjñyś")
    LIQUIDS = set("lr")
    FRICATIVES = set("sfhśṣ")

    # Similarity calculation weights
    LEVENSHTEIN_WEIGHT = 0.4
    FEATURE_WEIGHT = 0.3
    PATTERN_WEIGHT = 0.3

    def __init__(self) -> None:
        """Initialize the scorer."""
        pass

    def phoneme_similarity(self, p1: str, p2: str) -> float:
        """
        Calculate similarity between two phonemes.

        Args:
            p1: First phoneme
            p2: Second phoneme

        Returns:
            Similarity score (0.0 to 1.0)
        """
        if p1 == p2:
            return 1.0

        p1, p2 = p1.lower(), p2.lower()

        # Calculate different metrics
        levenshtein_sim = 1.0 - (self._levenshtein(p1, p2) / max(len(p1), len(p2), 1))
        feature_sim = self._feature_similarity(p1, p2)
        pattern_sim = self._pattern_similarity(p1, p2)

        # Weighted average
        return (self.LEVENSHTEIN_WEIGHT * levenshtein_sim + 
                self.FEATURE_WEIGHT * feature_sim + 
                self.PATTERN_WEIGHT * pattern_sim)

    def _levenshtein(self, s1: str, s2: str) -> int:
        """Calculate Levenshtein edit distance."""
        if len(s1) < len(s2):
            return self._levenshtein(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)

        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def _feature_similarity(self, p1: str, p2: str) -> float:
        """Calculate similarity based on phonetic features."""
        score = 0.0
        total = 0.0

        # Compare consonants
        c1 = [c for c in p1 if c not in self.VOWELS]
        c2 = [c for c in p2 if c not in self.VOWELS]

        if c1 and c2:
            total += 1
            if self._same_class(c1[0], c2[0]):
                score += 1
        elif not c1 and not c2:
            score += 0.5
            total += 1

        # Compare vowels
        v1 = [c for c in p1 if c in self.VOWELS]
        v2 = [c for c in p2 if c in self.VOWELS]

        if v1 and v2:
            total += 1
            if v1[0] == v2[0]:
                score += 1
            elif self._vowel_similar(v1[0], v2[0]):
                score += 0.5

        return score / total if total > 0 else 0.5

    def _same_class(self, c1: str, c2: str) -> bool:
        """Check if two consonants are in the same class."""
        for class_set in [self.LABIALS, self.DENTALS, self.VELARS,
                          self.PALATALS, self.LIQUIDS, self.FRICATIVES]:
            if c1 in class_set and c2 in class_set:
                return True
        return False

    def _vowel_similar(self, v1: str, v2: str) -> bool:
        """Check if two vowels are similar."""
        # Group similar vowels
        front = set("ieī")
        back = set("uoū")
        low = set("aā")

        for group in [front, back, low]:
            if v1 in group and v2 in group:
                return True
        return False

    def _pattern_similarity(self, p1: str, p2: str) -> float:
        """Calculate similarity based on CV pattern."""
        pattern1 = self._get_cv_pattern(p1)
        pattern2 = self._get_cv_pattern(p2)

        if pattern1 == pattern2:
            return 1.0

        # Calculate pattern overlap
        if len(pattern1) != len(pattern2):
            return 0.5

        matches = sum(1 for a, b in zip(pattern1, pattern2) if a == b)
        return matches / len(pattern1)

    def _get_cv_pattern(self, phoneme: str) -> str:
        """Get consonant-vowel pattern."""
        pattern = []
        for c in phoneme.lower():
            if c in self.VOWELS:
                pattern.append("V")
            elif c.isalpha():
                pattern.append("C")
        return "".join(pattern)

    def rank_candidates(
        self, target: str, candidates: list[str]
    ) -> list[tuple[str, float]]:
        """
        Rank candidates by similarity to target.

        Args:
            target: Target phoneme
            candidates: List of candidate phonemes

        Returns:
            List of (candidate, score) tuples, sorted by score
        """
        scored = [(c, self.phoneme_similarity(target, c)) for c in candidates]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored
