import unittest

from anagram import solver, all_words_set

class AnagramTest(unittest.TestCase):
    
    def test_solver(self):
        word_set = all_words_set('/usr/share/dict/words')
        assert solver("tofen", word_set) == ["often"]
        letters = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
        
        assert solver('SOKIK', word_set) == ["kiosk"]
        assert solver("niumem", word_set) == ["immune"]
        assert solver("laurr", word_set) == ["urlar", "rural"]
