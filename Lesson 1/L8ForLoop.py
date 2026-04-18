# ------------range

# range(start, stop, step) sama macam slicing
# often omit/tinggalkan start and step
# eg: for i in range(5):  ---> same as for i in range(0,5,1) = 0,1,2,3,4
#      - start default is 0
#      - step default is 1
# eg: for i in range(3,5): ----> same as write range(3,5,1) =3,4
#      - step default as 1
#  eg: range(1,4,1) = 1,2,3
# eg: range(1,4,2) = 1,3
# eg: range(4,0,-1) = 4,3,2,1

mysum = 0
for i in range(10):
    mysum += i  # same as mysum = mysum + i
print(mysum)  # 0+1+2+3+4+5+6+7+8+9= 45
print()


# -----------while loop vs for loop
# factorial  uses while loop
x = 4
i = 1  # loop variable
factorial = 1
while i <= x:
    factorial *= i  # same as factorial = factorial*i
    i += 1  # same as i=i+1
print(f'{x} factorial is {factorial}')  # = 4 factorial is 24

# factorial uses for loop
x = 4
factorial = 1
for i in range(1, x+1, 1):
    factorial *= i
print(f'{x} factorial is {factorial}')  # = 4 factorial is 24

# while loop, loops as long as condition is True.
# for loop, loop over range of numbers.
# for loop usefull for known number of loop to repeat.
# while loop usefull when not known how many of loop to repeat.
