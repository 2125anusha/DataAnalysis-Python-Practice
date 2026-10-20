# Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

number1=int(input("Enter the 1st number: "))
number2=int(input("Enter the 2nd number: "))
def calculate(num1,num2):
  product=number1*number2
  sum=number1+number2
  if  product<=1000:
    return product
  else:
    return sum

result=calculate(number1,number2)
print(f'The result is {result}')
