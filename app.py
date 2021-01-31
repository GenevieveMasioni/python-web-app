#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author  Geneviève Masioni <masionigenevieve@gmail.com>
# Version 0.0.1
#

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def execute_request():
    input = request.form['words']
    if(input):
        words = input.split(',')
        clean_list(words)
        result = get_occurrences(words)
        return render_template('index.html', list_of_tuples=result)
    return render_template('index.html', list_of_tuples="Empty input")

def clean_list(l):
    for i in range(len(l)):
        l[i] = l[i].strip().lower()

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

if __name__ == '__main__':
   app.run()
