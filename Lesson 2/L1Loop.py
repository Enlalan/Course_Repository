# loop over string, Guess-and-check, and Binary

# ----------------------Break statement

# while <condition_1>:
#       while <condition_2>:
#               <expression_a> ----evaluated when <condition_1> & <cond_2 >is True
#               break
#               <expression_b> --- Never evaluated coz after command 'break'
#       <expression_c>          -----evaluated when <condition_1> is True
mysum = 0
for i in range(5, 11, 2):  # 5,7,9
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)
print()

# -----------------------string and loops

# A
s = "demo loops - fruit loops"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("Thre is an i or u")
print()

# B
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")
print()

# C
for char in s:
    if char in 'iu':
        print("There is an i or u")
print()

# all A,B anc C method give same result, just diff in simplisity
