# learm while loop

# while <condition>:
#       <code>  ---- will execute if the condition is True
# after run <code> it will check <condition> again
# it will repeat u ntil <condition> is False
# if <condition> is never False, then it will loop forever!
# to stop infinite loop, click the shell and hit CTRL+c

where = input("You're in the Lost Forest. Go left or right? ")
n = 0
m = 0
while where == "right" and n < 4:
    m = m+1
    if m > 2:
        print(":(")
    where = input("You're still in the Lost Forest. Go left or right? ")
    n = n+1
print("You got out of the Lost Forest!")
print()
# ------------ go stop infinite loop
# eg to stop loop after run 3 times
n = 0
while n < 3:
    print(n)
    n = n+1  # the same as n+=1
print()
# shortcut with for loop
n = 0
for n in range(3):  # range(3) means sequence of no from 0,1,2
    print(n)
print()

# Find 4
x = 4
i = 1  # loop variable
factorial = 1
while i <= x:
    factorial *= i  # same as factorial = factorial*i
    i += 1  # same as i=i+1
print(f'{x} factorial is {factorial}')
