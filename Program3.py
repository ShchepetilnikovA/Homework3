lst: float = [1.1, 1.2, 3.1, 5, 10.01]
lst_float: float = []


def find (lst):    
    for i in range(len(lst)):
        lst[i] = lst[i] % 1 
        if lst[i] != 0:
            lst_float.append(lst[i])


find(lst)
lst_float.sort()
print(lst_float[-1] - lst_float[0])
