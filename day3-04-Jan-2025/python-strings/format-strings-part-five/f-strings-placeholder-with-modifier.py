"""
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f 
which means fixed point number with 2 decimals:
"""
price = 1000
pricePlaceholderWithModifier = f'The price is {price:.2f} INR'
pricePlaceholderWithModifier1 = f'The price is {price:.4f} INR'
pricePlaceholderWithModifier2 = f'The price is {price:.1f} INR'
print(pricePlaceholderWithModifier)
print(pricePlaceholderWithModifier1)

print(pricePlaceholderWithModifier2)
