def add_dots(word):
    l_word=list(word)
    length = len(word)
    for i in range(0,length-1):
        l_word.insert(i*2+1,".")
        #print(l_word,"    ",i)
    word=""
    word=word.join(l_word)
    return word
def remove_dots(word):
    l_word=word.split(".")
    word=""
    word=word.join(l_word)
    return word
word =input("Enter: ")
print(add_dots(word))
#print(remove_dots(add_dots(word)))