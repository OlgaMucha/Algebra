def binary_to_decimal(binary):
    print('*************************')
    print('binary: ', binary)
    decimal = 0
    for i in range(len(binary)):
        decimal = decimal + int(binary[len(binary)-1-i])*2**i
    print('decimal: ', decimal)
    return decimal
    print('**************************')


def decimal_to_binary(decimal):
    print('**************************')
    print('decimal: ', decimal)
    for i in range(1500):
        if (int(decimal)-2**i)*(int(decimal)-2**(i+1)) < 0:
            limit = i + 1
    dec_number = int(decimal)
    lst = []
    for i in range(1, limit + 1):
        lst = lst + [dec_number // 2 ** (limit - i) % 2]
    binary = int(''.join(str(x) for x in lst))
    print('binary: ', binary)
    return binary
    print('**************************')


def hexidecimal_to_decimal(hexidecimal):
    print('**************************')
    print('hexidecimal: ', hexidecimal)
    extra_letters = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    decimal = 0
    for i in range(len(hexidecimal)):
        if hexidecimal[len(hexidecimal)-1-i] in extra_letters.keys():
            decimal = decimal + extra_letters[hexidecimal[len(hexidecimal)-1-i]]*16**i
        else:
            decimal = decimal + int(hexidecimal[len(hexidecimal) - 1 - i])*16 ** i
    print('decimal: ', decimal)
    return decimal
    print('**************************')

def decimal_to_hexidecimal(decimal):
    print('**************************')
    print('decimal: ', decimal)

    extra_letters = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

    for i in range(1500):
        if (int(decimal)-16**i)*(int(decimal)-16**(i+1)) < 0:
            limit = i + 1

    dec_number = int(decimal)
    lst = []
    for i in range(1, limit + 1):
        if dec_number // 16 ** (limit - i) % 16 < 10:
            lst = lst + [dec_number // 16 ** (limit - i) % 16]
        else:
            for key, value in extra_letters.items():
                if value == dec_number // 16 ** (limit - i) % 16:
                    lst = lst + [key]


    hexidecimal = ''.join(str(x) for x in lst)
    print('hexidecimal: ', hexidecimal)
    return hexidecimal
    print('**************************')


