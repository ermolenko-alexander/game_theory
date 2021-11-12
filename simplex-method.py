import numpy as np


def simplex(n_vars, equations, function):
    """
    :param vars: Число переменных в задаче ЛП

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
    pass


def input_file():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите название файла")
    file = input()
    
    f = open(file, "r", encoding='utf-8')
    equations = []
    k = 0
    for line in f:
        if k == 0:
            n_vars = line.replace('\n', '')
        elif k == 1:
            function = line.replace('\n', '')
        else:
            equations.append(line.replace('\n', ''))
        k += 1
        
    print(function, equations, n_vars)
    
    return function, equations, n_vars
    

def input_console():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите функцию и цель исследования - min/max - через запятую и пробел после нее")
    function = input().split(', ')
    print(function)
    
    print("Введите количество переменных:")
    n_vars = int(input())
    
    print("Введите количество ограничений:")
    n = int(input())
    
    print(f"На каждой строке через enter введите {n} ограничений:")
    equations = []
    for i in range(n):
        equations.append(input())
        
    return function, equations, n_vars


def input_file():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите название файла")
    file = input()
    
    f = open(file, "r", encoding='utf-8')
    equations = []
    k = 0
    for line in f:
        if k == 0:
            n_vars = line.replace('\n', '')
        elif k == 1:
            function = line.replace('\n', '')
        else:
            equations.append(line.replace('\n', ''))
        k += 1
        
    print(function, equations, n_vars)
    
    return function, equations, n_vars
    

def input_console():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите функцию и цель исследования - min/max - через запятую и пробел после нее")
    function = input().split(', ')
    print(function)
    
    print("Введите количество переменных:")
    n_vars = int(input())
    
    print("Введите количество ограничений:")
    n = int(input())
    
    print(f"На каждой строке через enter введите {n} ограничений:")
    equations = []
    for i in range(n):
        equations.append(input())
        
    return function, equations, n_vars


if __name__ == '__main__':
    print("Укажите как хотите вводить исходные данные: консоль/файл")
    type_input = input().lower()
    
    assert type_input in ['консоль', 'console', 'file', 'файл'], 'Такой тип не поддерживается'
    
    if type_input in ['консоль', 'console']:
        function, equations, n_vars = input_console()
    
    elif type_input in ['file', 'файл']:
        function, equations, n_vars = input_file()
    
    simplex(n_vars, equations, function)