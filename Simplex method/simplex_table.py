from fractions import Fraction
import pandas as pd


def make_coeff_table(n_x_vars, equations, function):
    """
    По заданным ограничениям строим симплекс-таблицу
    
    Args:
        param n_x_vars (int): Количество переменных
        param equations (list): Ограничения
        param function (list): Тип исследования функции и сама функция

    Returns:
        coeff_table (DataFrame): Исходная симплекс-таблица
        columns (list): Названия столбцов симплекс-таблицы
    """

    n_s_vars = 0
    total_vars = n_x_vars

    # добавление слабых переменных в ограничения
    for equation in equations:
        if '>=' in equation or '<=' in equation:
            n_s_vars += 1
            total_vars += 1

    coeff_table = [[Fraction("0/1") for i in range(total_vars + 1)] for j in range(len(equations) + 1)]
    s_index = n_x_vars  # индекс, начиная с которого будут располагаться значения s в матрице

    for i in range(1, len(equations) + 1):
        equation = equations[i - 1].split(
            ' ')  # разбиваем ограничение по пробелам, чтобы уметь доставать любую переменную, коэффициент или операцию

        for j in range(len(equation)):
            if 'x_' in equation[j]:
                coeff, index = equation[j].split(
                    'x_')  # т.к. переменные у нас вида ax_i, то разделяя по x_, вытаскиваем коэффициент и индекс переменной

                if equation[j - 1] == '-':
                    coeff_table[i][int(index) - 1] = Fraction("-" + coeff)
                else:
                    coeff_table[i][int(index) - 1] = Fraction(coeff)

            elif equation[j] == '<=':
                coeff_table[i][s_index] = Fraction("1/1")
                s_index += 1

            elif equation[j] == '>=':
                coeff_table[i][s_index] = Fraction("-1/1")
                s_index += 1

            if j == len(equation) - 1:
                if equation[j - 1] == '-':
                    coeff_table[i][total_vars] = Fraction("-" + equation[j])
                else:
                    coeff_table[i][total_vars] = Fraction(equation[j])

    goal_function = function[0].split(' ')

    for j in range(len(goal_function)):
        if 'x_' in goal_function[j]:
            if function[1] == 'max':
                coeff, index = goal_function[j].split('x_')

                if goal_function[j - 1] == '-':
                    coeff_table[0][int(index) - 1] = Fraction(coeff)
                else:
                    coeff_table[0][int(index) - 1] = Fraction("-" + coeff)
            else:
                coeff, index = goal_function[j].split('x_')

                if goal_function[j - 1] == '-':
                    coeff_table[0][int(index) - 1] = Fraction("-" + coeff)
                else:
                    coeff_table[0][int(index) - 1] = Fraction(coeff)

    columns = []
    for i in range(n_x_vars):
        columns.append(f"x_{i + 1}")

    for i in range(n_s_vars):
        columns.append(f"s_{i + 1}")

    columns.append('basic')

    coeff_table = pd.DataFrame(coeff_table, columns=columns)

    return coeff_table, columns
