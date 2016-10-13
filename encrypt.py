# So here Alice has m for input and PK
import hashlib


def digest(x):
    return hash(x)


m = input("Enter m (write f for file): ")
if m == "f":
    with open("m", 'r') as f:
        m = int(f.read())
    print("m == " + str(m))
else:
    m = int(m)
with open("pk", 'r') as f:
    l = f.readline().split()
    n = int(l[0])
    q = int(l[1])
    c = int(l[2])
# M = hash(m)
M = digest(m)

print("M = h(m) = " + str(M))
# now Alice send M to Bob
with open("M", 'w') as f:
    f.write(str(M))
with open("m", 'w') as f:
    f.write(str(m))


