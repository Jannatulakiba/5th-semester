def generate_ngrams(text, n):
    # Tokenize the text into words
    words = text.split()
    
    # Generate n-grams
    ngrams = []
    for i in range(len(words)-n+1):
        ngrams.append(tuple(words[i:i+n]))
    return ngrams

# Example usage
text = "I love learning Python programming"
n = 2  # Change to 3 for trigrams, etc.

bigrams = generate_ngrams(text, n)
print(bigrams)
