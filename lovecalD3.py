uname = input("enter your name:").lower()
cname = input("enter crush name:").lower()

name = uname + cname

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

a = t+r+u+e
b = l+o+v+e

print("love factor = ", str(a) + str(b))
