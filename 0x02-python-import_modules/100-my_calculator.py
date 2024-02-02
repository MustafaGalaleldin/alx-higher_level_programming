#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    import calculator_1
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] == "+":
        f1 = calculator_1.add
        print("{:d} + {:d} = {:d}".format(a, b, f1(int(a), int(b))
    elif argv[2] == "-":
        f1 = calculator_1.sub
        print("{:d} - {:d} = {:d}".format(a, b, f1(int(a), int(b))
    elif argv[2] == "*":
        f1 = calculator_1.mul
        print("{:d} * {:d} = {:d}".format(a, b, f1(int(a), int(b))
    elif argv[2] == "/":
        f1 = calculator_1.div
        print("{:d} / {:d} = {:d}".format(a, b, f1(int(a), int(b))
