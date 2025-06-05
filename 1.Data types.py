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

int = 5
float = 5.1
str = 'fmr4o3fowpffm'
str3 = '''jsa99sd0k'''
bool_T = True
bool_F = False
None_type_var = None

print(int, ' - ', type(int))
print(float, ' - ', type(float))
print(str, ' - ', type(str))
print(str3, ' - ', type(str3))
print(bool_T, ' - ', type(bool_T))
print(bool_F, ' - ', type(bool_F))
print(None_type_var, ' - ', type(None_type_var))

# 5  -  <class 'int'>
# 5.1  -  <class 'float'>        
# fmr4o3fowpffm  -  <class 'str'>
# jsa99sd0k  -  <class 'str'>    
# True  -  <class 'bool'>
# False  -  <class 'bool'>
# None  -  <class 'NoneType'>



