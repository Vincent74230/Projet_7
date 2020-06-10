'''App's parser, imports a list to work with'''
from .usual_words import stop_words
PUNCTUATIONS = ['`', '~', '!', '@', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', ':', ';',
                '<', '>', '.', '?', '/', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def parser(users_question):
    """Parser : takes a sentence as entry and return simple words"""
    users_question = users_question.lower()
    elements = list(users_question)
    removable_elements = []
    for element in elements:
        for punctuation in PUNCTUATIONS:
            if element == punctuation:
                removable_elements.append(element)

    for element in removable_elements:
        elements.remove(element)
    users_question = ''.join(elements)

    decomposed_question = users_question.split(" ")
    removable_elements = []
    for word in decomposed_question:
        for stop_word in stop_words:
            if word == stop_word:
                removable_elements.append(word)

    for word in removable_elements:
        decomposed_question.remove(word)

    magic_word = " ".join(decomposed_question)

    return magic_word
