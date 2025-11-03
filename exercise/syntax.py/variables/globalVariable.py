# Variable outside function 

x="pepsi"
def myfunc():
    print("i love drinking "+x)
myfunc()

# Variable inside a function 
x="awesome"
def func():
    x="fantastics"
    print("python is "+x)

func()

# the global keyword 
def func():
    global x
    x="fantastic"
func()
print("python is "+x)