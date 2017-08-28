import re

bin_display = """
#   0 :  0  :  0  :  0  :  0  :  0  : 0  :  0  = 0 (OFF)
#  128  64    32    16     8     4    2     1  = 1 (ON)
"""

binary_string = '0110100100100000010000010110110100100000010000010010000001000111011100100110010101100001011101000010000001000100011000010110010000100001001000010010000000100000010010010010000001001100011011110111011001100101001000000101000001111001011101000110100001101111011011100010000100100001'  # "010001000100000101000100" # Reads DAD


h = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
     '8': '8', '9': '9', 'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}

b = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
     '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}


binary_lst = [128, 64, 32, 16, 8, 4, 2, 1]


def n():
    print("\n")


def nl():
    banner = '#' * 50
    print(banner)

hex_string = '3KA'
nl()
bin_match = re.match('^[_0-1]$', binary_string)
hex_match = re.match('^[0-9][A-F]?$', hex_string)

try:
    if hex_match:
        print('Hex Matches')
except ValueError:
    print('Hex Does Not Match')

def bin2hex(binary):
    try:
        bin_match
        """ Converts Binary to HExaDEcimal"""
        binary_split1 = (binary[0:4])
        binary_split2 = (binary[4:8])

        hex1 = b[binary_split1]
        hex2 = b[binary_split2]

        return str(hex1) + str(hex2)
    except (KeyError, TypeError, ValueError):
        print("Must be a binary string consisting of only 0s and 1s")


def split_string(string, length):
    """ function to split a string into differnt lengths or chunks"""
    return [string[max(i - length, 0):i] for i in range(len(string), 0, -length)][::-1]


def hex2integer(hex_string_input):
    """ convert from hex string to integers"""

    hex_match = re.match('^[0-9][A-F]?$', hex_string_input[0])
    hex1 = h[hex_string_input[0]]
    hex2 = h[hex_string_input[1]]

    return [str(hex1), str(hex2)]


def hex_int_to_dec(hex1, hex2):
    """ calculates a 2 digit hexadecimal to normal decimal """
    current_digit = int(hex1)
    current_digit1 = int(hex2)
    power = 1
    power1 = 0

    hex_iter = []

    if hex1:
        mul_dig = current_digit * (16 ** power)
        hex_iter.append(mul_dig)

    if hex2:
        mul_dig = current_digit1 * (16 ** power1)
        hex_iter.append(mul_dig)

    return sum(hex_iter)


def decimal2character(decimal_num):
    """ converts a decimal number to an ASCII character """
    return chr(decimal_num)


def run_the_show():
    rtn_bin_split = split_string(binary_string, 8)
    hex_string = [(bin2hex(item)) for item in rtn_bin_split]
    hex_integers = [hex2integer(item) for item in hex_string]
    hex_full_dec = [hex_int_to_dec(item[0], item[1]) for item in hex_integers]
    ascii_msg = [decimal2character(item) for item in hex_full_dec]
    print(''.join(map(str, ascii_msg)))


run_the_show()
nl()
