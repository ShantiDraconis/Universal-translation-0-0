"""
Reverse Writer for Universal Translation 0/0.

Implements various text reversal operations inspired by
mirror writing systems (Leonardo da Vinci, Hebrew, etc.).
"""


class ReverseWriter:
    """
    Implements text reversal operations for linguistic analysis.

    Supports:
    - Horizontal mirroring (right-to-left)
    - Vertical mirroring
    - Da Vinci style (mirror + reverse)
    - Boustrophedon (alternating directions)
    """

    # Mirror character mappings (visual mirrors)
    MIRROR_CHARS: dict[str, str] = {
        "a": "ɐ", "b": "d", "c": "ɔ", "d": "b", "e": "ǝ",
        "f": "ʇ", "g": "ƃ", "h": "ɥ", "i": "ı", "j": "ɾ",
        "k": "ʞ", "l": "l", "m": "ɯ", "n": "u", "o": "o",
        "p": "q", "q": "p", "r": "ɹ", "s": "s", "t": "ʇ",
        "u": "n", "v": "ʌ", "w": "ʍ", "x": "x", "y": "ʎ",
        "z": "z",
        # Numbers
        "1": "Ɩ", "2": "ς", "3": "Ɛ", "4": "ㄣ", "5": "ϛ",
        "6": "9", "7": "ㄥ", "8": "8", "9": "6", "0": "0",
    }

    def __init__(self) -> None:
        """Initialize the reverse writer."""
        # Create reverse mapping
        self._reverse_mirror = {v: k for k, v in self.MIRROR_CHARS.items()}

    def reverse_horizontal(self, text: str) -> str:
        """
        Reverse text horizontally (right-to-left).

        Args:
            text: The input text

        Returns:
            Horizontally reversed text
        """
        return text[::-1]

    def reverse_vertical(self, text: str) -> str:
        """
        Reverse text vertically (upside down).

        Uses visual mirror characters where available.

        Args:
            text: The input text

        Returns:
            Vertically reversed text
        """
        result: list[str] = []
        for char in text.lower():
            result.append(self.MIRROR_CHARS.get(char, char))
        return "".join(result)

    def mirror_davinci(self, text: str) -> str:
        """
        Apply Da Vinci style mirror writing.

        Combines horizontal reversal with vertical mirroring.

        Args:
            text: The input text

        Returns:
            Da Vinci style mirrored text
        """
        reversed_text = self.reverse_horizontal(text)
        return self.reverse_vertical(reversed_text)

    def boustrophedon(self, text: str, line_length: int = 40) -> str:
        """
        Apply boustrophedon writing (alternating direction).

        Args:
            text: The input text
            line_length: Characters per line

        Returns:
            Text with alternating line directions
        """
        lines: list[str] = []
        words = text.split()
        current_line: list[str] = []
        current_length = 0

        for word in words:
            if current_length + len(word) + 1 > line_length and current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word) + 1

        if current_line:
            lines.append(" ".join(current_line))

        # Reverse every other line
        result: list[str] = []
        for i, line in enumerate(lines):
            if i % 2 == 1:
                result.append(self.reverse_horizontal(line))
            else:
                result.append(line)

        return "\n".join(result)

    def reverse_words(self, text: str) -> str:
        """
        Reverse word order while keeping letters in order.

        Args:
            text: The input text

        Returns:
            Text with reversed word order
        """
        words = text.split()
        return " ".join(reversed(words))

    def reverse_each_word(self, text: str) -> str:
        """
        Reverse letters in each word while keeping word order.

        Args:
            text: The input text

        Returns:
            Text with each word's letters reversed
        """
        words = text.split()
        return " ".join(word[::-1] for word in words)

    def decode_mirror(self, text: str) -> str:
        """
        Decode mirrored text back to normal.

        Args:
            text: The mirrored text

        Returns:
            Decoded normal text
        """
        result: list[str] = []
        for char in text:
            result.append(self._reverse_mirror.get(char, char))
        return "".join(result)[::-1]
