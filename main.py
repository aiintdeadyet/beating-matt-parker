# trying to find 5 words each containing 5 letters with no letter repeated
import re, time


def narrow_list(in_file):
    """takes a word list file returns a set of only 5 letter words"""
    f = open(in_file, "r")  # opens file of all english words
    all_words = f.readlines()  # reads in word list
    word_set = set()  # makes empty set that will be returned
    for word in all_words:
        strip_word = word.lower()  # gets rid of all extra char
        strip_word = re.sub("[\W_]+", "", strip_word)
        # adds word to set of words
        if len(strip_word) != 5:
            continue
        word_set.add(strip_word)

    return word_set


def main():
    """runs program"""
    start_time = time.time()

    narrowed = narrow_list("wordlist_all.txt")
    print(len(narrowed))

    end_time = time.time()
    print("this program took", end_time - start_time, "seconds to run")


if __name__ == "__main__":
    main()
