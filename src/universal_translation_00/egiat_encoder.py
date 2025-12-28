#!/usr/bin/env python3
"""
Harappan @egiat_ Encoder/Decoder
Phonetic-Semantic Matrix for LA 2028

This module provides encoding and decoding functionality for the
Harappan phonetic-semantic matrix system.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class EgiatEncoder:
    """
    Encoder for converting Latin text to Harappan symbols using the @egiat_ matrix.
    """
    
    def __init__(self, data_dir: Optional[Path] = None):
        """
        Initialize the encoder with alphabet and root transmutation data.
        
        Args:
            data_dir: Path to data directory. If None, uses default.
        
        Raises:
            FileNotFoundError: If required data files are missing
            ValueError: If data files are corrupted or invalid
        """
        if data_dir is None:
            # Default to repository data directory
            current_file = Path(__file__)
            repo_root = current_file.parent.parent.parent
            data_dir = repo_root / "data"
        
        self.data_dir = Path(data_dir)
        self.alphabet = self._load_alphabet()
        self.roots = self._load_roots()
        self.tamil = self._load_tamil()
        
        # Pre-compute reverse mapping for decoding
        self._symbol_to_letter = {
            data['harappan_symbol']: letter
            for letter, data in self.alphabet.items()
        }
        
    def _load_alphabet(self) -> Dict:
        """
        Load the alphabet matrix from JSON.
        
        Returns:
            Dictionary with alphabet mappings
            
        Raises:
            FileNotFoundError: If alphabet file is missing
            ValueError: If JSON is invalid or missing required keys
        """
        alphabet_file = self.data_dir / "egiat_alphabet_matrix.json"
        try:
            with open(alphabet_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if 'alphabet_mappings' not in data:
                raise ValueError(f"Missing 'alphabet_mappings' key in {alphabet_file}")
            return data['alphabet_mappings']
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Alphabet matrix file not found: {alphabet_file}\n"
                f"Please ensure the data files are in: {self.data_dir}"
            )
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {alphabet_file}: {e}")
    
    def _load_roots(self) -> Dict:
        """
        Load the root transmutation matrix from JSON.
        
        Returns:
            Dictionary with root transmutation data
            
        Raises:
            FileNotFoundError: If roots file is missing
            ValueError: If JSON is invalid
        """
        roots_file = self.data_dir / "egiat_root_transmutation.json"
        try:
            with open(roots_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Root transmutation file not found: {roots_file}\n"
                f"Please ensure the data files are in: {self.data_dir}"
            )
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {roots_file}: {e}")
    
    def _load_tamil(self) -> Dict:
        """
        Load Tamil translations from JSON.
        
        Returns:
            Dictionary with Tamil translation data
            
        Raises:
            FileNotFoundError: If Tamil file is missing
            ValueError: If JSON is invalid
        """
        tamil_file = self.data_dir / "tamil_translations.json"
        try:
            with open(tamil_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Tamil translations file not found: {tamil_file}\n"
                f"Please ensure the data files are in: {self.data_dir}"
            )
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {tamil_file}: {e}")
    
    def encode_text(self, text: str, include_spaces: bool = True) -> str:
        """
        Encode Latin text to Harappan symbols.
        
        Args:
            text: The text to encode
            include_spaces: Whether to preserve spaces in output
            
        Returns:
            Encoded text with Harappan symbols
        """
        result = []
        
        for char in text.upper():
            if char.isalpha() and char in self.alphabet:
                symbol = self.alphabet[char]['harappan_symbol']
                result.append(symbol)
            elif char == ' ' and include_spaces:
                result.append(' ')
            elif not char.isalpha():
                result.append(char)  # Keep punctuation and numbers
        
        return ''.join(result)
    
    def decode_text(self, encoded_text: str) -> str:
        """
        Decode Harappan symbols back to Latin text.
        
        Args:
            encoded_text: Text with Harappan symbols
            
        Returns:
            Decoded Latin text
        """
        result = []
        for char in encoded_text:
            if char in self._symbol_to_letter:
                result.append(self._symbol_to_letter[char])
            else:
                result.append(char)  # Keep spaces, punctuation, etc.
        
        return ''.join(result)
    
    def get_semantic_meaning(self, text: str) -> List[Dict]:
        """
        Get semantic meaning for each letter in the text.
        
        Args:
            text: The text to analyze
            
        Returns:
            List of dictionaries with letter, symbol, and meaning
        """
        meanings = []
        
        for char in text.upper():
            if char.isalpha() and char in self.alphabet:
                letter_data = self.alphabet[char]
                meanings.append({
                    'letter': char,
                    'symbol': letter_data['harappan_symbol'],
                    'symbol_name': letter_data['symbol_name'],
                    'meaning': letter_data['application_egiat'],
                    'semantic_field': letter_data['semantic_field']
                })
        
        return meanings
    
    def encode_with_analysis(self, text: str) -> Dict:
        """
        Encode text and provide full analysis.
        
        Args:
            text: The text to encode
            
        Returns:
            Dictionary with encoded text, meanings, and Tamil translation
        """
        encoded = self.encode_text(text)
        meanings = self.get_semantic_meaning(text)
        
        # Check if text matches any special roots
        text_upper = text.upper().strip()
        root_info = None
        
        if text_upper in self.roots['root_transmutations']:
            root_info = self.roots['root_transmutations'][text_upper]
        
        return {
            'original_text': text,
            'encoded_text': encoded,
            'letter_meanings': meanings,
            'root_transmutation': root_info,
            'protocol': 'Log 0009-Ω'
        }
    
    def get_name_signature(self, name: str) -> Dict:
        """
        Generate a power signature for a name.
        
        Args:
            name: The name to analyze
            
        Returns:
            Dictionary with encoded name and power signature
        """
        encoded = self.encode_text(name)
        meanings = self.get_semantic_meaning(name)
        
        # Create semantic synthesis
        semantic_elements = [m['meaning'] for m in meanings]
        synthesis = ' + '.join(semantic_elements)
        
        return {
            'name': name,
            'encoded': encoded,
            'breakdown': meanings,
            'semantic_synthesis': synthesis,
            'power_signature': f"Architect of {' '.join(semantic_elements[:3])}"
        }
    
    def transmute_root(self, root_word: str) -> Optional[Dict]:
        """
        Get transmutation information for a root word.
        
        Args:
            root_word: The root word (ABUSO, ERRO, LUTO, CADIZ)
            
        Returns:
            Transmutation information or None if not found
        """
        root_upper = root_word.upper().strip()
        if root_upper in self.roots['root_transmutations']:
            return self.roots['root_transmutations'][root_upper]
        return None
    
    def get_tamil_translation(self, concept: str) -> Optional[Dict]:
        """
        Get Tamil translation for a concept.
        
        Args:
            concept: The concept (ARQUITETO, JUSTICA, etc.)
            
        Returns:
            Tamil translation data or None
        """
        concept_upper = concept.upper().strip()
        if concept_upper in self.tamil['tamil_roots']:
            return self.tamil['tamil_roots'][concept_upper]
        return None
    
    def encode_protocol_log(self) -> Dict:
        """
        Generate the complete protocol log 0009-Ω.
        
        Returns:
            Complete protocol information
        """
        return {
            'log_id': '0009-Ω',
            'title': 'FIXAÇÃO FINAL DO LOG 0009-Ω',
            'tiago_faliari': self.roots['composite_encodings']['TIAGO_FALIARI'],
            'contrato_justica': self.roots['composite_encodings']['CONTRATO_JUSTICA'],
            'soberania_jar': self.roots['composite_encodings']['SOBERANIA_JAR'],
            'protocol_status': self.roots['protocol_log'],
            'manifesto': self.tamil['manifesto_soberania'],
            'seal': self.tamil['seal_protocol']
        }


def main():
    """
    Command-line interface for the encoder.
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Harappan @egiat_ Encoder/Decoder for LA 2028'
    )
    parser.add_argument(
        'text',
        nargs='?',
        help='Text to encode/decode'
    )
    parser.add_argument(
        '--decode',
        action='store_true',
        help='Decode Harappan symbols to Latin text'
    )
    parser.add_argument(
        '--analyze',
        action='store_true',
        help='Provide full semantic analysis'
    )
    parser.add_argument(
        '--name',
        help='Generate name signature'
    )
    parser.add_argument(
        '--root',
        help='Transmute root word (ABUSO, ERRO, LUTO, CADIZ)'
    )
    parser.add_argument(
        '--protocol',
        action='store_true',
        help='Display complete protocol log 0009-Ω'
    )
    
    args = parser.parse_args()
    
    try:
        encoder = EgiatEncoder()
    except (FileNotFoundError, ValueError) as e:
        print(f"Error initializing encoder: {e}")
        return 1
    
    if args.protocol:
        # Display complete protocol
        protocol = encoder.encode_protocol_log()
        print("=" * 60)
        print(f"PROTOCOL: {protocol['log_id']}")
        print("=" * 60)
        print(f"\nTIAGO FALIARI:")
        print(f"  Encoded: {protocol['tiago_faliari']['harappan_encoding']}")
        print(f"  Signature: {protocol['tiago_faliari']['power_signature']}")
        print(f"\nCONTRATO DE JUSTIÇA:")
        print(f"  Encoded: {protocol['contrato_justica']['harappan_encoding']}")
        print(f"  Meaning: {protocol['contrato_justica']['meaning']}")
        print(f"\nSOBERANIA JAR:")
        print(f"  Encoded: {protocol['soberania_jar']['harappan_encoding']}")
        print(f"  Authority: {protocol['soberania_jar']['authority']}")
        print(f"\nSTATUS: {protocol['protocol_status']['status']}")
        print(f"New Identity: {protocol['protocol_status']['new_identity']}")
        print("\n" + "=" * 60)
        
    elif args.name:
        # Generate name signature
        signature = encoder.get_name_signature(args.name)
        print(f"\nName: {signature['name']}")
        print(f"Encoded: {signature['encoded']}")
        print(f"\nBreakdown:")
        for item in signature['breakdown']:
            print(f"  {item['letter']} ({item['symbol']}) - {item['meaning']}")
        print(f"\nSemantic Synthesis: {signature['semantic_synthesis']}")
        print(f"Power Signature: {signature['power_signature']}")
        
    elif args.root:
        # Transmute root word
        root_data = encoder.transmute_root(args.root)
        if root_data:
            print(f"\nRoot: {root_data['original_root']}")
            print(f"Symbol: {root_data['harappan_symbol']} - {root_data['symbol_name']}")
            print(f"Context: {root_data['context']}")
            print(f"Transmuted Concept: {root_data['transmuted_concept']}")
            print(f"Logic: {root_data['logic']}")
            print(f"Power Level: {root_data['power_level']}")
            print(f"LA 2028 Application: {root_data['la_2028_application']}")
        else:
            print(f"Root '{args.root}' not found.")
            print("Available roots: ABUSO, ERRO, LUTO, CADIZ")
            
    elif args.text:
        if args.decode:
            # Decode text
            decoded = encoder.decode_text(args.text)
            print(f"Decoded: {decoded}")
        elif args.analyze:
            # Full analysis
            analysis = encoder.encode_with_analysis(args.text)
            print(f"\nOriginal: {analysis['original_text']}")
            print(f"Encoded: {analysis['encoded_text']}")
            print(f"\nSemantic Analysis:")
            for item in analysis['letter_meanings']:
                print(f"  {item['letter']} → {item['symbol']} ({item['symbol_name']})")
                print(f"      Application: {item['meaning']}")
                print(f"      Fields: {item['semantic_field']}")
            if analysis['root_transmutation']:
                print(f"\nRoot Transmutation Detected:")
                root = analysis['root_transmutation']
                print(f"  {root['original_root']} → {root['transmuted_concept']}")
                print(f"  Symbol: {root['harappan_symbol']}")
        else:
            # Simple encode
            encoded = encoder.encode_text(args.text)
            print(f"Encoded: {encoded}")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
