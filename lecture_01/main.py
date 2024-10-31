# variables

x = 11
print(x)

print(x + 2)
print(x - 2)
print(x * 2)
print(x / 2)
print(x // 2)
print(x % 2)
print(x ** 2)

y = 3
print(x + y)


# datatypes
## primitives (immutable)
### int
type_int = 2
print(type(type_int))

### float
type_float = 2.2
print(type(type_float))

### string
type_str = "hello world"
print(type(type_str))

### bool
type_bool = True
print(type_bool)
print(type_bool + 1)

## non primitive (mutable)
### list
type_list = [1, 2, 3, 4]
print(type(type_list))

### tuple
type_tuple = (1, 2, 3, 4)
print(type(type_tuple))

### dict
type_dict = {"a": 1, "b": 2, "c": 3}
print(type(type_dict))

### set
type_set = {1, 2, 3, 4}
print(type(type_set))


# control flow
if True:
    print("you see this")
else:
    print("you dont see this")

name = "abraham lincoln"
if "washington" in name:
    print("it's washington")
elif "biden" in name:
    print("mr biden")
else:
    print("the rest")


# loops
for i in range(1, 15, 2):
    print(i)
    if i == 10:
        break

i = 0
while i < 15:
    print(i)
    i += 2
    if i == 10:
        continue


# functions
def power(n, p):
    return n ** p

print(power(5, 2))
