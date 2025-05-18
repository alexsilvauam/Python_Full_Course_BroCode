#typecasting = converting one data type to another, can be str, int, float, or bool

name = "Bro"
age = 20
height = 5.9
is_student = True

type(name)

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(is_student)) # <class 'bool'>

age = float(age)
print(type(age)) # <class 'float'>

age = int(age)
age = str(age)
print(type(age)) # <class 'str'>