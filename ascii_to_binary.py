
def nl():
    banner = '#' * 50
    print(banner)


nl()

ascii_string = "Hello My Name Is John. I Love Programming in PYTHON!"

b = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
     '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

h = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
     '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

h1 = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
      '8': '8', '9': '9', '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}


def split_string(string, length):
    """ function to split a string into differnt lengths or chunks"""
    return [string[max(i - length, 0):i] for i in range(len(string), 0, -length)][::-1]

def ascii2decimal(string):
    """ converts an ASCII character to a decimal """
    return ord(string)


def decimal2hex(dividend):
    """ converts a decimal to a hexadecimal """
    quotient = dividend // 16
    remainder = dividend - (quotient * 16)
    hex1 = str(remainder)
    hex1 = h1[hex1]

    quotient1 = quotient // 16
    remainder1 = quotient - (quotient1 * 16)
    hex2 = str(remainder1)
    hex2 = h1[hex2]

    return str(hex2) + str(hex1)


def hex2binary(hex_num):
    """ converts from hexadecimal to binary """
    hex1 = h[hex_num[0]]
    hex2 = h[hex_num[1]]

    return str(hex1) + str(hex2)


def run_the_show():
    decimal_msg = [ascii2decimal(char) for char in ascii_string]
    dec_to_hex = [decimal2hex(item) for item in decimal_msg]
    hex_to_bin = [hex2binary(item) for item in dec_to_hex]
    print(' '.join(map(str, hex_to_bin)))

run_the_show()

nl()
