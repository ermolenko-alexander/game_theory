def Gauss(coeff_table, lead_elem, columns):
    """
    Args:
        param coeff_table (DataFrame): Симплекс-таблица
        param lead_elem (tuple): Координаты текущего столбца
        param columns (list): Названия столбцов симплекс-таблицы

    Returns:
        param coeff_table (DataFrame): Симплекс-таблица после преобразования
    """
    return coeff_table