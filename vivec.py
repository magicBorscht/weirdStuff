import random

d_count = 0
j_count = 0
cash = 100
# Каким-то образом надо учесть в формулах ниже кол-во барахла на складе.
# Покупка действительно будет дешевле при наличии уже имеющихся предметов.
# Я пошёл пить кофе.


def eqq(a, profit, c):
    return a * profit[0] + (c * 4)


def moar(a, b, profit, c):
    return (b + c) * profit[0] + (a - (b + c)) * profit[1]


def less(a, b, profit, c):
    return (b + c) * profit[0] + ((b + c) - a) * profit[2]


def wisdom(strategies, needs, prices, profits):
    global d_count
    global j_count
    d_avg = 0
    j_avg = 0
    needlist = []
    P_M = {}
    d_prft = [7, -15, -10]
    j_prft = [2, -4, -5]
    d_needs = []
    j_needs = []
    d_probs = []
    j_probs = []
    the_str = []
    prob = []

    for ge in needs:
        d_needs.append(ge[0])
        j_needs.append(ge[1])

    for i in range(6):
        for j in range(6):
            needlist.append([i, j])

    # Лучше остановиться здесь и верить в то, что всё хорошо.
    # Правда. Лучше перестать читать код прямо здесь.
    # Дальше всё очень страшно, поверьте.
    # Мне самому страшно.

    for i, _a in enumerate(strategies):
        P_M[i] = {}
        for j, _p in enumerate(needlist):
            if _a[0] + d_count == _p[0] and _a[1] + j_count == _p[1]:
                P_M[i][j] = eqq(_a[0], d_prft, d_count) + eqq(_a[1], j_prft, j_count)

            elif _a[0] + d_count > _p[0] and _a[1] + j_count == _p[1]:
                P_M[i][j] = moar(_a[0], _p[0], d_prft, d_count) + eqq(_a[1], j_prft, j_count)
                # p * prices[1] + (_a - _p) * prices[0]
            elif _a[0] + d_count == _p[0] and _a[1] + j_count > _p[1]:
                P_M[i][j] = eqq(_a[0], d_prft, d_count) + moar(_a[1], _p[1], j_prft, j_count)

            elif _a[0] + d_count > _p[0] and _a[1] + j_count > _p[1]:
                P_M[i][j] = moar(_a[0], _p[0], d_prft, d_count) + moar(_a[1], _p[1], j_prft, j_count)

            elif _a[0] + d_count < _p[0] and _a[1] + j_count == _p[1]:
                P_M[i][j] = less(_a[0], _p[0], d_prft, d_count) + eqq(_a[1], j_prft, j_count)

            elif _a[0] + d_count == _p[0] and _a[1] + j_count < _p[1]:
                P_M[i][j] = eqq(_a[0], d_prft, d_count) + less(_a[1], _p[1], j_prft, j_count)

            elif _a[0] + d_count < _p[0] and _a[1] + j_count < _p[1]:
                P_M[i][j] = less(_a[0], _p[0], d_prft, d_count) + less(_a[1], _p[1], j_prft, j_count)
            # Мне реально стыдно на этом моменте.
            elif _a[0] + d_count > _p[0] and _a[1] + j_count < _p[1]:
                P_M[i][j] = moar(_a[0], _p[0], d_prft, d_count) + less(_a[1], _p[1], j_prft, j_count)

            elif _a[0] + d_count < _p[0] and _a[1] + j_count > _p[1]:
                P_M[i][j] = less(_a[0], _p[0], d_prft, d_count) + moar(_a[1], _p[1], j_prft, j_count)
            else:
                print("that should not happen")  # P_M[i][j] = _a * prices[1] + (_p - _a) * prices[2]
                print(_a, _p)
    i = 0
    for k in P_M.keys():
        print(i, P_M[k])
        i += 1
    # And now for something completely different. The possibilities
    d_needs = sorted(d_needs)
    j_needs = sorted(j_needs)

    for i in reversed(range(5)):
        res = []
        for k in range(6):
            if k <= i:
                res.append(1 - d_needs[k])
            else:
                res.append(d_needs[k])
        d_probs.append(sum(res) / 6)
    d_probs.append(sum(d_needs) / 6)
    print("d_probs =", d_probs)
    the_str.append(d_probs.index(max(d_probs)))

    for i in reversed(range(5)):
        res = []
        for k in range(6):
            if k <= i:
                res.append(1 - j_needs[k])
            else:
                res.append(j_needs[k])
        j_probs.append(sum(res) / 6)
    j_probs.append(sum(j_needs) / 6)
    print("j_probs =", j_probs)
    the_str.append(j_probs.index(max(j_probs)))
    print(the_str)

    for i in range(len(needlist)):
        prob.append((d_probs[needlist[i][0]] + j_probs[needlist[i][1]]) / 2)
    print(prob)
    print(needlist[prob.index(max(prob))])

    # А теперь для каждой стратегии надо помножить вероятность на возможный выигрыш

    # Это не нужно и будет удалено (возможно)
    ''' for client in needs:
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
    return varg.index(max(varg)) '''
    return 12


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

    for i in range(6):
        for j in range(6):
            strategies.append([i, j])

    for i in range(6):
        d_need = round(random.uniform(0.0, 1.0), 1)
        j_need = round(random.uniform(0.0, 1.0), 1)
        needs.append([d_need, j_need])

    chosen = wisdom(strategies, needs, prices, profits)
    print(chosen)
    print("this is NEEDS:", needs)


move()
