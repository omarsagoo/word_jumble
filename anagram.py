from itertools import permutations

def all_words_set(file):
    """create a set of all the words in the dictionary.
    o(n) time complexity, where n is the number of words in the dictionary
    not the most efficient, but also not the least."""
    dictFile = open(file, 'r')
    wordSet = set()
    for word in dictFile:
        wordSet.add(word.replace("\n", ''))
    return wordSet

def solver(anagram, word_set):
    """ solves an anagram with all possible words,
    o(p) where p is the number of permutations that an anagram has.
    not the most efficient, but also not the least. solves inidividual words quickly."""
    word_list = []
    for perm in permutations(anagram.lower()):
        if ''.join(perm) in word_set:
            if ''.join(perm) not in word_list:
                word_list.append(''.join(perm))
    return word_list

def letter_list(word_list):
    """returns a list of all the letters that belong in the solution
    o(n) where n is the length of the word that was created. ussually very small,
    upper limit is the longest word in the dictionary.
    This solution is not exponential because It is assumed that This is solving a puzzle of a few words
    not a huge list of 1 million words with the longest word being the longest word in the dictionary."""
    pair_list = []
    letters = []
    letters_list = []


    for item, sol in word_list:
        for word in item:
            for i, letter in enumerate(word):
                if sol[i] == "o":
                    letters.append(letter)
            pair_list.append(letters)
            letters = []
        letters_list.append(pair_list)
        pair_list = []

    return letters_list

def final_finder(letters_list):
    """returns all possible word combinations for the final statement
                            not completed"""
    letters = []
    final_letters = []
    group2_letters = []

    for group1 in letters_list:
        if len(group1) == 1:
            for group2 in group1:
                for letter in group2:
                    letters.append(letter)
            
        else:
            for group2 in group1:
                group2_letters.append(group2)

    if len(group2_letters) >= 1:

        for group in group2_letters:
            group += letters
            final_letters.append(group)
    else:
        final_letters.append(letters)
    
    return final_letters
    # print(possible_words(final_letters))

def possible_words(letters, final):
    """returns a list of all the possible words in the solution,
    same time complexity as solver.
    o(p) where p is the number of permutations a word has.
    upper limit is the longest word in the dictionary.
    This solution is not exponential because It is assumed that This is solving a puzzle of a few words
    not a huge list of 1 million words
    """
    words = []
    final_combo = []
    word_set = all_words_set('/usr/share/dict/words')

    for word in final:
        num = len(word)
        for lettergroup in letters:
            for perm in permutations(lettergroup, num):
                if ''.join(perm) in word_set:
                    if ''.join(perm) not in words:
                        words.append(''.join(perm))
            final_combo.append(words)
            words = []

    return final_combo

def all_letters(words, set_of_words, solutions):
    word_list = []

    for i, word in enumerate(words):
        ans = solver(word, set_of_words)
        word_list.append((ans, solutions[i]))
    return word_list


