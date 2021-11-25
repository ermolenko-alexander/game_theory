from inputs import input_file, input_console
from simplex_table import make_coeff_table
from iteration import optimality_check


def simplex(n_x_vars, equations, function):
    """
    :param n_x_vars: Число переменных в задаче ЛП

    :param equations: Список элементов типа string со всеми ограничениями:
                        1. правила для переменной:
                            записана с коэффициентом
                            через "_" должен быть прописан ее номер
                        2. используются только одиночные пробелы, между коэффициентом
                            и переменной пробела нет
                        Пример:
                            ['1x_1 + 7x_2 + 2x_3 <= 9', '2x_2 + 4x_1 >= 5', 'x_3 + 2x_2 = 3']

    :param function: Тип list с двумя параметрами:
                            1. min или max
                            2. функция, с которой работаем
    """
    coeff_table, columns = make_coeff_table(n_x_vars, equations, function)

    print("Итоговая симплекс-таблица:")
    print(optimality_check(coeff_table, columns))
    print("Оптимальное решение задачи")
    # TO-DO (Влад)


if __name__ == '__main__':
    print("Укажите как хотите вводить исходные данные: консоль/файл")
    type_input = input().lower()

    assert type_input in ['консоль', 'console', 'file', 'файл'], 'Такой тип не поддерживается'

    if type_input in ['консоль', 'console']:
        function, equations, n_x_vars = input_console()

    elif type_input in ['file', 'файл']:
        function, equations, n_x_vars = input_file()

    simplex(n_x_vars, equations, function)
