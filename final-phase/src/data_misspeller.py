import csv
import random
import string
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk import TreebankWordDetokenizer

nltk.download('punkt')

keyboard_rows = [["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", ""],
                 ["", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", ""],
                 ["", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "", "", ""],
                 ["", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "", "", ""],
                 ["", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "|"],
                 ["","A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "", "", ""],
                 ["", "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?", "", "", ""]]


def find_keyboard_coordinates(char, my_list=keyboard_rows):
    for sub_list in my_list:
        if char in sub_list:
            return my_list.index(sub_list), sub_list.index(char)


def find_adjacents(char):
    x, y = find_keyboard_coordinates(char)
    adjacents = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            try:
                adjacents.append(keyboard_rows[i][j])
            except:
                continue
    adjacents.remove(char)
    return adjacents


def replace_noise(token, random_index):
    c = token[random_index]
    c_adjacents = find_adjacents(c)
    new_char = random.choice(c_adjacents)
    return token[:random_index] + new_char + token[random_index + 1:]


def extra_noise(token, random_index):
    new_char = random.choice(string.ascii_letters)
    return token[:random_index] + new_char + token[random_index + 1:]


def eliminate_noise(token, random_index):
    return token[:random_index] + token[random_index + 1:]

def transposition_noise(token, random_index):
    if random_index == 0:
        random_index = random.randint(1, len(token) - 1)
    return token[:random_index-1] + token[random_index] + token[random_index-1]+token[random_index+1:]


def applyNoiseOnToken(token, alogrithm_name):
    random_index = random.randint(0, len(token) - 1)
    if (alogrithm_name == 'replace'):
        return replace_noise(token, random_index)
    elif (alogrithm_name == 'extra'):
        return extra_noise(token, random_index)
    elif (alogrithm_name == 'eliminate'):
        return eliminate_noise(token, random_index)
    elif (alogrithm_name == 'transposition'):
        return transposition_noise(token, random_index)
    else:
        return token

def addNoise(tokens):

    noise_algorithms = ['replace', 'extra', 'eliminate', 'transposition']
    new_tokens = tokens[:]

    tokens_to_be_noised_count = random.randint(1, 3)
    noised_count = 0
    tokens_checked_count = 0

    while noised_count < tokens_to_be_noised_count:
        if (tokens_checked_count > len(new_tokens) - 1):
            break

        target_token_index = random.randint(0, len(new_tokens) - 1)
        target_token = new_tokens[target_token_index]

        if (len(target_token) < 3):
            tokens_checked_count += 1
            continue

        algorithm = noise_algorithms[random.randint(0, len(noise_algorithms) - 1)]
        new_token = applyNoiseOnToken(target_token, algorithm)
        new_tokens[target_token_index] = new_token
        
        noised_count += 1

    return new_tokens

def main():
    file = open('final-phase/data/cleaned/false.csv', 'r', encoding='utf-8', errors='ignore')
    tweets= csv.reader(file)
    w  = []
    for tw in tweets:
        tweet = tw[0]
        words = word_tokenize(tweet)
        noisy_words = addNoise(words)
        w.append([TreebankWordDetokenizer().detokenize(noisy_words)])


    with open('final-phase/data/labeled/false.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(w)
    

if __name__ == '__main__':
    main()
