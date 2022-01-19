#operations = ['+', '-', '/', '*'] #lisk
#correct_data_types = [float, int] #lisk
#tuple - неизменяемый список.
operations = {'+', '-', '/', '*'}
correct_data_types = float, int
# a = tuple('hello, world!') # создать кортеж из итерируемого объекта

def IK_calc(operation, x, y):
    try:
        if operation == '+':
            return x + y
        if operation == '-':
            return x - y
        if operation == '*':
            return x * y
        if operation == '/':
            return x / y
        else:
            print("Incorrect operation: '", operation, "', need one of ", operations)
    except ZeroDivisionError:
        print("ZDE")
    except TypeError:
        print("TypeError: ")
#    except SyntaxError # по суті в коді який запускався дана перевірка не потрібна
#    except ValueError: # по суті перевірка не потрібна оскільки враховано ZeroDivisionError:




