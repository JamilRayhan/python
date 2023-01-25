# exception handling
try:
    age = int(input('Age: '))
    income = 102020
    risk = income / age
    print(age)
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('Age can not be zero')
