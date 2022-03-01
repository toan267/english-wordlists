import re
def load_words():
    # with open('words_alpha.txt') as word_file:
    with open('OALD8_abridged_edited.txt') as word_file:
        # valid_words = set(word_file.read().split())
        valid_words = word_file.readlines()

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    # print('fate' in english_words)
    r = re.compile(".*eɪ.*")
    newlist = list(filter(r.match, english_words))
    print("".join(newlist))
    
