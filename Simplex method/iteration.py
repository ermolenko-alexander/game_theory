from Gauss import Gauss
import numpy as np


def unlimited_check(coeff_table, lead_column):
    """
    Условие неограниченности задачи ЛП:
        Если в ведущем столбце s нет положительных коэффициентов,
        то значение задачи ЛП не ограничено (нет оптимального решения)
        
    Иначе:
        в качестве выводимой из базиса переменной x_r выбирается переменная,
        для которой:
            b_r / a_rs = min(b_i / a_is), a_is > 0
        r - ведущая строка (lead_row)
        a_rs - ведущий элемент
        
    Возвращает номер ведущей строки
    """
    fl = coeff_table[lead_column][1:].all() <= 0
    
    if fl:
        print("Нет оптимального решения")
    else:
        a_rs = np.array(coeff_table[lead_column][1:])
        b = np.array(coeff_table['basic'][1:])
        
        res = []
        i = 0
        for a in a_rs:
            if a > 0:
                res.append(a / b[i])
                i += 1

        return min(res)


def optimality_check(coeff_table, columns):
    """
    Проверка условия оптимальности:
        Если все коэффициенты в нулевой строке симплексной таблицы,
        соответствующие целевой функции, неотрицательны, то текущее
        базисное решение оптимально
    
    Если существуют коэффициенты <0, то текущее базисное решение
    можно улучшить за счет введения в базис переменной, выбирающейся из условия: 
    c_s = min c_j; c_j<0
    
    Когда ведущий столбец найден, проверяем условие неограниченности и ищем ведущую строку
    Далее преобразовываем симлекс-таблицу с помощью метода Гаусса
    """
    fl = (coeff_table.iloc[0]).all() > 0
    
    while not fl:
        row_0 = np.array(coeff_table[coeff_table.columns[:-1]].loc[0])
        
        min_c = row_0.min()
        lead_column = row_0.argmin()
        lead_column = columns[lead_column]
        
        if fl:
            return coeff_table
        else:
            lead_row = unlimited_check(coeff_table, lead_column)
            lead_elem = (lead_row, lead_column)
            #coeff_table = Gauss(coeff_table, lead_elem, columns)
            fl = True
    
     # lead_elem = coeff_table[row_index][column_index]
    return coeff_table