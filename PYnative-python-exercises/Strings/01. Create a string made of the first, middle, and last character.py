# Practice Problem: Write a program to create a new string made of an input string’s first, middle, and last characters.

name=input("Enter a name: ")
first_char = name[0] 
middle_char_index = int(len(name)/2)
middle_char = name[middle_char_index]
last_char = name[-1]
new_string = first_char + middle_char + last_char
print(new_string)