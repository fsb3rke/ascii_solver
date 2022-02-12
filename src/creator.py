from sys import argv
l = []
for i in argv:
    if i == argv[0]:
        pass
    else:
        if i == argv[1]:
            l.append(str(i))
        else:
            l.append(" "+str(i))
t = ""
for a in l:
    t += str(a)

ascii_t_LIST = [ord(x) for x in t]
ascii_t = ""
for i in ascii_t_LIST:
    ascii_t += str(i)
    print(ascii_t, end=",")

print(f"""

---CREATED---


{ascii_t}


---  END---

""")
print(ascii_t)