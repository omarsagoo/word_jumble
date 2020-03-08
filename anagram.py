from itertools import permutations

def all_words_set(file):
    dictFile = open(file, 'r')
    wordSet = set()
    for word in dictFile:
        wordSet.add(word.replace("\n", ''))
    return wordSet

def solver(anagram, word_set):
    word_list = []
    for perm in permutations(anagram.lower()):
        if ''.join(perm) in word_set:
            if ''.join(perm) not in word_list:
                word_list.append(''.join(perm))
    return word_list

def letter_list(word_list):
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
    
    print(possible_words(final_letters))

def possible_words(letters):
    final = ['OOOOO', 'OOOOO']
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



def main():
    import sys
    word_set = all_words_set('/usr/share/dict/words')
    args = sys.argv[1:]
    word_list = []
    word_tuple = ()
    letter_answers = ["_ooo_","o_o__", "oo____", "__o_oo" ]
    for i, arg in enumerate(args):
        word = solver(arg, word_set)
        word_list.append((word, letter_answers[i]))
    final_finder(letter_list(word_list))

if __name__ == "__main__":
    main()

