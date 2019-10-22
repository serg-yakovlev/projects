class CalcException():

    def __init__(self, inp, err_message):
        self.inp = inp
        self.err_message = err_message
    
    def print_message(self):
        print("       Error: '{}'{}".format(self.inp, self.err_message))
        return None

    
class Calculator():

    def get_arg(self, message, err_message):
        arg = self.check_arg(input(message),err_message)
        while arg == None:
            arg = self.check_arg(input(message),err_message)
        return arg

    def get_action(self, message, err_message):
        act = self.check_action(input(message),err_message)
        while act == None:
            act = self.check_action(input(message),err_message)
        return act

    def get_args(self):
        arg1 = self.get_arg("Type first number: ", " is not a correct number")
        action = self.get_action("Type action(+ - * /): ", " is not a correct action")
        arg2 = self.get_arg("Type second number: ", " is not a correct number")
        return arg1, action, arg2

    def check_arg(self, arg, err_message):
        try:
            if  "." in arg:
                arg = float(arg)
            elif "," in arg:
                arg = float(arg.replace(",","."))
            else:
                arg = int(arg)
            return arg
        except:
            e = CalcException(arg, err_message)
            return e.print_message()
                      
    def check_action(self, action, err_message):
        try:        
            if  action in "+-*/" and action != "":
                correct_act = action
            return(correct_act)
        except:
            e = CalcException(action, err_message)
            return e.print_message()
                 
    def get_result(self):
        if self.action == "+":
            self.result = self.arg1+self.arg2
        elif self.action == "-":
            self.result = self.arg1-self.arg2
        elif self.action == "*":
            self.result = self.arg1*self.arg2
        elif self.action == "/":
            self.result = self.arg1/self.arg2
        return self.result


a = Calculator()
while True:
    a.arg1, a.action, a.arg2 = a.get_args()
    print(a.arg1, a.action, a.arg2, "=", a.get_result())
    exit_calc = input("Do you want to exit? (y/n) ")
    if exit_calc == "y":
        break
