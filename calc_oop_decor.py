def check_arg(method):
    
    def wrapper(self, message, err_message):
        arg = method(self, message, err_message)
        while True:
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
                e.print_message()
                arg = method(self, message, err_message) 
    return wrapper

                      
def check_action(method):
    
    def wrapper(self, message, err_message):
        action = method(self, message, err_message) 
        while True:                  
            try:        
                if  action in "+-*/" and action !="":
                    correct_act = action
                return(correct_act)
            except:
                e = CalcException(action, err_message)
                e.print_message()
                action = method(self, message, err_message) 
    return wrapper   


class CalcException():

    def __init__(self, inp, err_message):
        self.inp = inp
        self.err_message = err_message        
    
    def print_message(self):
        print("       Error: '{}'{}".format(self.inp, self.err_message))
        return None

    
class Calculator():

    @check_arg
    def get_arg(self, message, err_message):
        arg = input(message)
        return arg

    @check_action
    def get_action(self, message, err_message):
        act = input(message)
        return act
                 
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

    def calculate(self):
        self.arg1 = self.get_arg("Type first number: ", " is not a correct number")
        self.action = self.get_action("Type action(+ - * /): ", " is not a correct action")
        self.arg2 = self.get_arg("Type second number: ", " is not a correct number")
        print(self.arg1, self.action, self.arg2, "=", self.get_result())
        return(input("Do you want to exit? (y/n) ")!="y")


a = Calculator()
while a.calculate():
    pass
