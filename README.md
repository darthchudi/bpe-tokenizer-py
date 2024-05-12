# Byte-Pair Encoding Tokenizer 

This project implements the byte-pair encoding (BPE) algorithm and adapts it for tokenization. The implemented tokenizer produces sub-word tokens when tokenizing a given input sequence.

A vocabulary interface is also implemented, which handles mapping between subword tokens and their corresponding indices in the vocabulary. This vocabulary implementation also provides utility methods for use within the context of a Transformer model.

## Usage

```python

from tokenizer import BPETokenizer

# Initialize the tokenizer with a corpus and a vocabulary size
tokenizer = BPETokenizer(corpus, vocabulary_size)

# Tokenize an input sequence
tokens = tokenizer.tokenise(input_sequence)

# Decode an encoded sequence
decoded_sequence = tokenizer.decode(tokens)
```

## Running the project

You can run the project using the following command:

```bash
make run
```

## Testing

To run the tests, use the following command:

```bash
make test
```

## References

1. [Neural Machine Translation of Rare Words with Subword Units (Sennrich et al., 2015)](https://arxiv.org/pdf/1508.07909)