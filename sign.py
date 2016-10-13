# Bob receives M and makes sign with SK


with open('sk', 'r') as f:
    x = int(f.readline())
    l = f.readline().split()
    n = int(l[0])
    q = int(l[1])
with open('M', 'r') as f:
    M = int(f.read())
# Bob should do it, right? Alice should only hash(M) the message(m)
# gen random 1 < k < n-1 primal with n-1
# r = q^k mod n
# s =(M-x*r)k^-1 (mod p-1)
# sign(M) = r, s
k = - 1
for i in range(2, n-2):
    if n-1 % i != 0:
        k = i
        break
if k == -1:
    print("ALERT")
    exit(1)
print("k = ", k)
r = pow(q, k) % n
s = (M - x*r)*pow(k, -1) % (n-1)  # it fuckes up here, cuz I don't know how to find s
with open("sign", 'w') as f:
    print(r, s, file=f)
print("Sign(r, s) =", r, s, sep=" ")
