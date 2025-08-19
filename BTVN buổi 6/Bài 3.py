from functools import reduce

def calculate(operation, *args):
    if operation == "add":
        return reduce(lambda a, b: a + b, args)
    elif operation == "multiply":
        return reduce(lambda a, b: a * b, args)
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    else:
        return "Invaid operation"

op = input("(add/ multiply/ max/ min): ")
nums = list(map(int, input("Danh sach so: ").split()))

print(calculate(op, *nums))