#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author  Geneviève Masioni <masionigenevieve@gmail.com>
# Version 0.0.1
#

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def test_get_occurrences():
    words = ['apple', 'lemon', 'banana', 'apple', 'apple', 'banana', 'lime', 'apricot']
    expected_result = [('apple', 3) , ('banana', 2) , ('apricot', 1), ('lemon',1), ('lime', 1)]
    # words = ['apple', 'fruit', 'abb', 'pomme', 'lemon', 'banana', 'abb', 'apple', 'apple', 'banana', 'abb','lime', 'apricot']
    # expected_result = [('abb', 3), ('apple', 3) , ('banana', 2) , ('apricot', 1), ('fruit', 1), ('lemon',1), ('lime', 1), ('pomme', 1)]
    result = get_occurrences(words)
    print(result)
    if(result == expected_result):
        print("test_get_occurrences[OK]")
    else:
        print("test_get_occurrences[FAILED]")

def get_occurrences(words):
    result = {}
    nb_words = len(words)
    for i in range(nb_words):
        if words[i] in result:
            result[words[i]] += 1
        else:
            result[words[i]] = 1
    result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    # sort subsets of tuples in alphabetical order
    i = j = 0;
    while j <= len(result):
        if (j == len(result)) or (result[j][1] < result[i][1]):
            subset = result[i:j]
            subset.sort(key=lambda tup: tup[0])
            result[i:j] = subset
            i = j
        j += 1
    return result
