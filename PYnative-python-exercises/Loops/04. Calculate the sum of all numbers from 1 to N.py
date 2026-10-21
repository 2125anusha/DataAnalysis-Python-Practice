# Practice Problem: Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.

sum=0
input_range=int(input("Enter a number: "))
for numbers in range(1,input_range+1):
  sum+=numbers
print(f"Sum is: {sum}")