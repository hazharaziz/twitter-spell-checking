import csv
import re
import matplotlib.pyplot as plt
import nltk
import numpy as np
from nltk import TreebankWordDetokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def whiteSpace(input_str):
    return re.sub(' +', ' ', input_str)

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

def remove_digit(input_str):
    return (re.sub(r'[^a-zA-Z\s]+', '', input_str))

def remove_mentions(tweet):
    tweet = re.sub(r'@[\w_]+', '', tweet)
    return tweet

def remove_hashtags(tweet):
    tweet = re.sub(r'#[\w_]+', '', tweet)
    return tweet

def stopWords(input_str):
    stop_words = set(stopwords.words('english'))
    result = [i for i in input_str if not i in stop_words]
    return result


def main():

    source_data_path = 'final-phase/data/raw/raw_data.csv'
    cleaned_data_path = 'final-phase/data/cleaned/cleaned_data.csv'

    file = open(source_data_path, 'r', encoding='utf-8', errors='ignore')
    tweets = csv.reader(file)

    filtered_tweets = []
    for tweet in tweets:
        tweet = tweet[0]
        hashtag_removed = remove_hashtags(tweet)
        mentions_removed = remove_mentions(hashtag_removed)
        whitespace_removed = whiteSpace(mentions_removed)
        url_removed = remove_url(whitespace_removed)
        tokens = word_tokenize(url_removed)
        filtered_tweets.append([TreebankWordDetokenizer().detokenize(tokens)])

    with open(cleaned_data_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filtered_tweets)

if __name__ == '__main__':
    main()
