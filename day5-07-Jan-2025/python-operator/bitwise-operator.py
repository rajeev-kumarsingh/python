"""
Python Bitwise Operator: &, |, ^, ~, <<, >>
Bitwise operators are used to compare (binary) numbers
"""
print(6 & 3) # & 	Name-AND	Sets each bit to 1 if both bits are 1
print(6 | 3) # |	Name-OR	Sets each bit to 1 if one of two bits is 1
print(6 ^ 3) # ^  Name-XOR	Sets each bit to 1 if only one of two bits is 1
print( ~ 3)  # ~  Name- NOT	Inverts all the bits
print(3 << 2) 
"""<<	Name-Zero fill left shift	
      hift left by pushing zeros in from the right and let the leftmost bits fall off"""
print(8 >> 2)
"""
>> Name- Signed Right Shift
Description: Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""