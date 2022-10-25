# trying to find 5 words each containing 5 letters with no letter repeated
import time


def narrow_list(in_file):
    """takes a word list file returns a set of only 5 letter words"""
    f = open(in_file, "r")  # opens file of all english words
    all_words = f.readlines()  # reads in word list
    word_dict = {  # makes dict that will be returned
        "a": set(),
        "b": set(),
        "c": set(),
        "d": set(),
        "e": set(),
        "f": set(),
        "g": set(),
        "h": set(),
        "i": set(),
        "j": set(),
        "k": set(),
        "l": set(),
        "m": set(),
        "n": set(),
        "o": set(),
        "p": set(),
        "q": set(),
        "r": set(),
        "s": set(),
        "t": set(),
        "u": set(),
        "v": set(),
        "w": set(),
        "x": set(),
        "y": set(),
        "z": set(),
    }
    for word in all_words:
        strip_word = word.lower().strip("\n")  # gets rid of all extra char

        # adds word to set of words
        if (len(strip_word) != 5) or not check_word(strip_word):
            continue
        for char in strip_word:
            # try:  # if char in word dict
            word_dict[char].add(strip_word)
            # except:  # else forget about it
            #     break

    return word_dict


def check_word(word):
    """checks that the word only has letters that don't repeat"""
    char_list = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    used = []  # used char
    for char in word:
        if (
            char not in char_list or char in used
        ):  # if char is a letter we haven't used yet
            return False
        used.append(char)

    return True


def main():
    """runs program"""
    start_time = time.time()

    narrowed = narrow_list("wordlist_all.txt")
    print(narrowed)

    end_time = time.time()
    print("this program took", end_time - start_time, "seconds to run")


if __name__ == "__main__":
    main()
