# learn about input

# name = input("What is your name? ")
# print(name + ", such a nice name you have.")
print()
# place = input("Where you are from? ")
# print("I see, you come from", place + ", what a beautiful place!")
# print((place + " ")*4 + place)
print()

# input always return as str unless define as int

# num1 = input("Type a number: ")
# print(num1*5)  # if enter 2; return =22222
# num2 = int(input("Type a number: "))
# print(num2*5)  # if enter 2; return=10

# Try Newton Raphson for cube root
x = int(input("What x to find the cube root of? "))
g = int(input("What guess to start with? "))
print("Current estimate cubed =", g**3)

next_g = g-((g**3 - x)/(3*g**2))
print("Next guess to try =", next_g)
