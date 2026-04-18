def calculate(lst):
    result = []
    for i in lst:
        if isinstance(i, int):
            result.append(i**3)
        elif isinstance(i, str):
            result.append(i[::-1])
    return result

lst = [1, 'hello', 2, 'world', 3, 'python']
print(calculate(lst))
