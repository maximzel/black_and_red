# black_and_red
Симулятор игры в рулетку по определённой схеме.  Правило игры: игрок начинает с 1000000$ (moneypool). Начальная ставка: 10$ (moneycurrentbet). В рулетке 36 чисел и 0 (0 - нечётное, 1 - чётное, 2 - zero). Игра начинается с начальной ставки на чётное число (side). Если ставка выиграла, меняется сторона ставки (было четное - стало нечетное). Если проигрыш - сторона ставки остается та же, ставка удваивается. moneygoal - цель банка, после которого игра прекращается и считается выигрышной. Проигрыш - когда величина банка становится равна 0. Программа симулирует 100 игр по заданной схеме и выводит кол-во выигрышей и проигрышей.
