def is_anagram(word_1,word_2):
    l_word_1=list(word_1.lower())
    l_word_2=list(word_2.lower())
    l_word_1.sort()
    l_word_2.sort()
    if l_word_1==l_word_2:
        return True
    else:
        return False
word_1=input("First: ")
word_2=input("Second: ")
print(is_anagram(word_1,word_2))

