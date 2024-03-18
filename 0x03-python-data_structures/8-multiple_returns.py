#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        n_sentence = (lenght, None)
    elif lenght > 0:
        n_sentence = (lenght, sentence[0])
    return n_sentence
