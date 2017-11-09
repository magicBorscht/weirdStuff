import random

d_count = 0
j_count = 0
cash = 100


def wisdom(strategies, needs, prices, profits):
    d_avg = 0
    j_avg = 0
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
    elif cash >= 200:
        return 'You win'

    prices = [15, 4]

    profits = [22, 6]

    strategies = []
    needs = []

    for i in range(1, 10):
        for j in range(1, 10):
            strategies.append([i, j])

    for i in range(5):
        kek = round(random.uniform(0.0, 0.5), 1)
        if random.randint(0, 10) % 2 == 0:
            d_need = 0.5 + kek
            j_need = 0.5 - kek
        else:
            j_need = 0.5 + kek
            d_need = 0.5 - kek
        needs.append([d_need, j_need])

    chosen = wisdom(strategies, needs, prices, profits)
    print(chosen)



move()
