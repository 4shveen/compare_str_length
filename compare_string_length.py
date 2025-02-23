'''String Length Comparison
Prompt the user to enter two strings. Write a Python program to compare the lengths of the two strings
and print a message indicating which string is longer, or if they are of equal length.'''
from colorama import Fore,Style
# Let the user know about the purpose of the program.
print(Fore.YELLOW+"This program serves to compare the lengths of two strings that you have to input."+Style.RESET_ALL)

# Take first and second strings from the user
string_1 = input("Enter the first string: ")
string_2 = input("Enter the second string: ")

# Compare the lengths of the two strings
length_1 = len(string_1)
length_2 = len(string_2)

# Display 
if length_1 == length_2 :
    print("Both strings are of the same length.")

elif length_1 > length_2 :
    print("The first string entered is the longer of the two.")

else :
    print("The second string entered is the longer of the two.")

print("\033[1;31mThank you for using this app.\033[0m")
print("bye")