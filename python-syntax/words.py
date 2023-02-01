def print_upper_words(words, start_letters):
    """ Function takes words from a list and prints them in uppercase 
        Only prints words whose starting letter is contained in start_letters"""
    for word in words:
        for letter in start_letters:
            if word[0] == letter:
                print(word.upper())
            else:
                continue      

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["g","h"])