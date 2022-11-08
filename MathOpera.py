def MathOperator(firstVar, secondVar, Operator):
    var1 = firstVar
    var2 = secondVar
    var3 = Operator
    if var3 == '+':
        test = math_addition(var1, var2)
    elif var3 == '-':
        test = math_sub(var1, var2)
    elif var3 == '*':
        test = math_multiply(var1, var2)
    else:
        test = 'failure'
    return test

def math_addition(var1, var2):
        return var1+var2

def math_sub(var1, var2):
    return var1-var2

def math_multiply(var1, var2):
    return var1*var2
