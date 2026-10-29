# Practice Problem: Write a program to create a new string made of the middle three characters of an input string of odd length.

name=input("Enter a name: ")
middle_char_index = int(len(name)/2)
middle_3_chars = name[middle_char_index-1 : middle_char_index+2]
print(middle_3_chars)