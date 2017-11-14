import random

d_count = 0
j_count = 0
cash = 100


def wisdom(strategies, needs, prices, profits):
    d_avg = 0
    j_avg = 0
    needlist = []
    P_M = {}

    for i in range(1, 10):
        for j in range(1, 10):
            needlist.append([i, j])

    # Вот здесь надо адаптировать формулу под
    # то, что у меня вместо чисел в стратегиях
    # листы.

    for i, _a in enumerate(strategies):
        P_M[i] = {}
        for j, _p in enumerate(needlist):
            if _a == _p:
                P_M[i][j] = _a * prices[1]
            elif _a > _p:
                P_M[i][j] = _p * prices[1] + (_a - _p) * prices[0]
            else:
                P_M[i][j] = _a * prices[1] + (_p - _a) * prices[2]

    for i in P_M.keys():
        print(P_M[i])

    for client in needs:
        d_avg += client[0]
        j_avg += client[1]

    d_avg = d_avg / 5
    j_avg = j_avg / 5
    print(d_avg, j_avg)

    varg = []
    for strtg in strategies:
        kek = ((d_avg * profits[0] * strtg[0]) + (j_avg * profits[1]) * strtg[1]) - ((d_avg * prices[0] * strtg[0]) + (j_avg * prices[1]) * strtg[1])
        varg.append(kek)
    print('varg = ', varg)
    return varg.index(max(varg))

def move():
    global cash
    global dispcount
    global jackcount

    if cash <= 4:
        return 'You lose'

    prices = [15, 4]

    profits = [22, 6]

    strategies = []
    needs = []

    for i in range(1, 10):
        for j in range(1, 10):
            strategies.append([i, j])

    for i in range(5):
        d_need = round(random.uniform(0.0, 0.5), 1)
        j_need = round(random.uniform(0.0, 0.5), 1)
        needs.append([d_need, j_need])

    chosen = wisdom(strategies, needs, prices, profits)
    print(chosen)



move()
