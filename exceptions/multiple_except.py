try:
    age = int(input("Age: "))
    print(age)
    income = 20000
    risk = income/age # if age is 0 it gives  ZeroDivisionError
except ZeroDivisionError:
    print("Age can't be 0")
except ValueError:
    print("Invalid value")