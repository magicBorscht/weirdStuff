import random
import numpy

# Счётчик частоты выбора тех или иных стратегий
d_count = 0
j_count = 0
cash = 1000
old_cash = 1000
d_gl_profits = (225, -50, -47, 250) # Цена за единицу товара, цена хранения, репутационные убытки,
j_gl_profits = (54, -42, -25, 60)   # чистая прибыль за ремонт
d_sale_price = 250                  # Другая чистая прибыль за ремонт (зачем я их разделил?)
j_sale_price = 60
time = 0
lose = False

counters = [0, 0, 0, 0, 0, 0, 0]
# Починено мониторов, джеков, не починено мониторов, джеков, куплено мониторов, джеков, покупатели

switcher = 0    # Переключение в режим тупицы, при значении 1 в качестве стратегии берутся переменные
raz = 3         # raz - кол-во дисплеев и dva - кол-во джеков
dva = 3

i_am_lazy = 100    # Количество ходов (мне было лень листать в конец файла)

# Каким-то образом надо учесть в формулах ниже кол-во барахла на складе.
# Покупка действительно будет дешевле при наличии уже имеющихся предметов.
# Я пошёл пить кофе.
# Комментарии оставлены для истории


def eqq(a, profit, c):
    return a * profit[0] + c * profit[3]


def moar(a, b, profit, c):
    return b * profit[0] + c * profit[3] + (a - (b + c)) * profit[1]


def less(a, b, profit, c):
    return b * profit[0] + c * profit[3] + ((b + c) - a) * profit[2]


def wisdom(strategies, needs):
    """Здесь находится РАЗУМ РОБОТА!"""
    global d_count
    global j_count
    needlist = []
    P_M = {}
    global d_gl_profits
    global j_gl_profits
    global d_sale_price
    global j_sale_price

    d_prft = list(d_gl_profits)
    j_prft = list(j_gl_profits)
    d_prft[0] = d_sale_price - d_prft[0]
    j_prft[0] = j_sale_price - j_prft[0]

    d_needs = []
    j_needs = []
    d_probs = []
    j_probs = []
    the_str = []
    prob = []
    stuff = []


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
                P_M[i][j] = eqq(_a[0] + d_count, d_prft, d_count) + eqq(_a[1] + j_count, j_prft, j_count)

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

    '''d_needs = sorted(d_needs)
    j_needs = sorted(j_needs)


    for i in reversed(range(5)):
        res = []
        for k in range(5):
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
        for k in range(5):
            if k <= i:
                res.append(1 - j_needs[k])
            else:
                res.append(j_needs[k])
        j_probs.append(sum(res) / 6)
    j_probs.append(sum(j_needs) / 6)
    # print("j_probs =", j_probs)
    the_str.append(j_probs.index(max(j_probs)))
    # print(the_str)'''

    # Я устал, это брутфорс
    d_yep = []
    j_yep = []
    d_nope = []
    j_nope = []

    for need in needs:
        d_yep.append(need[0])
        j_yep.append(need[1])
        d_nope.append(1 - need[0])
        j_nope.append(1 - need[1])

    d_probs = []
    j_probs = []
    yep = d_yep
    nope = d_nope

    d_probs.append(nope[0] * nope[1] * nope[2] * nope[3] * nope[4])
    d_probs.append((yep[0] * nope[1] * nope[2] * nope[3] * nope[4]) +
                   (nope[0] * yep[1] * nope[2] * nope[3] * nope[4]) +
                   (nope[0] * nope[1] * yep[2] * nope[3] * nope[4]) +
                   (nope[0] * nope[1] * nope[2] * yep[3] * nope[4]) +
                   (nope[0] * nope[1] * nope[2] * nope[3] * yep[4])
                   )
    d_probs.append((yep[0] * yep[1] * nope[2] * nope[3] * nope[4]) +
                   (yep[0] * nope[1] * yep[2] * nope[3] * nope[4]) +
                   (yep[0] * nope[1] * nope[2] * yep[3] * nope[4]) +
                   (yep[0] * nope[1] * nope[2] * nope[3] * yep[4]) +
                   (nope[0] * yep[1] * yep[2] * nope[3] * nope[4]) +
                   (nope[0] * yep[1] * nope[2] * yep[3] * nope[4]) +
                   (nope[0] * yep[1] * nope[2] * nope[3] * yep[4]) +
                   (nope[0] * nope[1] * yep[2] * yep[3] * nope[4]) +
                   (nope[0] * nope[1] * yep[2] * nope[3] * yep[4]) +
                   (nope[0] * nope[1] * nope[2] * yep[3] * yep[4])
                   )
    d_probs.append((yep[0] * yep[1] * yep[2] * nope[3] * nope[4]) +
                   (yep[0] * yep[1] * nope[2] * yep[3] * nope[4]) +
                   (yep[0] * yep[1] * nope[2] * nope[3] * yep[4]) +
                   (yep[0] * nope[1] * yep[2] * yep[3] * nope[4]) +
                   (yep[0] * nope[1] * yep[2] * nope[3] * yep[4]) +
                   (yep[0] * nope[1] * nope[2] * yep[3] * yep[4]) +
                   (nope[0] * yep[1] * yep[2] * yep[3] * nope[4]) +
                   (nope[0] * yep[1] * yep[2] * nope[3] * yep[4]) +
                   (nope[0] * nope[1] * yep[2] * yep[3] * yep[4])
                   )
    d_probs.append((yep[0] * yep[1] * yep[2] * yep[3] * nope[4]) +
                   (yep[0] * yep[1] * yep[2] * nope[3] * yep[4]) +
                   (yep[0] * yep[1] * nope[2] * yep[3] * yep[4]) +
                   (yep[0] * nope[1] * yep[2] * yep[3] * yep[4]) +
                   (nope[0] * yep[1] * yep[2] * yep[3] * yep[4])
                   )
    d_probs.append((yep[0] * yep[1] * yep[2] * yep[3] * yep[4]))

    yep = j_yep
    nope = j_nope
    j_probs.append(nope[0] * nope[1] * nope[2] * nope[3] * nope[4])
    j_probs.append((yep[0] * nope[1] * nope[2] * nope[3] * nope[4]) +
                   (nope[0] * yep[1] * nope[2] * nope[3] * nope[4]) +
                   (nope[0] * nope[1] * yep[2] * nope[3] * nope[4]) +
                   (nope[0] * nope[1] * nope[2] * yep[3] * nope[4]) +
                   (nope[0] * nope[1] * nope[2] * nope[3] * yep[4])
                   )
    j_probs.append((yep[0] * yep[1] * nope[2] * nope[3] * nope[4]) +
                   (yep[0] * nope[1] * yep[2] * nope[3] * nope[4]) +
                   (yep[0] * nope[1] * nope[2] * yep[3] * nope[4]) +
                   (yep[0] * nope[1] * nope[2] * nope[3] * yep[4]) +
                   (nope[0] * yep[1] * yep[2] * nope[3] * nope[4]) +
                   (nope[0] * yep[1] * nope[2] * yep[3] * nope[4]) +
                   (nope[0] * yep[1] * nope[2] * nope[3] * yep[4]) +
                   (nope[0] * nope[1] * yep[2] * yep[3] * nope[4]) +
                   (nope[0] * nope[1] * yep[2] * nope[3] * yep[4]) +
                   (nope[0] * nope[1] * nope[2] * yep[3] * yep[4])
                   )
    j_probs.append((yep[0] * yep[1] * yep[2] * nope[3] * nope[4]) +
                   (yep[0] * yep[1] * nope[2] * yep[3] * nope[4]) +
                   (yep[0] * yep[1] * nope[2] * nope[3] * yep[4]) +
                   (yep[0] * nope[1] * yep[2] * yep[3] * nope[4]) +
                   (yep[0] * nope[1] * yep[2] * nope[3] * yep[4]) +
                   (yep[0] * nope[1] * nope[2] * yep[3] * yep[4]) +
                   (nope[0] * yep[1] * yep[2] * yep[3] * nope[4]) +
                   (nope[0] * yep[1] * yep[2] * nope[3] * yep[4]) +
                   (nope[0] * nope[1] * yep[2] * yep[3] * yep[4])
                   )
    j_probs.append((yep[0] * yep[1] * yep[2] * yep[3] * nope[4]) +
                   (yep[0] * yep[1] * yep[2] * nope[3] * yep[4]) +
                   (yep[0] * yep[1] * nope[2] * yep[3] * yep[4]) +
                   (yep[0] * nope[1] * yep[2] * yep[3] * yep[4]) +
                   (nope[0] * yep[1] * yep[2] * yep[3] * yep[4])
                   )
    j_probs.append((yep[0] * yep[1] * yep[2] * yep[3] * yep[4]))


    for i in range(len(needlist)):
        prob.append((d_probs[needlist[i][0]] * j_probs[needlist[i][1]]))
    the_str = needlist[prob.index(max(prob))]

    # print(needlist[prob.index(max(prob))])
    b_i = []
    for line in P_M.values():
        buf = list(line.values())
        # b_i.append(max(buf)* prob[i])

    for line in P_M.values():
        buf = list(line.values())
        stuff.append(buf)

    for thing in stuff:
        b = 0
        for i in range(len(thing)):
            b += thing[i] * prob[i]
        b_i.append(b)
    ge = b_i.index(max(b_i))

    print("Выбранная стратегия: ", strategies[ge])
    # print("Вероятный профит:", b_i[ge])
    print("Но наиболее вероятное развитие событий:", the_str)
    # print("Вероятный профит:", b_i[strategies.index(the_str)])
    # print("Вероятный профит от [3, 3]:", b_i[strategies.index([3, 3])])
    # [3, 3] - одна из наиболее живучих стратегий на тестах, так что я вбил
    # эту строчку для сравнения при отстройке ИИ
    global switcher
    global raz
    global dva
    if switcher == 1:
        strategies[ge][0] = raz
        strategies[ge][1] = dva
    elif switcher == 2:
        strategies[ge][0] = the_str[0]
        strategies[ge][1] = the_str[1]

    return strategies[ge]


def zakup(strtg):
    """Закупка абстрактного оборудования в соответствии со стратегией"""
    global d_count
    global j_count
    global cash
    global d_gl_profits
    global j_gl_profits
    global d_sale_price
    global j_sale_price
    global counters

    ge = d_count
    gege = j_count
    sauce = [0, 0]

    for i in range(ge, strtg[0]):
        if cash < d_gl_profits[0]:
            print("Сперва прикупи себе денег")
            break
        d_count += 1
        cash -= d_gl_profits[0]
        counters[4] += 1
        sauce[0] += 1

    for i in range(gege, strtg[1]):
        if cash < j_gl_profits[0]:
            print("Даже джек купить не можешь")
            break
        j_count += 1
        cash -= j_gl_profits[0]
        sauce[1] += 1
        counters[5] += 1
    print("Приобретено {} дисплеев и {} джеков, теперь их {} и {}".format(sauce[0], sauce[1], d_count, j_count))
    print("В кассе теперь ", cash, " чего бы то ни было")


def repair(customers):
    """Непосредственно применение стратегии"""
    global cash
    global j_count
    global d_count
    global d_gl_profits
    global j_gl_profits
    global d_sale_price
    global j_sale_price
    global counters

    for person in customers:
        counters[6] += 1
        if person[0] == 1 and d_count > 0:
            d_count -= 1
            cash += d_sale_price
            print(f"Починен дисплей, получено {d_sale_price} чего бы то ни было")
            counters[0] += 1
        elif person[0] == 1 and d_count == 0:
            cash += d_gl_profits[2]
            print("Не починен дисплей, репутация ПАДАЕТ!")
            counters[2] += 1

        if person[1] == 1 and j_count > 0:
            j_count -= 1
            cash += j_sale_price
            print("Починен джек, получено {} чего бы то ни было".format(j_sale_price))
            counters[1] += 1
        elif person[1] == 1 and j_count == 0:
            cash += j_gl_profits[2]
            print("Не починен джек, репутация ПАДАЕТ!")
            counters[3] += 1

    if cash < 0:
        cash = 0


def move():
    """Ход"""
    global cash
    global d_count
    global j_count
    global old_cash
    global d_gl_profits
    global j_gl_profits
    global d_sale_price
    global j_sale_price

    customers = []
    strategies = []
    needs = []

    for i in range(6):
        for j in range(6):
            strategies.append([i, j])

    for i in range(5):
        d_need = round(random.uniform(0.0, 1.0), 1)
        j_need = round(random.uniform(0.0, 1.0), 1)
        needs.append([d_need, j_need])

    # print("these are NEEDS:", needs)
    chosen = wisdom(strategies, needs)
    # print(chosen)

    zakup(chosen)
    for k in needs:
        customers.append([numpy.random.choice([0, 1], p=[1 - k[0], k[0]]),
                          numpy.random.choice([0, 1], p=[1 - k[1], k[1]])])
    #print(customers)
    repair(customers)
    print("К концу дня на складе {} дисплеев и {} джеков".format(d_count, j_count))
    pay = -((d_gl_profits[1] * d_count) + (j_gl_profits[1] * j_count))
    print("Оплата хранения: {}".format(pay))
    cash -= pay
    if cash < 0:
        cash = 0
    print("Денег в кассе: {}, выручка за день: {}".format(cash, cash - old_cash))
    print('\n', '=' * 40, '\n')
    old_cash = cash


for i in range(i_am_lazy):
    time += 1
    print("Ход ", time)
    if cash < 40 and j_count == 0 and d_count == 0:
        print("Проиграл за {} дней".format(i+1))
        lose = True
        break
    move()

if lose:
    print("Такое нечасто случается, но гениальный искусственный интеллект подвёл наш гипотетический магазинчик.\n \
За свою недолгую и не очень-то победоносную карьеру он успел обслужить {} клиентов, починив {} дисплеев и \
{} джеков. Недовольными остались {} клиентов.".format(counters[6], counters[0], counters[1], counters[2] +
                                                      counters[3]))
else:
    print("Игра успешно окончена. За {} ходов разум машины принёс прибыль в {} абстрактных единиц, обслужил {} клиентов,\
 починил {} дисплеев и {} джеков, но при этом оставил недовольными {} клиентов. \nБыло куплено {} дисплеев и \
{} джеков. \nВо время работы ни один робот не пострадал.".format(time, cash - 1000, counters[6],
                                                                 counters[0], counters[1],
                                                                 counters[2] + counters[3],
                                                                 counters[4], counters[5]))

