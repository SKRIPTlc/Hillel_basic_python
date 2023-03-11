name = input("Enter your name: ")
age = input("Enter your age: ")

try:
    age = int(age)
except ValueError:
    print('Error, repeat input')
try:
    name = str(name)
except ValueError:
    print('Error, repeat input')
else:
    if age <= 0:
        print('Error, repeat input')
    elif age < 10:
        print(f'Hello,child {name}!')
    elif age <= 18:
        print(f'How are you, {name}?')
    elif age < 100:
        print(f'What do you want, {name}?')
    else:
        print(f'{name}, you lie - people do not live so long!')
