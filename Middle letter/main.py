def mid(word):
    length=len(word)
    if length%2!=0:
        l_word=list(word)
        n_mid =int(length/2)
        return l_word[n_mid]
    else:
        return ""
word = input("Enter a word: ")
print(mid(word))