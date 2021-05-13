import sys
import time
from Convertion.bin_to_dec import binary_to_decimal, decimal_to_binary, hexadecimal_to_decimal, decimal_to_hexadecimal

def main_menu():
    print('''    1. Decimal to binary 
    2. Binary to decimal 
    3. Decimal to hexadecimal 
    4. Hexadecimal to decimal 
    5. Exit \n''')

run = True

while run:

    print('**********************************')
    print('       Conversion calculator      ')
    print('              - MENU -            ')
    print('**********************************')
    main_menu()    # Displays menu
    conversion = int(input('Choose an option [1-5] \n'))
    conv_type = {1: "convert decimal to binary", 2: "convert binary to decimal", 3: "convert decimal to hexadecimal",
                 4: "convert hexadecimal to decimal", 5: "exit"}
    if conversion in conv_type.keys():
        print('''You have chosen to 
{}'''.format(conv_type[conversion]))

        if conversion == 1:
            number_to_convert = input('Enter decimal number to convert: ')
            decimal_to_binary(number_to_convert)
        elif conversion == 2:
            number_to_convert = input('Enter binary number to convert: ')
            binary_to_decimal(number_to_convert)
        elif conversion == 3:
            number_to_convert = input('Enter decimal to convert: ')
            decimal_to_hexadecimal(number_to_convert)
        elif conversion == 4:
            number_to_convert = input('Enter hexadecimal number to convert: ')
            hexadecimal_to_decimal(number_to_convert)
        elif conversion == 5:
            print('exiting.', end='')
            for i in range(1,27):
                time.sleep(2/i)
                print('.', end = '')
            sys.exit()
    else:
        print('Incorrect entry, try again')

