def only_ints(n_1,n_2):
    try:
        n_1=int(n_1)
        n_2=int(n_2)
        return True
    except:
        return False
n_1 = input()
n_2 = input()
print(only_ints(n_1,n_2))
