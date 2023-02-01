def print_upper_words(words, start_letter):
    """ Function takes words from a list and prints them in uppercase """
    for word in words:
        if word[0] is start_letter:
            print(word.upper())
        else:
            continue        

print_upper_words(["ello", "hey", "goodbye", "yo", "yes"], "e")