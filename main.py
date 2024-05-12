from tokenizer import BPETokenizer

def run():
    # Basic setup
    corpus = "This is an example that we will use to demonstrate BPE."
    bpe_tokenizer = BPETokenizer(corpus=corpus, vocabulary_size=50, handle_unknown_characters=False, debug=False)
    print("Base Vocabulary:", bpe_tokenizer.vocabulary)

    # Simple sentence tokenization and decoding
    test_sequence = "This is a test sentence to encode"
    tokenised_sequence = bpe_tokenizer.tokenise(test_sequence)
    decoded_sequence = bpe_tokenizer.decode(tokenised_sequence)

    print("Tokens: ", tokenised_sequence)
    print("Decoded: ", decoded_sequence)
    print("Original: ", test_sequence)
    print("Matched: ", decoded_sequence == test_sequence)


if __name__ == "__main__":
    run()
