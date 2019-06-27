class ClassException():
    pass


def tryNumber(inp, errMessage, nr):
    try:
        if  "." in inp:
            inp=float(inp)
        elif "," in inp:
            inp=float(inp.replace(",","."))
        else:
            inp=int(inp)
    except:
        ClassException()
        print("Line "+str(nr)+": "+errMessage, inp)
    return(inp)


def tryAction(inp, errMessage, nr):
    if  inp in "+-*/":
        action=inp
    else:
        print("Line "+str(nr)+": "+errMessage, inp)
    return(inp)
    

def check_data(inpData):
    data = inpData()
    args = data[0]
    actions = data[1]
    newArgs=[]
    newActions=[]
    
    i=0
    for act in actions[:-1]:
        newArgs.append(tryNumber(args[i], " This argument is not a correct number: ", i*2+1))
        newActions.append(tryAction(actions[i], " This input is not a correct action: ", i*2+2))
        i+=1
    newArgs.append(tryNumber(args[i], " This argument is not a correct number: ", i*2+1))
    return([newArgs, newActions])


@check_data
def inpData():
    args=[]
    actions=[]
    args.append(input("1. Please type first number: "))
    i=2
    while True:
        act=input(str(i)+'. Please type action(+ - * /) or "f" to finish input: ')
        i+=1
        actions.append(act)
        if act == "f":
            return([args, actions])        
        arg=input(str(i)+'. Please type next number: ')
        i+=1
        args.append(arg)


def outputData(data):
    args = data[0]
    actions = data[1]
    result = args[0]
    for i in range(1,len(args)):
        text = str(result)+actions[i-1]+str(args[i])+"="
        result = calcIter(result, actions[i-1],args[i])
        print(text+str(result))
    return(result)


def calcIter(prevRes, action, nextArg):
    if action == "+":
        result = prevRes+nextArg
    elif action == "-":
        result = prevRes-nextArg
    elif action == "*":
        result = prevRes*nextArg
    elif action == "/":
        result = prevRes/nextArg
    return(result)

        
def main():
    result = outputData(inpData)
    print("Result is "+str(result))


main()
    
