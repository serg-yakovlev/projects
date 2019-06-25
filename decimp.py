import decor as dc

@dc.clock
def newFunc():
    for i in range(200):
        print(i)

@dc.clock
@dc.wrap
def func():
    for i in range(1,5):
        print(i)

if __name__ == "__main__":
    print(dc.funcWrap)
    print(dc.funcClock)
