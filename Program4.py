dex_num = int(input('input dex num: '))


def convert_to_double(dex_num):
    if dex_num > 0:
        convert_to_double(dex_num // 2)
        print(dex_num % 2, end='')


convert_to_double(dex_num)
    
