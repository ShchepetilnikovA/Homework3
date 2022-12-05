lst_1 = [1, 4, 7, 3, 9, 14, 11]
for i in range(round(len(lst_1) / 2)):
    print(lst_1[i] * (lst_1[-i - 1]))