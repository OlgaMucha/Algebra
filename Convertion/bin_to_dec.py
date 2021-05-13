#Menu convertion

#1
def decimal_to_binary(decimal):
    print('------------------------------')
    print('decimal: ', decimal)
    numbers_decimal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if decimal == '0':
        binary = 0
        print('binary: ', binary)
        return binary
    else:
        s = 0

        for n in decimal:
            if n in numbers_decimal:
                s = s + 1
                continue
                # for every elem of str decimal check if this element is dec, if yes adding 1 to s and continue
            else:
                # if non - decimal value found, loop breaks
                break
        if s < len(decimal):
            # if loop broke before the end there was a non-decimal element, incorrect input message, funct returns None
            print('Incorrect input, not decimal')
            return None
        else:
            for i in range(1500):
            #checking for which i those 2 are opposite signs or one of them or both is 0 to get a number of times
            # we will run a next loop - 1 + 1
                 if (int(decimal)-2**i)*(int(decimal)-2**(i+1)) <= 0:
                    limit = i + 1
            dec_number = int(decimal)
            lst = []
            for i in range(1, limit + 1):
            #this loop will run limit times
                lst = lst + [dec_number // 2 ** (limit - i) % 2]
            binary = int(''.join(str(x) for x in lst))
            #calculating list of consecutive numbers in binary and than a string
            print('binary: ', binary)
            print('------------------------------')
            return binary

#2

def binary_to_decimal(binary):
    print('------------------------')
    print('binary: ', binary)
    numbers_binary = ['0', '1']
    decimal = 0
    if binary == '0':
        decimal = 0
        print('decimal: ', decimal)
        return decimal
    else:
        s = 0
        # for every elem of str binary check if there is a binary element, if yes adding 1 to s and continue
        for n in binary:
            if n in numbers_binary:
                s = s + 1
                continue
            else:
                break
        # if non - binary value found, loop breaks
        if s < len(binary):
            print('incorrect input, not binary')
            return None
        # if loop broke before at least once, there was an non-binary element, funct returns None
        else:
            for i in range(len(binary)):
                decimal = decimal + int(binary[len(binary)-1-i])*2**i
                #calculating decimal
            print('decimal: ', decimal)
            print('------------------------')
            return decimal


#3
def decimal_to_hexadecimal(decimal):
    print('------------------------')
    print('decimal: ', decimal)
    numbers_decimal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    extra_letters = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    lst = []
    if decimal == '0':
        hexadecimal = 0
        print('hexadecimal: ', hexadecimal)
        return hexadecimal
    else:
        s = 0
        # for every elem of str decimal check if every element is decimal, adding 1 to s every time when condition met
        # and continue
        for n in decimal:
            if n in numbers_decimal:
                s = s + 1
                continue
            else:
                break
                # if non - decimal value found, loop breaks
        if s < len(decimal):
            print('Incorrect input, not decimal')
            return None
        # if loop broke before the end there was a non-decimal element, incorrect input message, funct returns None
        else:
            dec_number = int(decimal)
            # checking for which i those 2 are opposite signs or one of them or both is 0 to get a number of times
            # we will run a next loop - 1 + 1
            for i in range(1500):
                if (int(decimal) - 16 ** i) * (int(decimal) - 16 ** (i + 1)) <= 0:
                    limit = i + 1
            for i in range(1, limit + 1):
            # this loop will run limit times
                if dec_number // 16 ** (limit - i) % 16 < 10:
                    lst = lst + [dec_number // 16 ** (limit - i) % 16]
                else:
                    for key, value in extra_letters.items():
                        if value == dec_number // 16 ** (limit - i) % 16:
                            lst = lst + [key]
            hexadecimal = ''.join(str(x) for x in lst)
            # calculating list of consecutive numbers in hex and than a string
            print('hexadecimal: ', hexadecimal)
            print('------------------------')
            return hexadecimal


#4
def hexadecimal_to_decimal(hexadecimal):
    print('------------------------')
    print('hexadecimal: ', hexadecimal)
    numbers_hexadecimal = ['1', '2', '3', '4', '5', '6', '7' ,'8' , '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
    extra_letters = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    if hexadecimal=='0':
        decimal = 0
        print('decimal: ', decimal)
        return decimal
    else:
        s = 0
        # for every elem of str hexadecimal check if every element is there is hexadecimal element,
        # if yes adding 1 to s and continue
        for n in hexadecimal:
            if n in numbers_hexadecimal:
                s = s + 1
                continue
            else:
                break
        if s < len(hexadecimal):
            print('incorrect input, not hexadecimal')
            return None
        else:
            decimal = 0
            for i in range(len(hexadecimal)):
                if hexadecimal[len(hexadecimal) - i - 1] in extra_letters.keys():
                    decimal = decimal + extra_letters[hexadecimal[len(hexadecimal) - i - 1]]*16 ** i
                else:
                    decimal = decimal + int(hexadecimal[len(hexadecimal) - i - 1])*16 ** i
            print('decimal: ', decimal)
            print('------------------------')
            return decimal

