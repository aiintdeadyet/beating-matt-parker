# trying to find 5 words each containing 5 letters with no letter repeated
import time, random, string

from parker_list import parker_list


def Narrow_list(in_file):
    """takes a word list file returns a set of only 5 letter words, Helper function for make_park_list"""
    with open(in_file, "r") as f:
        all_words = f.readlines()  # reads in word list
        word_dict = {  # makes dict that will be returned
            "a": [],
            "b": [],
            "c": [],
            "d": [],
            "e": [],
            "f": [],
            "g": [],
            "h": [],
            "i": [],
            "j": [],
            "k": [],
            "l": [],
            "m": [],
            "n": [],
            "o": [],
            "p": [],
            "q": [],
            "r": [],
            "s": [],
            "t": [],
            "u": [],
            "v": [],
            "w": [],
            "x": [],
            "y": [],
            "z": [],
        }
        for word in all_words:
            strip_word = word.lower().strip("\n")  # gets rid of all extra char

            # adds word to set of words
            if (len(strip_word) != 5) or not Check_word(strip_word):
                continue
            for char in strip_word:
                # try:  # if char in word dict
                word_dict[char].append(strip_word)
                # except:  # else forget about it
                #     break

    return word_dict


def Check_word(word):
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


def make_park_list(word_file):    # take word list file as an input
    """make a parker list of words with all uniq letters"""
    word_sets = Narrow_list(word_file) # get word sets 
    re_list = parker_list() # make a parker_list that will be returned
    for i in range(5):
        used_letters = re_list.get_letters() # gets used letters
        letter = random.choice(string.ascii_lowercase)
        while letter in used_letters: # gets a letter that hasn't been used yet
            letter = random.choice(string.ascii_lowercase)
        word = random.choice(word_sets[letter])
        while not (word in re_list.get_words()):
            word_letters = [word]
        
        re_list.add(word)

    return re_list


def main():
    """runs program"""
    start_time = time.time()

    park_list = make_park_list("wordlist_all.txt")
    print(park_list)

    end_time = time.time()
    print("this program took", end_time - start_time, "seconds to run")


if __name__ == "__main__":
    main()
