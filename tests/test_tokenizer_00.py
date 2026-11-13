"""Tests for the tokenizer module."""

import pytest

from universal_translation_00.core.tokenizer import Tokenizer, Token


class TestTokenizer:
    """Test suite for Tokenizer class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.tokenizer = Tokenizer()

    def test_tokenize_simple_text(self) -> None:
        """Test tokenization of simple Latin text."""
        text = "hello world"
        tokens = self.tokenizer.tokenize(text)

        assert len(tokens) == 3  # hello, space, world
        assert tokens[0].text == "hello"
        assert tokens[0].token_type == "word"
        assert tokens[0].script == "latin"

    def test_tokenize_with_punctuation(self) -> None:
        """Test tokenization with punctuation."""
        text = "hello, world!"
        tokens = self.tokenizer.tokenize(text)

        word_tokens = [t for t in tokens if t.token_type == "word"]
        punct_tokens = [t for t in tokens if t.token_type == "punctuation"]

        assert len(word_tokens) == 2
        assert len(punct_tokens) == 2

    def test_tokenize_numbers(self) -> None:
        """Test tokenization of numbers."""
        text = "test 123 abc"
        tokens = self.tokenizer.tokenize(text)

        number_tokens = [t for t in tokens if t.token_type == "number"]
        assert len(number_tokens) == 1
        assert number_tokens[0].text == "123"

    def test_detect_script_latin(self) -> None:
        """Test Latin script detection."""
        assert self.tokenizer.detect_script("hello") == "latin"
        assert self.tokenizer.detect_script("école") == "latin"

    def test_detect_script_tamil(self) -> None:
        """Test Tamil script detection."""
        assert self.tokenizer.detect_script("தமிழ்") == "tamil"

    def test_detect_script_devanagari(self) -> None:
        """Test Devanagari script detection."""
        assert self.tokenizer.detect_script("नमस्ते") == "devanagari"

    def test_detect_script_chinese(self) -> None:
        """Test Chinese script detection."""
        assert self.tokenizer.detect_script("中文") == "chinese"

    def test_tokenize_words_only(self) -> None:
        """Test getting only word tokens."""
        text = "hello, world! 123"
        tokens = self.tokenizer.tokenize_words_only(text)

        assert len(tokens) == 2
        assert all(t.token_type == "word" for t in tokens)

    def test_get_words(self) -> None:
        """Test getting word strings."""
        text = "hello world test"
        words = self.tokenizer.get_words(text)

        assert words == ["hello", "world", "test"]

    def test_empty_text(self) -> None:
        """Test tokenization of empty text."""
        tokens = self.tokenizer.tokenize("")
        assert tokens == []

    def test_unicode_normalization(self) -> None:
        """Test that Unicode is normalized."""
        # Combining character vs precomposed
        tokenizer_norm = Tokenizer(normalize_unicode=True)
        tokens = tokenizer_norm.tokenize("café")
        assert len(tokens) == 1


class TestToken:
    """Test suite for Token dataclass."""

    def test_token_creation(self) -> None:
        """Test Token creation."""
        token = Token(
            text="hello",
            position=0,
            length=5,
            token_type="word",
            script="latin",
        )

        assert token.text == "hello"
        assert token.position == 0
        assert token.length == 5
        assert token.token_type == "word"
        assert token.script == "latin"

    def test_token_repr(self) -> None:
        """Test Token string representation."""
        token = Token(
            text="test",
            position=0,
            length=4,
            token_type="word",
            script="latin",
        )

        repr_str = repr(token)
        assert "test" in repr_str
        assert "word" in repr_str
        assert "latin" in repr_str
