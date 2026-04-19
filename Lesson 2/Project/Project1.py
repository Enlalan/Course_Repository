# write code that loops a for loop over some range
# and prints how many even numbers are in that range

# 1) range(5)
# 2) range(10)
# 3) range(2,9,3)
# 4) range(-4,6,2)
# 5) range(5,6)


even_count = 0
for i in range(5):  # i= 0,1,2,3,4
    if i % 2 == 0:  # % is devide
        even_count += 1
print(even_count)  # = 3
print()

even_count = 0
for i in range(10):  # i=0,1,2,3,4,5,6,7,8,9
    if i % 2 == 0:  # % is devide
        even_count += 1
print(even_count)  # = 5
print()

even_count = 0
for i in range(2, 9, 3):  # i=2,5,8
    if i % 2 == 0:  # % is devide
        even_count += 1
print(even_count)  # = 2
print()

even_count = 0
for i in range(-4, 6, 2):  # i=-4,-2,0,2,4
    if i % 2 == 0:  # % is
        even_count += 1
print(even_count)
print()

even_count = 0
for i in range(5, 6):  # 5
    if i % 2 == 0:  # % is devide
        even_count += 1
print(even_count)  # = 0
print()
