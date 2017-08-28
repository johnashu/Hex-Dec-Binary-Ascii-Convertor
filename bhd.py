#
# A Script i wrote to convert an 8 digit binary 'byte' into a number of the sum of the digits..
# I hope to expand this scxript to include hexadecimal codes from the binary..
#

import re #import the regular expression module..

n = "\n"
nl = n + '#' * 25 + n

# create binary tuples becausedr they cant be changed..

bin_display = """
#   0 :  0  :  0  :  0  :  0  :  0  : 0  :  0  = 0 (OFF)
#  128  64    32    16     8     4    2     1  = 1 (ON)
"""

binary = (input("INput an 8 DIGIT binary number:")) # Get The data from User Input
match = re.match('^[_0-1]{8}$', binary) # Regular Expression match matches only 0-1 numbers and has to be 8 ncharacters long, the $ stops it from accepting more than 8 characters//

while match == None:
        binary = (input("INput an 8 DIGIT binary number:"))
        match = re.match('^[_0-1]{8}$', binary)
else:
    print(n, n, "Your Inputted Binary Number Is:", n, n, binary, n, n)

# Ok so all is good with getting the input.. but now what?? where is it and how do we now convert the binary information into something more understandable??

# What do the binary numbers add up to to give the number of the byte?
# 10101010 from right to left will be 0 + 2 + 0 + 8 + 0 32 + 0 + 128 we will have to work from left to right to replace the numbers from the above tuples


binary_lst = [128, 64, 32, 16, 8, 4, 2, 1] # create a list. this is to do our coversions..

# assign the nubmers in the inputted list to letters so we can add them up at the end..
a = binary[0]
b = binary[1]
c = binary[2]
d = binary[3]
e = binary[4]
f = binary[5]
g = binary[6]
h = binary[7]

if binary[0] != "0": # if the position is NOT 0 
   a = 128 # the value of a will become 128
else: 
    a = 0  # if it is 0 it will stay 0, or become 0..

if binary[1] != "0": # if the position is NOT 0 
       b = 64 # the value of a will become 64
else:
    b = 0   # if it is 0 it will stay 0, or become 0..

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



print('Your Binary Converted Numbers are:', n, n, a,b,c,d,e,f,g,h) # print the new converted values for the letter relating to the original input

binary_num = a+b+c+d+e+f+g+h # the sum of the binary digits will give us out binary number...

print("\n\nThe sum of binary numbers is:\n", n, binary_num, n, n) # print

# now we want to  go from binary to hex

# create a table first

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

# print(hex1, hex2) # test to match them both.. 1 nibble is 4 bits, 2 nibbles is 1 hex
# print(binary)

#ok so here we go...

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


print('The Hex Code from the Binary number is:', n, n, hex1, hex2, n, n) #prints the hex  code
