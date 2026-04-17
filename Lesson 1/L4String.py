# learn len, slice, escape character, format, concantenate

# use of triple qoute : string yg banyak line atau paragraph
message = """
Hi John'
Today i missed the meeting.
Lets rearrange.

Regards
Matt

"""
print(message)
print()

course = "Python Programming"
# ------len() return no of character/length of string/name/variable
print(len(course))  # =18

# ------slice [Start:Stop:Step] : to return specific character
# positif step : read from left to right
# negatif Step ; read from right to left
# "Python Programming"
#  01234567891011121314151617
print(course[0])  # = P : return 1st index letter
print(course[-1])  # = g : return the last letter
print(course[0:3])  # =Pyt : return 3 letter fr start ie:index 0 ,t
print(course[0:])  # =Python Programming
# return letter start indx 0 & stop at indx 0
print(course[:3])  # =Pyt : same as course[0:3]
print(course[:])  # =Python Programming
print(course[:3:-1])  # = gnimmargorP no
print(course[len(course)-1])  # = g
print(course[3:len(course)-1])  # = hon Programmin
print(course[4:0:-1])  # ohty

print()

# -----------------------Escape character
# \"
# \'
# \\
# \n = print at new line
course = "Python \"Programming"
print(course)  # = Python "Programming
course = "Python \'Programming"
print(course)  # = Python 'Programming
course = "Python \\Programming"
print(course)  # = Python \Programming
course = "Python \nProgramming"
print(course)  # = Python
#                  Programming
print()

# ------------------------F String

first = "Ahmad"
last = "Faizal"
full = first + " " + last
print(full)  # Ahmad Faizal
# using format f or called f string
# must bracketed by curly braces {}
full = f"{first} {last}"
print(full)  # Ahmad Faizal
full = f"{len(first)} {last}"
print(full)  # 5 Faizal
full = f"{len(first)} {3 + 3}"
print(full)  # 5 6

# ---------------------conchantenate
a = "The"
b = 3
c = "Musketeers"
all = f"{a} {b} {c}"
print(all)  # = The 3 Musketeers

all = a+str(b)+c
# all = a + b + c will result error coz concantenate only string not int
print(all)  # =The3Musketeers : not the diff of using f"{}

all = a, b, c
print(all)  # = ('The', 3, 'Musketeers')
# , in print will return as space
print(a, b, c)  # = The 3 Musketeers
print()

num = 3000
fraction = 1/3
print(num*fraction, "is", fraction*100, "% of", num)
print(num*fraction, "is", str(fraction*100) + "% of", num)
print(f"{num*fraction} is {fraction*100} % of {num}")
