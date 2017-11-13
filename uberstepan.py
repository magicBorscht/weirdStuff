P_M = {}
A = [0, 1, 2, 3, 4, 5]
P = [0, 1, 2, 3, 4, 5]
q = [0.05, 0.15, 0.15, 0.23, 0.17, 0.15]
price = [-1, 2, -3]
beta = []

for i, _a in enumerate(A):
    P_M[i] = {}
    for j, _p in enumerate(P):
        if _a == _p:
            P_M[i][j] = _a*price[1]
        elif _a > _p:
            P_M[i][j] = _p*price[1]+(_a-_p)*price[0]
        else:
            P_M[i][j] = _a*price[1]+(_p-_a)*price[2]

b_i = []
a_i = []
for line in P_M.values():
    buf = list(line.values())
    print(buf)
    a_i.append(min(buf))
    _b_i = 0
    for i, b in enumerate(buf):
        _b_i += b*q[i]
    print(_b_i)
    b_i.append(_b_i)

K_i = max(a_i)
answer = a_i.index(K_i)
print('пыщь' * 20)
print(K_i, answer+1)
print("blbl" * 20)
print(" ")

b_i_j = [list(element.values()) for element in P_M.values()]

_tmp = list(zip(*b_i_j))

for column in _tmp:
    beta.append(max(column))


r_i_j = []

b_i_j_t = list(zip(*b_i_j))

for i, row in enumerate(b_i_j_t):
    r_i_j.append([])
    for b in row:
        r_i_j[i].append(beta[i]-b)

r_i_j = list(zip(*r_i_j))

r_i = [max(row) for row in r_i_j]

rres = min(r_i)
ares = r_i.index(rres) + 1
cntres = r_i.count(rres)

if cntres > 1:
    print("минимальный риск составляет {} в {} стратегиях, например, {}".format(rres, cntres, ares))
else:
    print("минимальный риск составляет {} в стратегии №{}".format(rres, ares))

print("bl"*20+"\n")

beta = []
d = 0.2

_tmp = list(zip(*b_i_j))

k_III = []

left = []

for column in _tmp:
    k_III.append(d * min(column) + (1 - d) * max(column))

K_III = max(k_III)

aresIII = k_III.index(K_III) + 1
cntresIII = k_III.count(K_III)

if cntresIII > 1:
    print("K III составляет {} в {} стратегиях, например, {} при коэффициенте {}".format(K_III, cntresIII, aresIII, d))
else:
    print("K III составляет {} в стратегии №{} при коэффициенте {}".format(K_III, aresIII, d))
