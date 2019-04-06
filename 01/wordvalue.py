from data import DICTIONARY, LETTER_SCORES



def load_words():
    """Load dictionary into a list and return list"""
    f = open(DICTIONARY, 'r')
    content = f.read()
    f.close()
    dictionary_list = content.split()
    return dictionary_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    word_value = 0
    for letter in word:
        try:
            word_value += LETTER_SCORES[letter.upper()]
        except:
            pass
    return word_value

def max_word_value(word_list = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_value_word = ''
    for word in word_list:
        word_value = calc_word_value(word)
        if word_value > max_value:
            max_value_word = word
            max_value = word_value
    return max_value_word

if __name__ == "__main__":
    pass # run unittests to validate
