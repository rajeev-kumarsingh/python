"""
Operator Precedance: Operator precedence describes the order in which operations are performed.
BODMAS
"""
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6+3) * (4*5))
#Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
print(6 / 3 + 2 * 5 -10 )

print(5 + 4 - 7 + 3)
#Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

