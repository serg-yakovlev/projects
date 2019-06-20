actions=["+","-","*","/"]
arg1=input("print first nr")
arg2=input("print second nr")
action=input("specify action")


try:
    if "." in arg1:
        arg1 = float(arg1)
    else:
        arg1 = int(arg1)
except ValueError:
    print("error arg1")
    exit(1)



try:
    if "." in arg2:
        arg2 = float(arg2)
    else:
        arg2 = int(arg2)
except ValueError:
    print("error arg2")
    exit(1)



if action not in actions:
    print("Error")


if action == "+":
    print(arg1+arg2)

if action == "-":
    print(arg1-arg2)

if action == "*":
    print(arg1*arg2)

if action == "/":
    print(arg1/arg2)
