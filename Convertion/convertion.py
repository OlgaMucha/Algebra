import sys
import time
from Convertion.bin_to_dec import binary_to_decimal, decimal_to_binary, hexidecimal_to_decimal, decimal_to_hexidecimal


def main_menu():
    global conversion
    conversion = int(input('''Choose a conversion:
    1. Decimal to binary 
    2. Binary to decimal 
    3. Decimal to hexadecimal 
    4. Hexadecimal to decimal 
    5. Exit \n'''))
    return conversion


print('**********************************')
print('     Conversion - main menu       ')
print('**********************************')
main_menu()
print('**********************************')

conv_type = {1: "convert decimal to binary", 2: "convert binary to decimal", 3: "convert decimal to hexadecimal",
             4: "convert hexadecimal to decimal", 5: "exit"}
if conversion in conv_type.keys():
    print('''You have chosen to 
{}'''.format(conv_type[conversion]))
    print('**********************************')

    if conversion == 1:
        number_to_convert = input('Enter decimal number to convert: \n')
        decimal_to_binary(number_to_convert)
        print('**********************************')
        print('back to main menu...')
        main_menu()
    elif conversion == 2:
        number_to_convert = input('Enter binary number to convert: \n')
        binary_to_decimal(number_to_convert)
        print('**********************************')
        main_menu()
    elif conversion == 3:
        number_to_convert = input('Enter decimal to convert: \n')
        decimal_to_hexidecimal(number_to_convert)
        print('**********************************')
        main_menu()
    elif conversion == 4:
        number_to_convert = input('Enter hexadecimal number to convert: \n')
        hexidecimal_to_decimal(number_to_convert)
        print('**********************************')
        main_menu()
    elif conversion == 5:
        print('exiting.', end='')
        for i in range(1,27):
            time.sleep(2/i)
            print('.', end = '')
        sys.exit()
else:
    print('Incorrect entry, try again')
    main_menu()
