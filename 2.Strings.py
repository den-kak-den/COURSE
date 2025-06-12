# string is UNmutable object. Adding any new elements to string will create NEW string with NEW id!!!

# a = "12345"
# print(a, id(a))

# a += '6'
# print(a, id(a))

# 12345 1784138929120
# 123456 1784138935264

######################################

# '''.....''' using to add many values of text to variable

# string = "asjdlfksjdfllsdjf
# sdfsdfasdfsfds
# sdafsadfsdfdsf
# dsafdsafsadfdsf"

#return ERROR, but

# string = '''sadgfadgsdfsdkfj
# idsfkahkdfhdsakfhf
# shdafsakdjfkdsljfls
# safdabsdkfskjdfnjf'''

# # working correctly

# print(string) 

# sadgfadgsdfsdkfj
# idsfkahkdfhdsakfhf
# shdafsakdjfkdsljfls
# safdabsdkfskjdfnjf

################################

# num = 12345
# print(num, type(num))

# str = str(num)
# print(str, type(str))

# 12345 <class 'int'>
# 12345 <class 'str'>

###################

# CONCATENATION OF STRINGS

# str1 = "12345"
# str2 = "skdhflksjd"

# print(str1 + str2)
# print(str1 + " " + str2)

# 12345skdhflksjd
# 12345 skdhflksjd

# MULTIPLICATION OF STRINGS

# str = '12345'
# print(str * 3)
# print((str + " ") * 3)

# 123451234512345
# 12345 12345 12345 

############################################

# LENGTH OF STRING

# str = '''hsadifhisdhifhdsoifsay7d8f7sav9ysay9sd7f9sdf79s7df98sf
# sa8df76sdf798s7f7d97f9as78f6d87s8698d97f986sa86f8s6df
# s7vusafijjf9u8jeoij984wjnic4hj9fdos4jf0sif4n094nf09
# fi3qhfjn94hfjqw4fh04jfj409fjqfjfj04jf
# '''
# print(len(str))

# 199

##############################################################

# SLICES (СРЕЗЫ -- извлечение из строки фрагмента )

# str = "Hello, World"
# for index, value in enumerate(str):
#     print(index, value)
    
# index, value, enumerate(str) -- служебные ссылки на данные в теле цикла for

# 0 H
# 1 e
# 2 l
# 3 l
# 4 o
# 5 ,
# 6
# 7 W
# 8 o
# 9 r
# 10 l
# 11 d

# print(str[1])  # e
# print(str[:3])  # Hel
# print(str[1:4]) # ell 1st symbol INCLUDE, 4th symbol NOT include !!!
# print(str[-2:-6])  # empty output
# print(str[-5:-3])  # Wo
# print(str[::2])  # Hlo ol

