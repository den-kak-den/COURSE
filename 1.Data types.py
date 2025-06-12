# var = 1
# print(var)
# print(type(var))        #тип данных
# print(id(var))          #адрес объекта в памяти. Адрес уникален и неизменен в течение всей жизни объекта

# #ИСКЛЮЧЕНИЕ! если разным переменным присваивается одинаковое число, то ИД этих переменных будет одним. Значение будет храниться в одной ячейке памяти, а разные переменные будут просто на него ссылаться

# a = 5
# b = 5

# print(id(a))
# print(id(b)) 

# b = b + 1

# print(id(b))        #А вот сейчас адрес переменной Б изменился

# int = 5
# float = 5.1
# str = 'fmr4o3fowpffm'
# str3 = '''jsa99sd0k'''
# bool_T = True
# bool_F = False
# None_type_var = None

# print(int, ' - ', type(int))
# print(float, ' - ', type(float))
# print(str, ' - ', type(str))
# print(str3, ' - ', type(str3))
# print(bool_T, ' - ', type(bool_T))
# print(bool_F, ' - ', type(bool_F))
# print(None_type_var, ' - ', type(None_type_var))

# 5  -  <class 'int'>
# 5.1  -  <class 'float'>        
# fmr4o3fowpffm  -  <class 'str'>
# jsa99sd0k  -  <class 'str'>    
# True  -  <class 'bool'>
# False  -  <class 'bool'>
# None  -  <class 'NoneType'>


# DINAMIC TYPING

# var = 45

# print(type(var))

# var = 'dfdsdlfj'

# print(type(var))

# <class 'int'>
# <class 'str'>


# user_mess = input('Write your message here: ')
# print(user_mess, type(user_mess))

# # Write your message here: 12331241
# # 12331241 <class 'str'>  # !!!!!!!!!!!111

# user_mess = int(input('Write your message here: '))
# print(user_mess, type(user_mess))

# user_mess = float(input('Write your message here: '))
# print(user_mess, type(user_mess))

# user_mess = bool(input('Write your message here: '))
# print(user_mess, type(user_mess))

# user_mess = None(input('Write your message here: ')) # !!!!! Object with class None cannot be called !!! 
# print(user_mess, type(user_mess))

# Write your message here: 2134324134
# 2134324134 <class 'int'>
# Write your message here: 132323
# 132323.0 <class 'float'>
# Write your message here: 2132313
# True <class 'bool'>
# Write your message here: 12312312
# Traceback (most recent call last):
#   File "f:\IT\Python\COURSE\1.Data types.py", line 72, in <module>
#     user_mess = None(input('Write your message here: ')) # !!!!! Object with class None cannot be called !!!
#                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: 'NoneType' object is not callable

# !!!! String cannot be converted to int of float

# user_mess = int(input('Write your message here: '))
# print(user_mess, type(user_mess))

# ERROR !

#####################################################

# OUTPUT FORMATTING

# str1 = 'first'
# str2 = 'second'

# # print(str1, str2, sep='\n')

# # # first
# # # second

# print(str1, '324923749', end=' new output ending ')
# print(str2, '2143213123')
# print('12412342')

# first 324923749 new output ending second 2143213123
# 12412342

#####################################################

# import math  #import all lib with all methods

# s = math.radians(x) # call to method

# from random import randint, uniform # import only some methods from lib.

# s = randint(x) # call to method



