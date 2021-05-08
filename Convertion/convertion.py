from Convertion.bin_to_dec import binary_to_decimal, decimal_to_binary, hexidecimal_to_decimal, decimal_to_hexidecimal

print('***************************')
print('Number convertion')
print('***************************')

convertion = int(input('''Choose a convertion:
1. Decimal to binary 
2. Binary to decimal 
3. Decimal to hexidecimal 
4. Hexidecimal to decimal \n'''))

print('***************************')

conv_type = {1: "decimal to binary", 2:"binary to decimal", 3: "decimal to hexidecimal", 4: "hexidecimal to decimal"}
print('''You have chosen to convert: 
{}'''.format(conv_type[convertion]))
print('***************************')
number_to_convert = input('Enter number to convert: ')

if convertion == 1:
    decimal_to_binary(number_to_convert)
if convertion == 2:
    binary_to_decimal(number_to_convert)
if convertion == 3:
    decimal_to_hexidecimal(number_to_convert)
if convertion == 4:
    hexidecimal_to_decimal(number_to_convert)