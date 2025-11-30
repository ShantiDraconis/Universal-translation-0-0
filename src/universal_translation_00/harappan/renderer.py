"""
Harappan Renderer for Universal Translation 0/0.

Renders Harappan signs in various output formats
including text, Unicode, and symbolic representations.
"""

from typing import Optional

from universal_translation_00.harappan.mapping import HarappanSign


class HarappanRenderer:
    """
    Renders Harappan signs and sequences in various formats.

    Supports:
    - Plain text (IDs)
    - Phonetic representation
    - Unicode approximations
    - Structured output
    """

    # Unicode approximations for semantic groups
    # These are placeholder symbols that visually suggest the sign category
    GROUP_SYMBOLS: dict[str, str] = {
        "NUM": "𐠀",  # Linear A sign (placeholder)
        "CON": "𐠁",
        "GRID": "𐠂",
        "CHEV": "𐠃",
        "CIRC": "𐠄",
        "OPER": "𐠅",
        "HUM": "𐠆",
        "ANIM": "𐠇",
        "PLANT": "𐠈",
        "ABSTR": "𐠉",
        "RIT": "𐠊",
        "ARCH": "𐠋",
        "MISC": "𐠌",
    }

    # Phoneme to IPA approximation
    IPA_MAP: dict[str, str] = {
        "a": "ɑ", "i": "i", "u": "u", "e": "e", "o": "o",
        "ka": "kɑ", "ki": "ki", "ku": "ku", "ko": "ko",
        "ga": "gɑ", "gi": "gi", "gu": "gu", "go": "go",
        "ta": "tɑ", "ti": "ti", "tu": "tu", "to": "to",
        "da": "dɑ", "di": "di", "du": "du", "do": "do",
        "na": "nɑ", "ni": "ni", "nu": "nu", "no": "no",
        "ma": "mɑ", "mi": "mi", "mu": "mu", "mo": "mo",
        "pa": "pɑ", "pi": "pi", "pu": "pu", "po": "po",
        "ra": "ɾɑ", "ri": "ɾi", "ru": "ɾu", "ro": "ɾo",
        "la": "lɑ", "li": "li", "lu": "lu", "lo": "lo",
        "sa": "sɑ", "si": "si", "su": "su", "so": "so",
        "ha": "hɑ", "hi": "hi", "hu": "hu", "ho": "ho",
        "ya": "jɑ", "yi": "ji", "yu": "ju", "yo": "jo",
        "wa": "wɑ", "wi": "wi", "wu": "wu", "wo": "wo",
    }

    def __init__(self, format_type: str = "text") -> None:
        """
        Initialize the renderer.

        Args:
            format_type: Output format ('text', 'phonetic', 'unicode', 'ipa')
        """
        self.format_type = format_type

    def render_sign(
        self, sign: HarappanSign, format_type: Optional[str] = None
    ) -> str:
        """
        Render a single Harappan sign.

        Args:
            sign: The Harappan sign to render
            format_type: Override default format

        Returns:
            Rendered string representation
        """
        fmt = format_type or self.format_type

        if fmt == "text":
            return sign.id
        elif fmt == "phonetic":
            return sign.phoneme
        elif fmt == "unicode":
            return self.GROUP_SYMBOLS.get(sign.group, "?")
        elif fmt == "ipa":
            return self.IPA_MAP.get(sign.phoneme, sign.phoneme)
        elif fmt == "full":
            return f"{sign.id}[{sign.phoneme}]"
        else:
            return sign.id

    def render_sequence(
        self,
        signs: list[HarappanSign],
        separator: str = " ",
        format_type: Optional[str] = None,
    ) -> str:
        """
        Render a sequence of Harappan signs.

        Args:
            signs: List of Harappan signs
            separator: Separator between signs
            format_type: Override default format

        Returns:
            Rendered string
        """
        rendered = [self.render_sign(s, format_type) for s in signs]
        return separator.join(rendered)

    def render_with_glosses(self, signs: list[HarappanSign]) -> str:
        """
        Render signs with semantic glosses.

        Args:
            signs: List of Harappan signs

        Returns:
            Multi-line rendering with glosses
        """
        lines: list[str] = []

        # Sign IDs
        ids = " ".join(s.id for s in signs)
        lines.append(f"Signs:    {ids}")

        # Phonemes
        phonemes = "-".join(s.phoneme for s in signs)
        lines.append(f"Phonetic: {phonemes}")

        # Groups
        groups = " ".join(s.group for s in signs)
        lines.append(f"Groups:   {groups}")

        return "\n".join(lines)

    def render_detailed(self, sign: HarappanSign) -> str:
        """
        Render detailed information about a sign.

        Args:
            sign: The Harappan sign

        Returns:
            Detailed multi-line representation
        """
        lines = [
            f"═══════════════════════════════════════",
            f" {sign.id} - {sign.group_full}",
            f"═══════════════════════════════════════",
            f" Phoneme:  {sign.phoneme}",
            f" IPA:      {self.IPA_MAP.get(sign.phoneme, sign.phoneme)}",
            f" Semantic: {sign.semantic_field}",
            f"───────────────────────────────────────",
            f" Cognates:",
            f"   Tamil:   {sign.tamil_root}",
            f"   Chinese: {sign.chinese_root}",
            f"   Norse:   {sign.norse_root}",
            f"   Latin:   {sign.latin_root}",
            f"   Tupi:    {sign.tupi_root}",
            f"───────────────────────────────────────",
            f" {sign.description}",
            f"═══════════════════════════════════════",
        ]
        return "\n".join(lines)

    def render_table(self, signs: list[HarappanSign]) -> str:
        """
        Render signs as a formatted table.

        Args:
            signs: List of Harappan signs

        Returns:
            Formatted table string
        """
        if not signs:
            return "No signs to display"

        # Header
        header = f"{'ID':<6} {'Group':<6} {'Phoneme':<8} {'Semantic Field':<30}"
        separator = "-" * len(header)

        lines = [header, separator]

        for sign in signs:
            line = f"{sign.id:<6} {sign.group:<6} {sign.phoneme:<8} {sign.semantic_field[:30]:<30}"
            lines.append(line)

        return "\n".join(lines)

    def to_json_structure(self, signs: list[HarappanSign]) -> list[dict]:
        """
        Convert signs to JSON-serializable structure.

        Args:
            signs: List of Harappan signs

        Returns:
            List of dictionaries
        """
        return [sign.to_dict() for sign in signs]
