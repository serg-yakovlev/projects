actions=["+","-","*","/"]
arg1=input("print first nr")
arg2=input("print second nr")
action=input("specify action")




arg1=int(arg1)
arg2=int(arg2)

if isinstance(arg1, str) or isinstance(arg2, str):
    print("Arg error")
    exit()

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
