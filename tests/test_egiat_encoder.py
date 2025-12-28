"""
Unit tests for Harappan @egiat_ Encoder/Decoder
"""

import unittest
import json
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from universal_translation_00.egiat_encoder import EgiatEncoder


class TestEgiatEncoder(unittest.TestCase):
    """Test suite for EgiatEncoder class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up encoder instance for all tests"""
        cls.encoder = EgiatEncoder()
    
    def test_encoder_initialization(self):
        """Test that encoder initializes correctly"""
        self.assertIsNotNone(self.encoder.alphabet)
        self.assertIsNotNone(self.encoder.roots)
        self.assertIsNotNone(self.encoder.tamil)
        self.assertEqual(len(self.encoder.alphabet), 26)
    
    def test_encode_single_letter(self):
        """Test encoding single letters"""
        self.assertEqual(self.encoder.encode_text('A'), '𓂝')
        self.assertEqual(self.encoder.encode_text('T'), '𓏙')
        self.assertEqual(self.encoder.encode_text('S'), '𓋹')
    
    def test_encode_word(self):
        """Test encoding complete words"""
        encoded = self.encoder.encode_text('HELLO')
        self.assertIsNotNone(encoded)
        self.assertGreater(len(encoded), 0)
    
    def test_encode_preserves_spaces(self):
        """Test that spaces are preserved in encoding"""
        encoded = self.encoder.encode_text('LA 2028', include_spaces=True)
        self.assertIn(' ', encoded)
    
    def test_encode_decode_roundtrip(self):
        """Test that encoding and decoding are inverses"""
        test_texts = ['HELLO', 'WORLD', 'ACTION', 'LA 2028']
        
        for text in test_texts:
            encoded = self.encoder.encode_text(text)
            decoded = self.encoder.decode_text(encoded)
            self.assertEqual(text, decoded, f"Failed roundtrip for '{text}'")
    
    def test_encode_mixed_case(self):
        """Test that mixed case is handled (converted to uppercase)"""
        encoded_upper = self.encoder.encode_text('HELLO')
        encoded_mixed = self.encoder.encode_text('HeLLo')
        self.assertEqual(encoded_upper, encoded_mixed)
    
    def test_get_semantic_meaning(self):
        """Test semantic meaning extraction"""
        meanings = self.encoder.get_semantic_meaning('ACTION')
        
        self.assertEqual(len(meanings), 6)  # A, C, T, I, O, N
        self.assertEqual(meanings[0]['letter'], 'A')
        self.assertEqual(meanings[0]['symbol'], '𓂝')
        self.assertIn('meaning', meanings[0])
        self.assertIn('semantic_field', meanings[0])
    
    def test_encode_with_analysis(self):
        """Test full analysis encoding"""
        analysis = self.encoder.encode_with_analysis('TIAGO')
        
        self.assertEqual(analysis['original_text'], 'TIAGO')
        self.assertIn('encoded_text', analysis)
        self.assertIn('letter_meanings', analysis)
        self.assertEqual(len(analysis['letter_meanings']), 5)
        self.assertEqual(analysis['protocol'], 'Log 0009-Ω')
    
    def test_get_name_signature(self):
        """Test name signature generation"""
        signature = self.encoder.get_name_signature('TIAGO FALIARI')
        
        self.assertEqual(signature['name'], 'TIAGO FALIARI')
        self.assertIn('encoded', signature)
        self.assertIn('breakdown', signature)
        self.assertIn('semantic_synthesis', signature)
        self.assertIn('power_signature', signature)
        self.assertGreater(len(signature['breakdown']), 0)
    
    def test_root_transmutation_abuso(self):
        """Test ABUSO root transmutation"""
        root = self.encoder.transmute_root('ABUSO')
        
        self.assertIsNotNone(root)
        self.assertEqual(root['original_root'], 'ABUSO')
        self.assertEqual(root['harappan_symbol'], '𓀜')
        self.assertEqual(root['symbol_name'], 'O Inimigo Caído')
        self.assertEqual(root['power_level'], 'transformative')
    
    def test_root_transmutation_erro(self):
        """Test ERRO root transmutation"""
        root = self.encoder.transmute_root('ERRO')
        
        self.assertIsNotNone(root)
        self.assertEqual(root['original_root'], 'ERRO')
        self.assertEqual(root['harappan_symbol'], '𓏣')
        self.assertEqual(root['symbol_name'], 'O Ajuste Fino')
        self.assertEqual(root['power_level'], 'resilience')
    
    def test_root_transmutation_luto(self):
        """Test LUTO root transmutation"""
        root = self.encoder.transmute_root('LUTO')
        
        self.assertIsNotNone(root)
        self.assertEqual(root['original_root'], 'LUTO')
        self.assertEqual(root['harappan_symbol'], '𓇳')
        self.assertEqual(root['symbol_name'], 'O Sol Eterno')
        self.assertEqual(root['power_level'], 'transcendent')
        self.assertIn('operator_connection', root)
    
    def test_root_transmutation_cadiz(self):
        """Test CÁDIZ root transmutation"""
        root = self.encoder.transmute_root('CADIZ')
        
        self.assertIsNotNone(root)
        self.assertEqual(root['original_root'], 'CÁDIZ')
        self.assertEqual(root['harappan_symbol'], '𓊝')
        self.assertEqual(root['symbol_name'], 'A Travessia do Deserto')
        self.assertEqual(root['power_level'], 'foundational')
        self.assertEqual(root['date'], '2024-11-14')
    
    def test_root_transmutation_invalid(self):
        """Test invalid root returns None"""
        root = self.encoder.transmute_root('INVALID')
        self.assertIsNone(root)
    
    def test_all_roots_exist(self):
        """Test that all documented roots exist"""
        roots = ['ABUSO', 'ERRO', 'LUTO', 'CADIZ']
        
        for root_name in roots:
            root = self.encoder.transmute_root(root_name)
            self.assertIsNotNone(root, f"Root {root_name} not found")
            self.assertIn('transmuted_concept', root)
            self.assertIn('la_2028_application', root)
    
    def test_tamil_translation_arquiteto(self):
        """Test Tamil translation for ARQUITETO"""
        tamil = self.encoder.get_tamil_translation('ARQUITETO')
        
        self.assertIsNotNone(tamil)
        self.assertEqual(tamil['tamil'], 'சிற்பி')
        self.assertEqual(tamil['transliteration'], 'Sirpi')
    
    def test_tamil_translation_justica(self):
        """Test Tamil translation for JUSTICA"""
        tamil = self.encoder.get_tamil_translation('JUSTICA')
        
        self.assertIsNotNone(tamil)
        self.assertEqual(tamil['tamil'], 'நீதி')
        self.assertEqual(tamil['transliteration'], 'Neethi')
    
    def test_tamil_translation_soberania(self):
        """Test Tamil translation for SOBERANIA"""
        tamil = self.encoder.get_tamil_translation('SOBERANIA')
        
        self.assertIsNotNone(tamil)
        self.assertEqual(tamil['tamil'], 'இறையாண்மை')
        self.assertEqual(tamil['transliteration'], 'Iraiyanmai')
    
    def test_protocol_log_structure(self):
        """Test protocol log structure"""
        protocol = self.encoder.encode_protocol_log()
        
        self.assertEqual(protocol['log_id'], '0009-Ω')
        self.assertIn('tiago_faliari', protocol)
        self.assertIn('contrato_justica', protocol)
        self.assertIn('soberania_jar', protocol)
        self.assertIn('protocol_status', protocol)
    
    def test_protocol_log_tiago_faliari(self):
        """Test TIAGO FALIARI encoding in protocol"""
        protocol = self.encoder.encode_protocol_log()
        tiago = protocol['tiago_faliari']
        
        self.assertEqual(tiago['full_name'], 'TIAGO FALIARI')
        self.assertEqual(tiago['harappan_encoding'], '𓏙𓏲𓂝𓊹𓊖 𓄜𓂝𓊛𓏲𓂝𓇯𓏲')
        self.assertIn('breakdown', tiago)
        # Breakdown has one entry per unique letter (T, I, A, G, O, F, L, R = 8 unique)
        self.assertEqual(len(tiago['breakdown']), 8)
    
    def test_protocol_log_contrato_justica(self):
        """Test CONTRATO JUSTICA encoding in protocol"""
        protocol = self.encoder.encode_protocol_log()
        contrato = protocol['contrato_justica']
        
        self.assertEqual(contrato['phrase'], 'CONTRATO DE JUSTIÇA')
        self.assertEqual(contrato['harappan_encoding'], '𓍢 0/0 𓏞 𓍝')
        self.assertEqual(contrato['meaning'], 'Justice Contract Sealed at Zero Point')
    
    def test_protocol_log_status(self):
        """Test protocol log status"""
        protocol = self.encoder.encode_protocol_log()
        status = protocol['protocol_status']
        
        self.assertEqual(status['status'], 'COMPLETED')
        self.assertTrue(status['transformation_complete'])
        self.assertEqual(status['old_identity'], 'Tiago (Subordinado)')
        self.assertEqual(status['new_identity'], '@egiat_ (Arquiteto Soberano)')
    
    def test_alphabet_completeness(self):
        """Test that all 26 letters are mapped"""
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        for letter in alphabet:
            self.assertIn(letter, self.encoder.alphabet, f"Letter {letter} missing")
            letter_data = self.encoder.alphabet[letter]
            self.assertIn('harappan_symbol', letter_data)
            self.assertIn('meaning_harappan', letter_data)
            self.assertIn('application_egiat', letter_data)
    
    def test_alphabet_symbols_unique(self):
        """Test that Harappan symbols are unique per letter"""
        symbols = [data['harappan_symbol'] for data in self.encoder.alphabet.values()]
        self.assertEqual(len(symbols), len(set(symbols)), "Duplicate symbols found")
    
    def test_encode_numbers_preserved(self):
        """Test that numbers are preserved in encoding"""
        encoded = self.encoder.encode_text('LA 2028')
        self.assertIn('2028', encoded)
    
    def test_encode_punctuation_preserved(self):
        """Test that punctuation is preserved"""
        encoded = self.encoder.encode_text('HELLO!')
        self.assertIn('!', encoded)
    
    def test_semantic_fields_present(self):
        """Test that all letters have semantic fields"""
        for letter, data in self.encoder.alphabet.items():
            self.assertIn('semantic_field', data, f"Letter {letter} missing semantic_field")
            self.assertIsInstance(data['semantic_field'], str)
    
    def test_phonetic_values_present(self):
        """Test that all letters have phonetic values"""
        for letter, data in self.encoder.alphabet.items():
            self.assertIn('phonetic_value', data, f"Letter {letter} missing phonetic_value")
            self.assertIsInstance(data['phonetic_value'], str)
    
    def test_data_files_exist(self):
        """Test that all required data files exist"""
        data_dir = self.encoder.data_dir
        
        required_files = [
            'egiat_alphabet_matrix.json',
            'egiat_root_transmutation.json',
            'tamil_translations.json'
        ]
        
        for filename in required_files:
            filepath = data_dir / filename
            self.assertTrue(filepath.exists(), f"Missing data file: {filename}")
    
    def test_json_structure_alphabet(self):
        """Test alphabet JSON structure"""
        alphabet_file = self.encoder.data_dir / 'egiat_alphabet_matrix.json'
        with open(alphabet_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.assertIn('metadata', data)
        self.assertIn('alphabet_mappings', data)
        self.assertEqual(data['metadata']['version'], '1.0.0')
    
    def test_json_structure_roots(self):
        """Test roots JSON structure"""
        roots_file = self.encoder.data_dir / 'egiat_root_transmutation.json'
        with open(roots_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.assertIn('metadata', data)
        self.assertIn('root_transmutations', data)
        self.assertIn('composite_encodings', data)
        self.assertIn('protocol_log', data)
    
    def test_composite_encodings_exist(self):
        """Test that composite encodings exist"""
        composites = ['TIAGO_FALIARI', 'CONTRATO_JUSTICA', 'SOBERANIA_JAR']
        
        for composite in composites:
            self.assertIn(composite, self.encoder.roots['composite_encodings'])


class TestEgiatEncoderEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""
    
    @classmethod
    def setUpClass(cls):
        cls.encoder = EgiatEncoder()
    
    def test_empty_string_encoding(self):
        """Test encoding empty string"""
        encoded = self.encoder.encode_text('')
        self.assertEqual(encoded, '')
    
    def test_empty_string_decoding(self):
        """Test decoding empty string"""
        decoded = self.encoder.decode_text('')
        self.assertEqual(decoded, '')
    
    def test_whitespace_only(self):
        """Test encoding whitespace only"""
        encoded = self.encoder.encode_text('   ')
        self.assertEqual(encoded, '   ')
    
    def test_lowercase_handling(self):
        """Test that lowercase is handled correctly"""
        upper = self.encoder.encode_text('HELLO')
        lower = self.encoder.encode_text('hello')
        mixed = self.encoder.encode_text('HeLLo')
        
        self.assertEqual(upper, lower)
        self.assertEqual(upper, mixed)
    
    def test_special_characters(self):
        """Test handling of special characters"""
        text = 'HELLO@WORLD#2028'
        encoded = self.encoder.encode_text(text)
        decoded = self.encoder.decode_text(encoded)
        
        # Letters should be encoded, special chars preserved
        self.assertIn('@', encoded)
        self.assertIn('#', encoded)
        self.assertIn('2028', encoded)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
