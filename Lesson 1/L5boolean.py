
# ---------comparison operators
# i > j
# i >= j
# i < j
# i <= j
# i == j ---> equality test, True if i is the same as j
# i != j ---> inequality test, True if i not the same as j
# case sensitive with string

# ----------Logical operators on Bool
#       A       B        A and B         A or B
#      True    True       True            True
#      True    False      False           True
#      False   True       False           True
#      False   False      False           False

# a and b --> True if both are True
# a or b ---> False if both are False
# not a ---> True if a is False
#            False if a is True

"a" == "A"  # False
(2 < 3)  # True
not (2 < 3)  # False
(2 < 3) and (3 < 4)  # True
(2 < 3) and (3 > 4)  # False

pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)  # False
derive = True
drink = False
both = drink and derive
print(both)  # False
print()

secret_num = 5
guess_num = int(input("Guess the secrete number: "))

if secret_num == guess_num:
    print("You guess right!")
    if guess_num != 0:
        print("Therefore secret num / guess num is:", secret_num/guess_num)
elif guess_num > secret_num:
    print("You guess higher")
else:
    print("You guess lower")
print("Thanks")


# if something is True, do this, otherwise do that
