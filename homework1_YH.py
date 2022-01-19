# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 19:36:22 2022

@author: Yan Kharevych
"""

# =============================================================================
# Написать интерактивный калькулятор, который запрашивает у пользователя 2 
# числа и операцию (+, -, *, /), которую необходимо к ним применить, 
# и выводит результат. Выдавать сообщение об ошибке при некорректном вводе.
# =============================================================================

from operator import add, sub, mul, truediv

def calculator():
    ops = {'+': add, '-': sub, '*': mul, '/': truediv}
    
    # main loop of input
    while True:
        inpt = input('Enter your expression as "X op Y":')
        
        # parse and calculate
        try:
            x, op, y = parse(inpt)
            result = ops[op](x, y)
            print('result: {}'.format(result))
        except AssertionError:
            print('Wrong number of inputs')
        except ValueError as e:
            x, y = e.args
            print(f'X and Y should be numbers. Got "{x}" and "{y}" instead')
        except KeyError:
            print(f'Unknown operator "{op}". Only available: +, -, *, /')
        except ZeroDivisionError:
            print(f"Y can't be 0 in division")
        
        print()
            
def parse(inpt):
    splt = [w for w in inpt.split(' ') if w]   # split and remove blancks

    assert len(splt) == 3
    x, op, y = splt
    
    try:
        x = float(x)
        y = float(y)
    except ValueError as e:
        raise ValueError(x, y) from e
        
    return x, op, y
    
if __name__ == '__main__':
    calculator()
