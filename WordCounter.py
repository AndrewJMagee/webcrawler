import requests
from bs4 import BeautifulSoup
import operator

# Word counter for local news source


def start(url):
    word_list = []
    source_code = requests.get(url).text  # gets url
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll("a", {'class': 'complexListingLink'}):  # found what I wanted in sourcecode...
                                                                          # I wanted to search through user submitted posts.
                                                                          # So this is what class they were in in website source code.
        content = post_text.string  # this cleans out all html and just gives me actual text
                                    # however, we don't want full sentences. We just want individual words.
        words = content.lower().split()
                                    # this takes the content, lower cases everything, and splits up your string based on spaces
        for each_word in words:

            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):  # this looks through every word, finds symbols, and replaces them with blank space
    clean_word_list = []
    for word in word_list:
        symbols = "[~`!@#$%^&*()_+{}[]:;,.\"<>'=-]"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)  # For something like :)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):    # dictionary of all words found on page
    word_count = {}
    for word in clean_word_list:
        if word in word_count:             # if the word already exists add 1 to its value
            word_count[word] += 1
        else:
            word_count[word] = 1           # if not the case, then assign it to 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):  # this is to sort by value. 0 is alphebetical, 1 is value
        print(key, value)

start('http://www.lowellsun.com/')
