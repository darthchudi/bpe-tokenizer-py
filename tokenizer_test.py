import unittest
from tokenizer import BPETokenizer


class TestBPETokenizer(unittest.TestCase):
    def setUp(self):
        # Setup for all tests
        corpus = "This is an example that we will use to demonstrate BPE."
        self.bpe_tokenizer = BPETokenizer(
            corpus=corpus,
            vocabulary_size=50,
            handle_unknown_characters=False,
            debug=False,
        )

    def test_tokenize_simple_sequence(self):
        # Test basic tokenization and decoding
        test_sequence = "This is a test sentence to encode"
        tokenized_sequence = self.bpe_tokenizer.tokenise(test_sequence)
        decoded_sequence = self.bpe_tokenizer.decode(tokenized_sequence)
        self.assertEqual(
            test_sequence,
            decoded_sequence,
            "Failed to decode back to original sequence",
        )

    def test_tokenize_with_repeated_patterns(self):
        # Test tokenization of words with repeated characters
        test_sequence = "loose goose"
        tokenized_sequence = self.bpe_tokenizer.tokenise(test_sequence)
        decoded_sequence = self.bpe_tokenizer.decode(tokenized_sequence)
        self.assertEqual(
            test_sequence,
            decoded_sequence,
            "Failed to tokenize and decode repeated patterns correctly",
        )

    def test_handle_unknown_characters(self):
        # Test handling of unknown characters
        test_sequence = "xyz abc"
        tokenized_sequence = self.bpe_tokenizer.tokenise(test_sequence)
        decoded_sequence = self.bpe_tokenizer.decode(tokenized_sequence)
        self.assertEqual(
            test_sequence,
            decoded_sequence,
            "Failed to handle unknown characters correctly",
        )

    def test_empty_input(self):
        # Test tokenization of an empty string
        test_sequence = ""
        tokenized_sequence = self.bpe_tokenizer.tokenise(test_sequence)
        decoded_sequence = self.bpe_tokenizer.decode(tokenized_sequence)
        self.assertEqual(
            test_sequence, decoded_sequence, "Failed to handle empty input correctly"
        )

    def test_punctuation_handling(self):
        # Test tokenization and decoding with punctuation
        test_sequence = "Hello, world! How's it going?"
        tokenized_sequence = self.bpe_tokenizer.tokenise(test_sequence)
        decoded_sequence = self.bpe_tokenizer.decode(tokenized_sequence)
        self.assertEqual(
            test_sequence, decoded_sequence, "Failed to handle punctuation correctly"
        )


if __name__ == "__main__":
    unittest.main()
