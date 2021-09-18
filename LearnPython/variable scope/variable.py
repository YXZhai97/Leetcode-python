'''
LEGB
Local, Enclosing, Global, Built-in
'''

x='global x'

def test():
    global x # tell python that x should be treated as global variable
    y= 'local y' # y only lives within the function
    x = 'local x'
    print(y) # first find the y inside the function and print it
    print(x)

test()
print(x)

x='global x'
def outer():
    # x="outer x"
    def inner():
        # nonlocal x
        # x="inner x"
        print(x)
    inner()
    print(x)

outer()





