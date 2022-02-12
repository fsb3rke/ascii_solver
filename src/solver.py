from sys import argv
alph = [ord(x) for x in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
text = str(argv[1])
for j in alph:
    text = text.replace(str(j), str(chr(j)))
    for i in text:
        print(i, end=",")

print(f"""

---SOLVED---


{text}


--- END---

""")