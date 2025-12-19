user_input = input("Enter a number or character: ")

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = "abcdefghijklmnopqrstuvwxyz"
n = "0123456789"
c = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"

if user_input in A:
    print("You entered an uppercase letter.")

elif user_input in a:
    print("You entered a lowercase letter.")

elif user_input in n:
    print("You entered a number.")

elif user_input in c:
    print("You entered a special character.")
else :
    print("Input not recognized. Or it may be more than one character.")

