import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    return [np.exp(n) / sum(np.exp(L)) for n in L]
