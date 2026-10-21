# Practice Problem: Create a program that takes an integer and prints its multiplication table from 1 to 10.

user_number=int(input("Enter a number: "))
for number in range(1,11):
  product=number*user_number
  print(product)