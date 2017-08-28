binary_int = '010001000100000101000100'
binary = binary_int

def split_string(string, length):
    """ function to split a string into differnt lengths or chunks"""
    return [binary[max(i-length,0):i] for i in range(len(binary), 0, -length)][::-1]

print(str(split_string(binary, 4)))

