import random
# Bob generates these.
# So Alice will encrypt m with PK and send it (M) to bob for sign,
# so Bob will return M and sign to Alice,
# and she will recover her message. Does she need it? Probably no, she only needs sign to send it further.
# and what is further?
# So now Alice has m and sign for M (and m too). What do she do now?
# She will send it to 3rd person for validation. Right.
# And Charlie will receive m and sign. So she needs to know SK to check the sign.
# Let's do it!

with open("keygen.in", 'r') as f:
    n = int(f.readline())
q = -1
for i in range(2, n):
    if pow(i, n - 1) % n == 1:
        q = i
        break
if q == -1:
    print("ALERT")
    exit(1)
else:
    print("q = " + str(q))
b = random.randint(1, n - 1)
c = pow(q, b) % n
pk = [n, q, c]
sk = [b]
print("Public key = " + str(pk))
print("Secret key = " + str(sk))

with open("pk", 'w') as f:
    print(n, q, c, end=" ", file=f)
with open("sk", 'w') as f:
    print(b, file=f)
    print(n, q, c, end=" ", file=f)

# такое минимальное число k, что g^(fi(m)) = 1 (mod m)
# fi(m) - минимальное число, что g^(fi(m)) == 1 (mod m)
