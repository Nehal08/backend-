from sympy.abc import *
from sympy import solve
from sympy.parsing.sympy_parser import parse_expr
from sympy import Symbol
from torch import eq


def calculate(equation1,equation2,id):
    if id == 1:
        if 'x' or 'y' in equation1:
            x = Symbol('x')
            y = Symbol('y')
            return solve([equation1,equation2],x,y)
    if 'x' in equation1:
        x = Symbol('x')
        return solve(equation1,x)
    elif 'y' in equation1:
        y = Symbol('y')
        return solve(equation1,y)
    elif 'z' in equation1:
        z = Symbol('z')
        return solve(equation1,z)
    elif 'a' in equation1:
        a = Symbol('a')
        return solve(equation1,a)
    elif 'b' in equation1:
        b = Symbol('b')
        return solve(equation1,b)
    elif 'c' in equation1:
        c = Symbol('c')
        return solve(equation1,c)
    elif 'p' in equation1:
        p = Symbol('p')
        return solve(equation1,p)
    elif 'q' in equation1:
        q = Symbol('q')
        return solve(equation1,q)
    return NotImplementedError

  