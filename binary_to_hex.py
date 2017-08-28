import re #import the regular expression module..

# create binary tabel

bin_display = """
#   0 :  0  :  0  :  0  :  0  :  0  : 0  :  0  = 0 (OFF)
#  128  64    32    16     8     4    2     1  = 1 (ON)
"""
binary_string =  '010001000100000101000100'   #"010001000100000101000100" # Reads DAD


n = "\n"
nl = n + '#' * 25 + n

def bin2hex(binary):
    
    match = re.match('^[_0-1]{8}$', binary) # Regular Expression match matches only 0-1 numbers and has to be 8 ncharacters long, the $ stops it from accepting more than 8 

    binary_lst = [128, 64, 32, 16, 8, 4, 2, 1] 

    # assign the nubmers in the inputted list to letters so we can add them up at the end..
    a = binary[0]
    b = binary[1]
    c = binary[2]
    d = binary[3]
    e = binary[4]
    f = binary[5]
    g = binary[6]
    h = binary[7]

    if binary[0] != "0": 
        a = 128 
    else: 
        a = 0  

    if binary[1] != "0":
        b = 64 
    else:
        b = 0 

    if binary[2] != "0":
        c = 32
    else:
        c = 0 

    if binary[3] != "0":
        d = 16
    else:
        d = 0 
    if binary[4] != "0":
        e = 8
    else:
        e = 0 
    if binary[5] != "0":
        f = 4
    else:
        f = 0 
    if binary[6] != "0":
        g = 2
    else:
        g = 0 
    if binary[7] != "0":
        h = 1
    else:
        h = 0 


    binary_num = a+b+c+d+e+f+g+h # the sum of the binary digits will give us out binary number...

    h0 = "0000"
    h1 = "0001"
    h2 = "0010"
    h3 = "0011"
    h4 = "0100"
    h5 = "0101"
    h6 = "0110" 
    h7 = "0111" 
    h8 = "1000"
    h9 = "1001"
    ha = "1010"
    hb = "1011"
    hc = "1100"
    hd = "1101"
    he = "1110"
    hf = "1111"

    hex1 = binary[0:4] # the first letter/number is calculated from the 1st 4 digits in the binary code ( called a nibble, 4 bits)
    hex2 = binary[4:8] # the second letter/number is calculated from the 2nd 4 digits in the binary code. ( called a nibble, 4 bits)

    if hex1 == h0: # if hex 1 is the same as h0
        hex1 = 0 # then hex1 is equal to 0
    elif hex1 == h1:
        hex1 = 1
    elif hex1 == h2:
        hex1 = 2
    elif hex1 == h3:
        hex1 = 3
    elif hex1 == h4:
        hex1 = 4
    elif hex1 == h5:
        hex1 = 5
    elif hex1 == h6:
        hex1 = 6
    elif hex1 == h7:
        hex1 = 7
    elif hex1 == h8:
        hex1 = 8
    elif hex1 == h9:
        hex1 = 9
    elif hex1 == ha:
        hex1 = "A"        
    elif hex1 == hb:
        hex1 = "B"   
    elif hex1 == hc:
        hex1 = "C"                          
    elif hex1 == hd:
        hex1 = "D"
    elif hex1 == he:
        hex1 = "E"   
    elif hex1 == hf:
        hex1 = "F"   
            
    # same again for hex2

    if hex2 == h0:
        hex2 = 0
    elif hex2 == h1:
        hex2 = 1
    elif hex2 == h2:
        hex2 = 2
    elif hex2 == h3:
        hex2 = 3
    elif hex2 == h4:
        hex2 = 4
    elif hex2 == h5:
        hex2 = 5
    elif hex2 == h6:
        hex2 = 6
    elif hex2 == h7:
        hex2 = 7
    elif hex2 == h8:
        hex2 = 8
    elif hex2 == h9:
        hex2 = 9
    elif hex2 == ha:
        hex2 = "A"        
    elif hex2 == hb:
        hex2 = "B"   
    elif hex2 == hc:
        hex2 = "C"                          
    elif hex2 == hd:
        hex2 = "D"
    elif hex2 == he:
        hex2 = "E"   
    elif hex2 == hf:
        hex2 = "F"  


    return str(hex1) + str(hex2)


def split_string(string, length):
        """ function to split a string into differnt lengths or chunks"""
        return [string[max(i-length,0):i] for i in range(len(string), 0, -length)][::-1]

rtn_bin_split = split_string(binary_string, 8)


for item in rtn_bin_split:
    print(bin2hex(item))




