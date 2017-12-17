def f(n, result=1):
    if n == 1:
        return result
    return f(n-1, n * result)


print(f(5))