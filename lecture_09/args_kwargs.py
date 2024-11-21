def func(x, *args, **kwargs):
    print(x)
    # print(type(args))
    # print(type(kwargs))
    print(args)
    print(kwargs)


# func("hello", 1, 2, 3, 4)

# func(x="hello", y="world", z="!")

func("hello", 1, 2, 3, 4, y="world", z="!")

# func("hello", 1, 2, 3, 4, x = "hi", y="world", z="!") # error!!!



def func2(x, y):
    print(f"{x} {y}!")


# func2("hello", "world")

func2(**{"y": "world", "x": "hello"})
func2(*["hello", "world"])
