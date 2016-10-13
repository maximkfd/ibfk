# who should do this?
# Bob, i believe? He got SK. Or anyone, who got SK.
# We receive here message(m) and sign(r, s)
with open('m', 'r') as f:
    m = int(f.read())
with open('sign', 'r') as f:
    l = f.readline().split()
    r = int(l[0])
    s = float(l[1])
with open('sk', 'r') as f:
    x = int(f.readline())
    l = f.readline().split()
    n = int(l[0])
    q = int(l[1])
    c = int(l[2])
# c^r*r^s mod n = q^m mod n
left = (pow(c, r) % n) * (pow(r, s) % n) % n
right = pow(q, m) % n
print(left)
print(right)


