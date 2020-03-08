import unittest

from anagram import solver, all_words_set, all_letters, letter_list, final_finder

class AnagramTest(unittest.TestCase):
    
    def test_solver(self):
        word_set = all_words_set('/usr/share/dict/words')
        assert solver("tofen", word_set) == ["often"]
        letters = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
        
        assert solver('SOKIK', word_set) == ["kiosk"]
        assert solver("niumem", word_set) == ["immune"]
        assert solver("laurr", word_set) == ["urlar", "rural"]

    def test_all_letters(self):
        [(['often'], '_ooo_'), (['urlar', 'rural'], 'o_o__'), (['rebuke'], 'oo____'), (['uproot'], '__o_oo')]
        word_set = all_words_set('/usr/share/dict/words')
        letters = ['tfoen', 'laurr', 'bureek', 'prouot']

        assert all_letters(letters, word_set) == [(['often'], '_ooo_'), (['urlar', 'rural'], 'o_o__'), (['rebuke'], 'oo____'), (['uproot'], '__o_oo')]

    def test_letter_list(self):
        word_set = all_words_set('/usr/share/dict/words')
        letters = ['tfoen', 'laurr', 'bureek', 'prouot']
        all_let = all_letters(letters, word_set)
        assert all_let == [(['often'], '_ooo_'), (['urlar', 'rural'], 'o_o__'), (['rebuke'], 'oo____'), (['uproot'], '__o_oo')]
        list_of_letters_in_answer = letter_list(all_let)
        assert list_of_letters_in_answer == [[['f', 't', 'e']], [['u', 'l'], ['r', 'r']], [['r', 'e']], [['r', 'o', 't']]]

    def test_all_possible_letters(self):
        word_set = all_words_set('/usr/share/dict/words')
        letters = ['tfoen', 'laurr', 'bureek', 'prouot']
        all_let = all_letters(letters, word_set)
        assert all_let == [(['often'], '_ooo_'), (['urlar', 'rural'], 'o_o__'), (['rebuke'], 'oo____'), (['uproot'], '__o_oo')]
        list_of_letters_in_answer = letter_list(all_let)
        assert list_of_letters_in_answer == [[['f', 't', 'e']], [['u', 'l'], ['r', 'r']], [['r', 'e']], [['r', 'o', 't']]]
        final_letters = final_finder(list_of_letters_in_answer)
        assert final_letters == [['u', 'l', 'f', 't', 'e', 'r', 'e', 'r', 'o', 't'], ['r', 'r', 'f', 't', 'e', 'r', 'e', 'r', 'o', 't']]