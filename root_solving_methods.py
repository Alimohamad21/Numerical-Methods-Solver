import time
from math import sin, cos, tan, log, exp
import sympy as sy
from sympy import symbols

def fx(equation, value):
    equation = equation.replace('ln', 'log')
    equation = equation.replace('^', '**')
    x = value
    return eval(equation)


def derivative(equation, value):
    equation = equation.replace('ln', 'sy.log')
    equation = equation.replace('sin', 'sy.sin')
    equation = equation.replace('cos', 'sy.cos')
    equation = equation.replace('tan', 'sy.tan')
    equation = equation.replace('exp', 'sy.exp')
    equation = equation.replace('^', '**')
    x = symbols('x')
    d = eval(equation).diff(x)
    return d.evalf(subs={x: value})


def gx_fixed_point(equation):
    equation = equation.replace('ln', 'log')
    multiplier = '-1'
    for i in range(len(equation)):
        if equation[i] == 'x':
            if i + 1 == len(equation) or (equation[i + 1] != ')' and equation[i + 1] != '^'):
                if i == 0:
                    if equation[+1] == '-':
                        equation = equation[1:]
                    else:
                        equation = equation[2:]
                    break
                elif equation[i - 1] == '+' or equation[i - 1] == '-':
                    if equation[i - 1] == '-':
                        multiplier = '1'
                    equation = equation[:i - 1] + equation[i + 1:]
                    break
                elif i >= 2 and equation[i - 2].isnumeric():
                    j = i - 2
                    count = 1
                    multiplier = ''
                    while j >= 0:
                        if equation[j] == '-':
                            break
                        if equation[j] == '+':
                            multiplier = multiplier + '-'
                            break
                        multiplier += equation[j]
                        j -= 1
                        count += 1
                    multiplier = multiplier[::-1]
                    if j == -1:
                        multiplier = '-' + multiplier
                    equation = equation[:i - count] + equation[i + 1:]
                    break
    equation = '(' + equation + f')*1/{multiplier}'
    return equation


def fixed_point(equation, initial_guess, epsilon=0.00001, max_iterations=50):
    start_time = time.time()
    xi = initial_guess
    iterations = ''
    iterations += f'i \t\t\t xi \t\t\t\t\t f(xi)\t\t\t\t\tEa(%)\n'
    iterations += '%d \t %.16f \t %.15f\t\t\t-\n' % (0, xi, fx(equation, xi))
    gx_equation = gx_fixed_point(equation)
    for i in range(1, max_iterations + 1):
        prev = xi
        xi = fx(gx_equation, xi)
        approximate_error = abs((xi - prev) / xi) * 100
        iterations += '%d \t %.16f \t %.15f\t\t %.16f\n' % (i, xi, fx(equation, xi), approximate_error)
        if approximate_error < epsilon:
            break
    execution_time = time.time() - start_time
    return {'Final Answer': str(xi), 'Iterations': iterations, 'Execution Time': str(execution_time)}


def newton_raphson(equation, initial_guess, epsilon=0.00001, max_iterations=50):
    start_time = time.time()
    xi = initial_guess
    iterations = ''
    iterations += f'i \t\t\t xi \t\t\t\t\t f(xi)\t\t\t\t\tEa(%)\n'
    iterations += '%d \t %.16f \t %.15f\t\t\t-\n' % (0, xi, fx(equation, xi))
    for i in range(1, max_iterations + 1):
        prev = xi
        xi = xi - fx(equation, xi) / derivative(equation, xi)
        approximate_error = abs((xi - prev) / xi) * 100
        iterations += '%d \t %.16f \t %.15f\t\t %.16f\n' % (i, xi, fx(equation, xi), approximate_error)
        if approximate_error < epsilon:
            break
    execution_time = time.time() - start_time
    return {'Final Answer': str(xi), 'Iterations': iterations, 'Execution Time': str(execution_time)}


def bisection(equation, xl, xu, epsilon=0.00001, max_iterations=50):
    start_time = time.time()
    xr = (xl + xu) / 2
    iterations = ''
    iterations += f'i \t\t\t xl \t\t\t\t\t xu \t\t\t\t\t xr \t\t\t\t\t f(xr) \t\t\t\t\t Ea(%)\n'
    iterations += '%d \t %.16f \t %.15f\t\t  %.15f\t\t %.15f\t\t\t\t-\n' % (0, xl, xu, xr, fx(equation, xr))
    if fx(equation, xl) * fx(equation, xu) < 0:
        for i in range(1, max_iterations + 1):
            if fx(equation, xr) * fx(equation, xl) < 0:
                xu = xr
            elif fx(equation, xr) * fx(equation, xl) > 0:
                xl = xr
            prev = xr
            xr = (xl + xu) / 2
            approximate_error = abs((xr - prev) / xr) * 100
            iterations += '%d\t %.15f \t\t %.15f\t\t  %.15f\t\t %.15f\t\t%.15f\n' % (
                i, xl, xu, xr, fx(equation, xr), approximate_error)
            if approximate_error < epsilon:
                break
    else:
        iterations += 'Invalid Initial guesses'
    execution_time = time.time() - start_time
    return {'Final Answer': str(xr), 'Iterations': iterations, 'Execution Time': str(execution_time)}