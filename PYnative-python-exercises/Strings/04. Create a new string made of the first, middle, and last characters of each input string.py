# Practice Problem: Given two strings, s1 and s2, create a new string from the first, middle, and last characters of each input string.

n1=input("Enter a name: ")
n2=input("Enter another name: ")

first_char_n1 = n1[0]
first_char_n2 = n2[0]
mid_char_n1 = n1[int(len(n1)/2)]
mid_char_n2 = n2[int(len(n2)/2)]
last_char_n1 = n1[-1]
last_char_n2 = n2[-1]
new_name = first_char_n1 + first_char_n2 + mid_char_n1 + mid_char_n2 + last_char_n1 + last_char_n2
print(new_name)