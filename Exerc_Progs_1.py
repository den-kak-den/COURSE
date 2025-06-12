#1. 

# int_1 = input("Input 1st int number: ")
# int_2 = input("Input 2nd int number: ")
# string = input("Input string: ")
# float = input("Input float number: ")

# print(int_1)
# print(int_2)
# print(string)
# print(float)

# Input 1st int number: 1
# Input 2nd int number: 4
# Input string: fdsafsdf
# Input float number: 131,5
# 1
# 4
# fdsafsdf
# 131,5 

####################################################

#2. 

# all_money = 11
# bread_cost = 1.5
# bread_number = 3

# money_balance = all_money - bread_cost * bread_number

# print(money_balance)

# 6.5

#######################################################

#3. Calculate the average age of students in the group

# stud_number = int(input("Input number of students: "))
# stud_cont = range(stud_number)
# ages_summ = 0
# for student in stud_cont:
#     age = int(input(f"Input the student's {student + 1} age: "))
#     ages_summ += age

# average_age = ages_summ / stud_number

# print(average_age)

# Input number of students: 3
# Input the student's 1 age: 20
# Input the student's 2 age: 30
# Input the student's 3 age: 40
# 30.0

############################################################

#4. Create the program for converting degrees to radians

# import math

# degrees = 1
# while degrees != 0:
#     degrees = float(input("Input value in degrees: "))
#     if degrees == 0:
#         print('Program exit')
#         break
#     else:    
#         radians = math.radians(degrees)

#         print(radians)

# Input value in degrees: 100
# 1.7453292519943295
# Input value in degrees: 57
# 0.9948376736367679
# Input value in degrees: 200
# 3.490658503988659
# Input value in degrees: 0
# Program exit

######################################################

#5. CALCULATE SUM OF DIGITS OF RANDOM 3-DIGIT NUMBER

# from random import randint

# number = randint(100, 999)
# print(f"выбрано число: {number}")

# sum_of_digits = (number // 100) + (number % 100 // 10) + (number % 10)

# print(sum_of_digits)

# prog working correctly

#####################################################

#6.

# anna_apples = 2
# paul_apples = 5

# print(f"Anna has {anna_apples} apples, Paul has {paul_apples} apples")

######################################################

#7.

# cube_edge = float(input("Input lenght of the cube edge: "))
# v_cube = cube_edge ** 3
# s_cube = cube_edge ** 2 * 6

# print(f"V of the cube = {v_cube}, S of the cube = {s_cube}")

# Input lenght of the cube edge: 2
# V of the cube = 8.0, S of the cube = 24.0

########################################################

#8.

# daily_path = 2
# nightly_path = 1
# tree_hight = 20
# all_path = 0
# days = 0

# while all_path < tree_hight:
#     all_path += daily_path
#     days += 1 
#     if all_path < tree_hight:
#         all_path -= nightly_path
#     else:
#         print(days)
#         break
            
# result = 19 days - correct

####################################################

#9.


