# lists
l1 = [1, 2, 3, 4, 5]
print(l1[0], l1[1])
print(l1[-1])
print(l1[2:4])
print(l1[2:-2])

l2 = ["hello", "world", "!"]
print(l2)
print(len(l2))

l3 = ["hello", 123, "world", 3, 2, "!"]
print(l3)

l4 = ["a", "b", "c", "d"]
for item in l4:
    print(item)

for item in l4:
    if item == "c":
        continue


l4[0] = "A"
print(l4)

l4.append("e")
l4.append("z")
l4.pop()
l4.pop(0)

l4.index("b")
l4.remove("c")
l4.insert(0, "aa")


# tuple
t1 = (1, 2, 3, 4)
print(t1)
print(t1[0])
# t1[0] = 100 # error
print(len(t1))

t2 = (False, 1, 2, "three")
print(t2)

# dictionary
d1 = {
    "first_name": "abraham",
    "last_name": "lincoln",
    "age": 200
}
print(d1)
print(d1["first_name"])

print(d1.get("first_name"))
# print(d1["non_existing_key"]) # error
print(d1.get("non_existing_key"))

print(d1.keys())
print(d1.values())

d1["birth_date"] = "February 12, 1809"
print(d1)
d1.pop("age")
print(d1)

# set
s1 = {"a", "b", "c", "d"}
print(s1)
s1.add("a")
print(s1)
s1.add("z")
print(s1)

s2 = {"w", "x", "y", "z"}
print(s1.intersection(s2))
print(s1.difference(s2))
