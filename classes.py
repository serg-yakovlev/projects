class AClass():
    name="uasia"
    first_name="ivanov"

    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name

if __name__ == "__main__":
    a=AClass("A","obj")
    b=AClass("B","obj")
    a.attr1=1
    #print(dir(a))
    #print(dir(b))
    #print(a.__dict__)
    #print(a.name)
    #print(b.name)
    #print(a.first_name)
    #print(a)
    #print(b)#

def __str__(self):
    return f"{self.name}"

print(a.__dict__)

def __setattr__(self, name, value):
    print(name, value, "Set value")
    super().__settatr__(name, value)
