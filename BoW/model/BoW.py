# import torch
# from torch import nn

# class BoW(nn.Module):
#     def __init__(self, vocab_size, num_classes):
#         super(BoW, self).__init__()
#         self.embedding = nn.EmbeddingBag(vocab_size, num_classes, sparse=True)
#         self.linear = nn.Linear(num_classes, num_classes)

#     def forward(self, text):
#         embedded = self.embedding(text)
#         return self.linear(embedded)

# def create_bag_of_words(corpus):
#     # Initialize an empty dictionary to store the word frequencies
#     word_freq = {}

#     # Iterate over each document in the corpus
#     for document in corpus:
#         # Split the document into individual words
#         words = document.split()

#         # Iterate over each word in the document
#         for word in words:
#             # Increment the frequency count of the word
#             if word in word_freq:
#                 word_freq[word] += 1
#             else:
#                 word_freq[word] = 1

#     # Return the bag of words model
#     return word_freq

######  This is the part in which we are making the get_status and merge_vocab functions.

from collections import defaultdict, Counter

def get_stats(vocab):
    """
    Calculate frequency of each pair of consecutive symbols in the vocabulary.
    
    Args:
    vocab (dict): A dictionary where keys are words and values are their frequencies.
    
    Returns:
    dict: A dictionary where keys are pairs of symbols and values are their frequencies.
    """
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += freq
    return pairs

def merge_vocab(pair, vocab):
    """
    Merge the most frequent pair of symbols in the vocabulary.
    
    Args:
    pair (tuple): A tuple representing the most frequent pair of symbols.
    vocab (dict): A dictionary where keys are words and values are their frequencies.
    
    Returns:
    dict: A new vocabulary dictionary with the most frequent pair merged.
    """
    new_vocab = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in vocab:
        new_word = word.replace(bigram, replacement)
        new_vocab[new_word] = vocab[word]
    return new_vocab

# Example usage:
vocab = {'l o w </w>': 5, 'l o w e r </w>': 2, 'n e w e s t </w>': 6, 'w i d e s t </w>': 3}

# Initial get_stats
pairs = get_stats(vocab)
print(pairs)

# Initial merge_vocab
vocab = merge_vocab(('e', 's'), vocab)
print(vocab)

# Continuing the process
num_merges = 10
for _ in range(num_merges):
    pairs = get_stats(vocab)
    if not pairs:
        break
    best_pair = max(pairs, key=pairs.get)
    vocab = merge_vocab(best_pair, vocab)
    print(vocab)



#######


# import torch
# from torch import nn
# from torch.autograd import Variable

# class BOW (torch.nn.module):
# def __init__(self, nwords, ntags):
# super(BOW, self).__init__()

# self.bias = Variable(torch.zeros(ntags), requires_grad = True). type(FloatTensor)
# self.embedding = nn.Embedding(nwords, ntags)
# nn.init.xavier_uniform(self.embedding.weight)

# def forward (self, words) :
# emb = self.embedding(words)
# out =torch.sum(emb, dim = 0) + self.bias -> 1xN
# out = out.view (1, -1)
# return out