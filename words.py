def print_upper_words(words):
    #for word in words:
        #print(word.upper())
    
    #for word in words:
        #if word.lower().startswith('e'):
            #print(word.upper())

    for word in words:
        if word[0].lower() in letters:
            print(word.upper())


#print_upper_words(["hello", "hey", "hi", "hola"])
#print_upper_words(["hello", "eat", "hey", "earth"])
print_upper_words(["hello", "you", "green"], {"h","y"})
