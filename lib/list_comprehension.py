#!/usr/bin/env python3

def return_evens(num_list):
    if len(num_list) == 0:
        return []
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return []
    return [sentence + "!" for sentence in sentence_list]