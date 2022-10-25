# contains the parker_list class


class Parker_list:
    """Parker_list objects alow for more efficient use of data"""

    def __init__(self, words=[]):
        """Initializes Parker_list objects"""
        self.Words = words
        self.Letters = self.used_letters()

    def used_letters(self):
        """returns a set of letters that have been used in the words"""
        re_set = set()
        for word in self.Words:
            for char in word:
                re_set.add(char)
        return re_set

    def add(self, word):
        """Add word to the object"""
        self.Words.append(word)
        self.Letters = self.used_letters()

    def remove(self, word):
        """Removes a word from the object using either the index or the value of the removed word"""
        if isinstance(word, str):
            self.Words.remove(word)
            self.Letters = self.used_letters()
        elif isinstance(word, int):
            self.Words.pop(word)
            self.Letters = self.used_letters()

    def __len__(self):
        """Returns how manny words are in the object"""
        return len(self.Words)

    def __str__(self):
        """Returns a string representation of the object"""
        return f"Words {str(self.Words)}\nletters used {str(self.Letters)}"


def main():
    park_list = Parker_list(["james", "david"])
    park_list.add("critc")
    park_list.remove(1)
    print(park_list)


if __name__ == "__main__":
    main()
