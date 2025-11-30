"""
Tokenizer for Universal Translation 0/0.

Splits input text into tokens for phonetic analysis.
Handles multiple writing systems and Unicode normalization.
"""

import re
import unicodedata
from dataclasses import dataclass


@dataclass
class Token:
    """Represents a single token in the input text."""

    text: str
    position: int
    length: int
    token_type: str  # 'word', 'number', 'punctuation', 'whitespace'
    script: str  # 'latin', 'devanagari', 'tamil', 'chinese', etc.

    def __repr__(self) -> str:
        return f"Token({self.text!r}, type={self.token_type}, script={self.script})"


class Tokenizer:
    """
    Universal tokenizer that handles multiple writing systems.

    Splits text into tokens while preserving script information
    for accurate phonetic analysis.
    """

    # Script detection patterns
    SCRIPT_PATTERNS: dict[str, re.Pattern[str]] = {
        "latin": re.compile(r"[\u0041-\u007A\u00C0-\u024F]+"),
        "devanagari": re.compile(r"[\u0900-\u097F]+"),
        "tamil": re.compile(r"[\u0B80-\u0BFF]+"),
        "chinese": re.compile(r"[\u4E00-\u9FFF]+"),
        "hebrew": re.compile(r"[\u0590-\u05FF]+"),
        "arabic": re.compile(r"[\u0600-\u06FF]+"),
        "cyrillic": re.compile(r"[\u0400-\u04FF]+"),
        "greek": re.compile(r"[\u0370-\u03FF]+"),
        "runic": re.compile(r"[\u16A0-\u16FF]+"),
    }

    # Token type patterns
    WORD_PATTERN = re.compile(r"\w+", re.UNICODE)
    NUMBER_PATTERN = re.compile(r"\d+")
    PUNCTUATION_PATTERN = re.compile(r"[^\w\s]+", re.UNICODE)
    WHITESPACE_PATTERN = re.compile(r"\s+")

    def __init__(self, normalize_unicode: bool = True) -> None:
        """
        Initialize the tokenizer.

        Args:
            normalize_unicode: Whether to apply Unicode NFC normalization
        """
        self.normalize_unicode = normalize_unicode

    def detect_script(self, text: str) -> str:
        """
        Detect the primary script of a text segment.

        Args:
            text: The text to analyze

        Returns:
            Script name (e.g., 'latin', 'tamil', 'chinese')
        """
        for script_name, pattern in self.SCRIPT_PATTERNS.items():
            if pattern.search(text):
                return script_name
        return "unknown"

    def tokenize(self, text: str) -> list[Token]:
        """
        Tokenize input text into a list of tokens.

        Args:
            text: The input text to tokenize

        Returns:
            List of Token objects
        """
        if self.normalize_unicode:
            text = unicodedata.normalize("NFC", text)

        tokens: list[Token] = []
        position = 0

        while position < len(text):
            # Try to match each token type
            remaining = text[position:]

            # Check whitespace first
            ws_match = self.WHITESPACE_PATTERN.match(remaining)
            if ws_match:
                tokens.append(
                    Token(
                        text=ws_match.group(),
                        position=position,
                        length=len(ws_match.group()),
                        token_type="whitespace",
                        script="none",
                    )
                )
                position += len(ws_match.group())
                continue

            # Check numbers
            num_match = self.NUMBER_PATTERN.match(remaining)
            if num_match:
                tokens.append(
                    Token(
                        text=num_match.group(),
                        position=position,
                        length=len(num_match.group()),
                        token_type="number",
                        script="numeric",
                    )
                )
                position += len(num_match.group())
                continue

            # Check words (includes Unicode word characters)
            word_match = self.WORD_PATTERN.match(remaining)
            if word_match:
                word = word_match.group()
                script = self.detect_script(word)
                tokens.append(
                    Token(
                        text=word,
                        position=position,
                        length=len(word),
                        token_type="word",
                        script=script,
                    )
                )
                position += len(word)
                continue

            # Check punctuation
            punct_match = self.PUNCTUATION_PATTERN.match(remaining)
            if punct_match:
                tokens.append(
                    Token(
                        text=punct_match.group(),
                        position=position,
                        length=len(punct_match.group()),
                        token_type="punctuation",
                        script="none",
                    )
                )
                position += len(punct_match.group())
                continue

            # Single character fallback
            tokens.append(
                Token(
                    text=remaining[0],
                    position=position,
                    length=1,
                    token_type="unknown",
                    script=self.detect_script(remaining[0]),
                )
            )
            position += 1

        return tokens

    def tokenize_words_only(self, text: str) -> list[Token]:
        """
        Tokenize and return only word tokens.

        Args:
            text: The input text

        Returns:
            List of word Token objects
        """
        return [t for t in self.tokenize(text) if t.token_type == "word"]

    def get_words(self, text: str) -> list[str]:
        """
        Get just the word strings from text.

        Args:
            text: The input text

        Returns:
            List of word strings
        """
        return [t.text for t in self.tokenize_words_only(text)]
