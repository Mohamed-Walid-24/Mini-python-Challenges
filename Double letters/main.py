def double_letters(word):
    l_word=list(word)
    length = len(word)
    i=0
    for letter in word:
        if i < length-1:
            if l_word[i]==l_word[i+1]:
                return True
        else:
            return False
        i=i+1
    return False #if there is now entered
word = input("Enter a word: ")
print(double_letters(word))
