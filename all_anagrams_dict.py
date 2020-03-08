from anagram import all_words_set
import pprint

def create_dict(set_of_words):
    new_dict = dict()
    word_dict = {}
    pp = pprint.PrettyPrinter(indent=4)
    for word in set_of_words:
        word_sorted = sorted(word)
        end = len(word_sorted) - 1
        new_dict = word_dict
        for i, letter in enumerate(word_sorted):
            if letter not in word_dict.keys():
                word_dict[letter] = {}
            word_dict = word_dict[letter]
            pp.pprint(word_dict)

            i += 1
            # if i == end:
            #     word_dict["word"] = word
        

    return new_dict


if __name__ == "__main__":
    words = set(["dog", "god", "hello"])

    print(create_dict(words))