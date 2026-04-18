# --------------------Branching in Python
# if <condition>:
#   <code>          --will execute when conition above is True

# if <condition1>:
#   <code>          --will execute when condition1 is True
# else:             --will execute when condition1 is False
#   <code>

# if <condition1>:
#   <code>              --will execute when condition1 is True
# elif <condition2>:    --will execute when condition1 is False
#   <code>              --will execute when condition2 is True
# else:                 --will execute when condition1 & condition2 is False
#   <code>

# if <condition1>:
#   <code>              --will execute when condition1 is True
# elif <condition2>:    --will execute when condition1 is False
#   if <condition2a>:   --will execute when condition2 is True
#       <code>          --will execute when condition2a is True
# elif <condition3>:    --will execute when condition2 is False
#   <code>
# else:                 --will execute when all the conditions above is False
#   <code>

pset_time = 15
sleep_time = 8

if (pset_time + sleep_time) > 24:
    print("Impossible!")
elif (pset_time + sleep_time) >= 24:
    print("Full schedule!")
else:
    leftover = abs(24-pset_time-sleep_time)
    print(leftover, "h of free time")
print("End of day")
print()

x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: "))

if x == y:
    print(x, "is the same as", y)
elif x > y:
    print(x, "is bigger than", y)
else:
    print(x, "is smaller than", y)
print()

# -----------nested branching
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))

if x == y:  # main branch
    print("x and y are equal")
    if y != 0:  # nested branch
        print("therefore, x/y is", x/y)
elif x < y:  # main branch
    print("x is smller")
else:  # main branch
    print("y is smaller")
print("Thanks!")
