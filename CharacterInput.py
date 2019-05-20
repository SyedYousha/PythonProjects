#Project from practicepython.org

name = input('Please enter your name: ')

age = int(input('Please enter your age: ')) #Need to declare the int 
#because you will be changing the value to a string later.

year = str((2019 - age) + 100) #Declared string here because you're 
#converting from a integer to a string value.

print('Hello,', name,', you are', age, 'years old! In the year', year,
'you will be 100 years old!' )