from datetime import datetime

def clock(func):

    def action(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        message = "Start: {0}, End: {1})"
        print(message.format(start,end))
        return(result)
    return action


def wrap(func):

    def action(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Decorator wrapper")
        return result
    return action

@wrap
@clock
def func():
    for i in range(0, 10):
        print(i)
    return("End")

if __name__ == '__main__':
    print(func())
