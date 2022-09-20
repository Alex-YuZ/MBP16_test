def fib(n):
    """_generate fibonacci numbers_

    Args:
        n (_int_): _give any integer_

    Returns:
        _int_: _fibonacci number_
    """
    if n  in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
    
def print_fib(n):
    """_print a series of fibonacci numbers_

    Args:
        n (_int_): _the number of fibonacci numbers you want to generate_
    """
    for i in range(1, n+1):
        print(fib(i))
        
    return "===Fibonacci Numbers Generated==="
        
        
if __name__ == '__main__':
    n = int(input("How many Fibonacci numbers you want to generate?"))
    print(print_fib(n))