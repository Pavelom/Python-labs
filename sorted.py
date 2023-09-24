g = input("text=")
gg = g.split()
a = ""
for i in gg:
    if len(i) >= 4:
        a += i
print(len(a))
