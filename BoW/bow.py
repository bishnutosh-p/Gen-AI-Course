from collections import defaultdict
import numpy as np
import torch
from torch import nn
from torch.autograd import Variable
from model import BoW   #ASSIGNMENT PART 1

w2i = defaultdict(lambda: len(w2i)) # word to index mapping
t2i = defaultdict(lambda: len(w2i)) # tags to index mapping
UNK = w2i["<unk>"]

def read_corpus(filename):
    with open(filename, 'r') as fl:
        for line in fl:
            tag, words = line.lower().strip().split(" ||| ")
            yield ([w2i[x] for x in words.split(" ")], t2i[tag] )

train_dataframe = list(read_corpus("D:\Gen AI Internship Course\Assignments\BoW\train.txt"))

w2i = defaultdict(lambda: UNK, w2i)
nwords = len(w2i) #no of unique words in the dataset
ntags = len(t2i) #no of unique tags n the dataset

model = BoW(nwords, ntags)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

#TRAINING LOOP

for i in range(100):
    train_loss = 0.0
    for word, tag in train_dataframe:
        words = torch.tensor(words).type(type)
        tags = torch.tensor(tags).type(type)
        scores = model(words)
        loss = criterion(scores, tags)
        train_loss += loss.item()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # DO THE SAME FOR TEST AND PRINT THE ITERATION AND TRAINING, TEST LOSS #ASSIGNMENT PART 2


# from collections import defaultdict
# import torch
# from torch import nn
# from torch.autograd import Variable

# # Assuming BoW model is defined elsewhere or use the provided BoW implementation above

# # Define the mappings
# w2i = defaultdict(lambda: len(w2i)) # word to index mapping
# t2i = defaultdict(lambda: len(t2i)) # tags to index mapping
# UNK = w2i["<unk>"]

# def read_corpus(filename):
#     with open(filename, 'r') as fl:
#         for line in fl:
#             tag, words = line.lower().strip().split(" ||| ")
#             yield ([w2i[x] for x in words.split(" ")], t2i[tag])

# # Read the training data
# train = list(read_corpus("C:/Users/parroy/Downloads/train.txt"))

# # Freeze the mappings by switching to default UNK
# w2i = defaultdict(lambda: UNK, w2i)
# nwords = len(w2i)  # number of unique words in the dataset
# ntags = len(t2i)   # number of unique tags in the dataset

# # Define the model, criterion, and optimizer
# model = BoW(nwords, ntags)
# criterion = nn.CrossEntropyLoss()
# optimizer = torch.optim.Adam(model.parameters())

# # Training loop
# for epoch in range(100):
#     train_loss = 0.0
#     for words, tag in train:
#         words_tensor = torch.tensor(words, dtype=torch.long)
#         tags_tensor = torch.tensor([tag], dtype=torch.long)
#         scores = model(words_tensor)
#         loss = criterion(scores, tags_tensor)
#         train_loss += loss.item()
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     print(f"Epoch {epoch + 1}, Train Loss: {train_loss / len(train)}")

#     # If there is a test set, you should evaluate it here
#     # test = list(read_corpus("path/to/test.txt"))  # Ensure test set exists
#     # test_loss = 0.0
#     # for words, tag in test:
#     #     words_tensor = torch.tensor(words, dtype=torch.long)
#     #     tags_tensor = torch.tensor([tag], dtype=torch.long)
#     #     with torch.no_grad():
#     #         scores = model(words_tensor)
#     #         loss = criterion(scores, tags_tensor)
#     #         test_loss += loss.item()
#     # print(f"Epoch {epoch + 1}, Test Loss: {test_loss / len(test)}")
