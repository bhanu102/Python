'''Closures'''

def outer_func():
    msg="Bhanu"
    def inner_func():
        print("Hi", msg)
    return inner_func()

func=outer_func
func()
