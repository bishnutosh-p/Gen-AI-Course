import torch
from torch import nn

class BoW(nn.Module):
    def __init__(self, vocab_size, num_classes):
        super(BoW, self).__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, num_classes, sparse=True)
        self.linear = nn.Linear(num_classes, num_classes)

    def forward(self, text):
        embedded = self.embedding(text)
        return self.linear(embedded)

def create_bag_of_words(corpus):
    # Initialize an empty dictionary to store the word frequencies
    word_freq = {}

    # Iterate over each document in the corpus
    for document in corpus:
        # Split the document into individual words
        words = document.split()

        # Iterate over each word in the document
        for word in words:
            # Increment the frequency count of the word
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    # Return the bag of words model
    return word_freq