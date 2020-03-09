from anagram import all_words_set, letter_list, all_letters, final_finder, solver

def main():

    words = input("Input anagrams to decode: ")
    sol = input(f"solutions to the {len(words)} anagrams (in the same order, format'__o__o'): ")
    final = input("input the final solution: (format: 'OOOO OOOO' upper(o) not 0)")

    word_set = all_words_set('/usr/share/dict/words')
        

    for word in words.split():
        print(f"word: {word}\nSolution/s: {solver(word, word_set)}\n")

    letters = all_letters(words.split(), word_set, sol.split())
    print(f"answers for solution:\n{letters}\n")

    list_of_letters = letter_list(letters)
    final_letters = final_finder(list_of_letters)
    print(f"all letters for the word:\n{final_letters}\n")

if __name__ == "__main__":
    main()