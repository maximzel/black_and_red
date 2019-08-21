import random


def black_or_red():
    zero1 = zero()
    if zero1 == 0:
        return 2
    elif zero1 % 2 == 0:
        return 1
    else:
        return 0


def zero():
    return random.randint(0, 36)


def currentside(side):
    return side % 2 == 0

"""
def printing(result, moneypool, iterations, current_side, blackorred):
    print(result + ' Moneypool:' + str(moneypool) + ' Iteration:' + str(iterations) + ' bet side:' + str(current_side) + ' wheel side:' + str(blackorred))
"""


def main():
    moneypool = 1000000
    moneycurrentbet = 10
    iterations = 0
    side = 0
    moneygoal = 2000000
    while 0 < moneypool < moneygoal:
        iterations += 1
        current_side = currentside(side)
        blackorred = black_or_red()
        if blackorred == current_side:
            moneypool += moneycurrentbet
            side += 1
            #printing('win', moneypool, iterations, current_side, blackorred)
            moneycurrentbet = 10
        if blackorred != current_side:
            moneypool -= moneycurrentbet
            moneycurrentbet *= 2
            #printing('loose', moneypool, iterations, current_side, blackorred)
    return moneypool


def result():
    win = 0
    loose = 0
    for i in range(100):
        if main() > 0:
            win += 1
        else:
            loose += 1
    print("loose:" + str(loose) + " win:" + str(win))


result()
