def input_file():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите название файла")
    file = input()
    
    f = open(file, "r", encoding='utf-8')
    equations = []
    k = 0
    for line in f:
        if k == 0:
            n_x_vars = int(line.replace('\n', ''))
        elif k == 1:
            function = line.replace('\n', '')
        else:
            equations.append(line.replace('\n', ''))
        k += 1
    
    function = function.split(', ')
    
    return function, equations, n_x_vars
    

def input_console():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите функцию и цель исследования - min/max - через запятую и пробел после нее")
    function = input().split(', ')
    
    print("Введите количество переменных:")
    n_x_vars = int(input())
    
    print("Введите количество ограничений:")
    n = int(input())
    
    print(f"На каждой строке через enter введите {n} ограничений:")
    equations = []
    for i in range(n):
        equations.append(input())
        
    return function, equations, n_x_vars