import numpy as np


def Gauss(coeff_table, lead_elem, columns):
    """
    Args:
        param coeff_table (DataFrame): Симплекс-таблица
        param lead_elem (list): Координаты текущего столбца
        param columns (list): Названия столбцов симплекс-таблицы
    Returns:
        param coeff_table (DataFrame): Симплекс-таблица после преобразования
    """
    # Изменяем строки методом Гаусса
    for i in range(coeff_table.shape[0]):
        x = -coeff_table.iloc[i, lead_elem[1]] / coeff_table.iloc[lead_elem]
        if i != lead_elem[0]:
            coeff_table.iloc[i] = coeff_table.iloc[i] + coeff_table.iloc[lead_elem[0]] * x

    # Находим базис и меняем индексы
    indexes = coeff_table.index
    for i in range(coeff_table.shape[1]):
        if np.count_nonzero(coeff_table.iloc[:, i]) == 1:
            non_zero_index = np.nonzero(coeff_table.iloc[:, i].to_numpy())[0][0]  # Индекс строки ненулевого элемента в колонке
            coeff_table.rename(index={indexes[non_zero_index]: columns[i]}, inplace=True)

    return coeff_table
