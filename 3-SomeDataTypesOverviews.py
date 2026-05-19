#--------------------
#type()
#all data in Python is an object, and every object has a type. The type() function is used to determine the type of an object.
#--------------------
print(type(10))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>
print(type("Hello, World!"))  # Output: <class 'str'>
print(type(True))  # Output: <class 'bool'>
print(type(None))  # Output: <class 'NoneType'>         
print(type([1, 2, 3]))  # Output: <class 'list'>
print(type((1, 2, 3)))  # Output: <class 'tuple'>
print(type({'name': 'Alice', 'age': 30}))  # Output: <class 'dict'>
print(type({1, 2, 3}))  # Output: <class 'set'>
print(type(10))  # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(100.9))  # float => Floating Point Number
print(type(1.950950))  # float => Floating Point Number
print(type(-100.9595))  # float => Floating Point Number

print(type("Hello Python"))  # str => String

print(type([1, 2, 3, 4, 5]))  # list => List

print(type((1, 2, 3, 4, 5)))  # tuple => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary

print(type(2 == 2))  # bool => Boolean
print(type(2 > 3))  # bool => Boolean