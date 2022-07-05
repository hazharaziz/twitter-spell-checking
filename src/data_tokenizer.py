
from nltk.tokenize import sent_tokenize, word_tokenize
import csv

file1 = open('output.csv', encoding='utf-8', errors='ignore')
read_file = file1.read()

word_token=word_tokenize(read_file)
sentence_token=sent_tokenize(read_file)

sentences=len(sentence_token)
print("length of sentences:")
print(sentences)
words=len(word_token)
print("length of words:")
print(words)

freq=dict(zip(word_token,[word_token.count(i) for i in word_token]))

unique_word_count = len(freq)
print("unique word :")
print(unique_word_count)

freq_sort=sorted(freq.items(), key=lambda item: item[1])
print("frequency :")
print(freq_sort)



def main():
    file = open('output.csv', 'r', encoding='utf-8', errors='ignore')
    tweets= csv.reader(file)
    s = []
    w  = []
    for tw in tweets:
        tweet = tw[0]
        sent = sent_tokenize(tweet)
        s.append(sent)
        word = word_tokenize(tweet)
        w.append(word)

    with open('sentence_broken.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(s)
    with open('word_broken.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(w)



if __name__ == '__main__':
    main()
