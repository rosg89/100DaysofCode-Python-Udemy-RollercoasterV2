print("Welcome to the rollercoaster!")

#Convierte el input de String a Int
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster! =)")
  age = int(input("What is your age?"))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
  print("Sorry, you have to grow taller before you can ride =(")

#Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to