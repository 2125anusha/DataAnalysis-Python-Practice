# Practice Problem: Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1.

user_number = int(input("Enter a number: "))
for number in range(1,user_number+1):
  cube = number**3
  print(f"Current Number is : {number} and the cube is {cube}")