import random
import numpy

d_count = 0
j_count = 0
cash = 100
old_cash = 100
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
    needlist = []
    P_M = {}
    d_prft = [7, -22, -7]
    j_prft = [2, -8, -4]
    d_needs = []
    j_needs = []
    d_probs = []
    j_probs = []
    the_str = []
    prob = []
    beta = []

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
                print("that should not happen")
                print(_a, _p)

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
    # print("d_probs =", d_probs)
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
    # print("j_probs =", j_probs)
    the_str.append(j_probs.index(max(j_probs)))
    # print(the_str)

    for i in range(len(needlist)):
        prob.append((d_probs[needlist[i][0]] + j_probs[needlist[i][1]]) / 2)

    # print(needlist[prob.index(max(prob))])
    b_i = []
    i = 0
    for line in P_M.values():
        buf = list(line.values())
        print(max(buf)* prob[i])
        i += 1
        b_i.append(max(buf)* prob[i])
        _b_i = 0
        '''for i, b in enumerate(buf):
            _b_i += b * prob[i]
        b_i.append(_b_i)'''
    ge = 12  # P_M[the_str[0] * the_str[1] - 1][the_str[0] * the_str[1] - 1]
    print("ВНИМАНИЕ! ГЕ: ", ge)
    # the_str[0] = 100
    # the_str[1] = 100
    return the_str


def zakup(strtg):
    global d_count
    global j_count
    global cash
    ge = d_count
    gege = j_count
    sauce = [0, 0]

    for i in range(ge, strtg[0]):
        if cash < 15:
            print("Сперва прикупи себе денег")
            break
        d_count += 1
        cash -= 15
        sauce[0] += 1

    for i in range(gege, strtg[1]):
        if cash < 4:
            print("Даже джек купить не можешь")
            break
        j_count += 1
        cash -= 4
        sauce[1] += 1
    print("Приобретено {} дисплеев и {} джеков, теперь их {} и {}".format(sauce[0], sauce[1], d_count, j_count))
    print("В кассе теперь ", cash, " чего бы то ни было")


def repair(customers):
    global cash
    global j_count
    global d_count
    for person in customers:
        if person[0] == 1 and d_count > 0:
            d_count -= 1
            cash += 22
            print("Починен дисплей, получено 22 чего бы то ни было")
        elif person[0] == 1 and d_count == 0:
            cash -= 7
            print("Не починен дисплей, репутация ПАДАЕТ!")

        if person[1] == 1 and j_count > 0:
            j_count -= 1
            cash += 6
            print("Починен джек, получено 6 чего бы то ни было")
        elif person[1] == 1 and j_count == 0:
            cash -= 4
            print("Не починен джек, репутация ПАДАЕТ!")

    if cash < 0:
        cash = 0

def move():
    global cash
    global d_count
    global j_count
    global old_cash

    customers = []
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
    # print(chosen)
    # print("these are NEEDS:", needs)
    zakup(chosen)
    for k in needs:
        customers.append([numpy.random.choice([0, 1], p=[k[0], 1 - k[0]]),
                          numpy.random.choice([0, 1], p=[k[1], 1 - k[1]])])
    print(customers)
    repair(customers)
    print("К концу дня на складе {} дисплеев и {} джеков".format(d_count, j_count))
    print("Оплата хранения: {}".format((7 * d_count) + (j_count * 4)))
    cash -= (7 * d_count) + 4 * j_count
    if cash < 0:
        cash = 0
    print("Денег в кассе: {}, выручка за день: {}".format(cash, cash - old_cash))
    print('\n', '=' * 40, '\n')
    old_cash = cash

for i in range(1):
    if cash < 4 and j_count == 0 and d_count == 0:
        print("Проиграл за {} дней".format(i))
        break
    move()
