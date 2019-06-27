class CalcException(Exception):
    pass


def tryNumber(inp, errMessage):
    try:
        if  "." in inp:
            inp=float(inp)
        elif "," in inp:
            inp=float(inp.replace(",","."))
        else:
            inp=int(inp)
    except ValueError:
        raise CalcException(errMessage)
        return(inp)


def tryAction(inp, errMessage):
    if  inp in "+-*/":
        action=inp
    else:
        print("This input is not a correct action: ", inp)
    return(inp)



def check_data(inpData):
    args = inpData()
    arg1 = tryNumber(args[0], "First argument is not a correct number: ")
    action = tryAction(args[1], "This input is not a correct action: ")
    arg2 = tryNumber(args[2], "Second argument is not a correct number: ")
    return([arg1,action,arg2])


@check_data
def inpData():
    arg1 = input("Type first number: ")
    action = input("Type action(+ - * /): ")
    arg2 = input("Type second number: ")
    return([arg1,action,arg2])


def outputData(args):
    arg1=args[0]
    action=args[1]
    arg2=args[2]

    if action == "+":
        result = arg1+arg2
    elif action == "-":
        result = arg1-arg2
    elif action == "*":
        result = arg1*arg2
    elif action == "/":
        result = arg1/arg2
    return('{0} {1} {2} = {3}'.format(arg1,action,arg2,result))


def main():
    result = outputData(inpData)
    print(result)


main()
