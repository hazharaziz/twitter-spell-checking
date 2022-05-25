import csv
import re
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from nltk import TreebankWordDetokenizer
from nltk.corpus import stopwords
from nltk.tokenize import  word_tokenize


def whiteSpace(input_str):
    return re.sub(' +', ' ', input_str)

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

def remove_digit(input_str):
    return (re.sub(r'[^a-zA-Z\s]+', '', input_str))



def stopWords(input_str):
    stop_words = set(stopwords.words('english'))
    result = [i for i in input_str if not i in stop_words]
    return result


def main():

    file = open('output.csv', 'r', encoding='utf-8', errors='ignore')
    tweets= csv.reader(file)
    s = []
    for tw in tweets:
        tweet = tw[0]
        res = whiteSpace(tweet)
        text = remove_url(res)
        text2=remove_digit(text)
        tokens = word_tokenize(text2)
        token = stopWords(tokens)
        s.append([TreebankWordDetokenizer().detokenize(token)])

    with open('cleaned.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(s)

    file1 = open('cleaned.csv', encoding='utf-8', errors='ignore')
    read_file = file1.read()

    # counts = Counter(word_tokenize(read_file))
    # labels, values = zip(*counts.items())
    # indSort = np.argsort(values)[::-1]
    #
    # labels = np.array(labels)[indSort]
    # values = np.array(values)[indSort]
    # indexes = np.arange(len(labels))
    # bar_width = 0.35
    # plt.bar(indexes, values)
    # plt.xticks(indexes + bar_width, labels)
    # plt.show()


if __name__ == '__main__':
    main()
