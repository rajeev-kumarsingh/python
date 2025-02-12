# if-else in placeholder

price = int(input("Kindly enter the price: "))
result = f"It is very {'Expensive' if price>=100 else 'Cheap'} "
print(result)
