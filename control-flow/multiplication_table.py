number = float(input("Enter a number to see its multiplication table:"))

for i in range(10):
  print(f"{int(number)} * {i+1} = {int(number * (i+1))}")