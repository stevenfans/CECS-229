# Steven Phan
# CECS 229 - Fall 2019
# Programing Assignment #1

# 1. Write a Python expression to find the number of seconds ina century. You can assume one year has 365 days. Save the
#    value to a variable called seconds_in_century. Then print it.
years_in_century = 100
days_in_year = 365
hours_in_day = 24
mins_in_hour = 60
secs_in_min = 60

seconds_in_century = years_in_century * days_in_year * hours_in_day * mins_in_hour * secs_in_min
# print("#1. seconds_in_century:%i" %seconds_in_century)

# 2. Write a Python expression to find the remainder of 5789248 divided by 6 by using Python's modulus operator. Save
#    the value to a variable called remainder_with_mod. Then print it.

remainder_with_mod = 5789248 % 6
# print("remainder_with_mod = %i" %remainder_with_mod)

# 3. Write a Python expression to find the remainder of 5789248 divided by 6 without using Python's modulus operator.
#    Instead,  you must use the floor division (//) operator. Save the value to a variable called remainder_without_mod.
#    Print the result.
quotient = 5789248 // 6
remainder_without_mod = 5789248 - (quotient * 6)
# print("remainder_without_mod = %i" %remainder_without_mod)

# 4. Write a comprehension over {1,3,5,7,11} whose value is the set consisting of their fourth power minus 2.
#    Print the result.
list = []
for num in range(0,12):
    if num%2 is not 0 and num != 9:
        temp = num**4 - 2
        list.append(temp)
 print(list)

# 5. Write a comprehension over [11, -2, 8, 15, 22] whose value is the list consisting of the cube minus the value's
#    index. Assume that the index starts at zero and assign variable M to be the list [11, -2, 8, 15, 22]. Print
#    the results.
M = [11, -2, 8, 15, 22]
new_list = []
for num in range(len(M)):
    ans= M[num]**3 - num
    new_list.append(ans)

print("#5. New M list:", new_list)

# 6. Write a Python expression that will give the intersection of the following two sets:
#    First Set: the cube of numbers from 1 to 30
#    Second Set: the tripling of number from 1 to 30
#
#    Then print the resulting set.
#    You cannot manually write out the numbers from 1 to 30, you must use a built-in Python function that will do
#    that for you.
first_set = set()
seconds_set = set()

for i in range(1,31):
    cube = i**3
    triple = i * 3
    first_set.add(cube)
    seconds_set.add(triple)

intersected_set = first_set.intersection(seconds_set)
print("#6. intersected set is:",intersected_set)



