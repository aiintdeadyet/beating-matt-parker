# trying to find 5 words each containing 5 letters with no letter repeated 


def take5(in_file):
    '''takes a word list file returns a set of only 5 letter words'''
    f = open(in_file, 'r') # opens file of all english words
    all_words = f.readlines() # reads in word list
    word_set = set()
    for word in all_words:
        strip_word = word.strip().lower() # gets rid of all extra char
        # adds word to set of words
        if len(strip_word) == 5: 
            word_set.add(strip_word)

    return word_set


def main():
    '''runs program'''
    print(take5("wordlist_all.txt"))


if __name__ == "__main__":
    main()