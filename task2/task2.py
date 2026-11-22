import argparse
from fractions import Fraction

def get_data(path: str)-> list[tuple[Fraction, ...]]:
    """
    Функция получения данных из файла, так как работаем с мат вычислениями, точность важна, то используем fraction, а
    не float.
    :param path: путь к файлу
    :return: массив пар данных
    """

    with open(path, "r", encoding="utf-8-sig") as file:
        pairs = [
            tuple(map(Fraction, line.split()))
            for line in file
            if line.strip()
        ]


    return pairs

def dot_is_circle(circle: list[tuple[Fraction,...]], dots: list[tuple[Fraction, ...]])->list[int]:
    """
    Проверяет принадлежит ли точка эллипсу, формирует список со значениями
    0 - лежит на окружности, 1 - принадлежит, 2 - не принадлежит
    :param circle: координаты центра эллипса и значение полуосей
    :param dots: координаты точек
    :return: list
    """
    x_o, y_o = circle[0]
    x_a, y_b = circle[1]
    a = abs(x_a - x_o)
    b = abs(y_b - y_o)
    if a == 0 or b == 0:
        raise ValueError("Вырожденный эллипс")
    arr = list()
    for x, y in dots:
        term = ((x - x_o) ** 2/(a ** 2) + (y - y_o) ** 2/(b ** 2))
        if term == 1:
            arr.append(0)
        elif term < 1:
            arr.append(1)
        else:
            arr.append(2)
    return arr

def input_data()-> tuple[str, str]:
    """
    Получение данных с командной строки
    :return: кортеж путей
    """

    parser = argparse.ArgumentParser(description="Положение точек относительно эллипса")
    parser.add_argument("path_circle_file",)
    parser.add_argument("path_dots_file", )
    args = parser.parse_args()
    return args.path_circle_file, args.path_dots_file

def main()-> None:
    """
    Выводит в консоль принадлежность точек заданному эллипсу
    :return:
    """

    path_circle, path_dots = input_data()

    circle = get_data(path_circle)
    dots = get_data(path_dots)

    arr = dot_is_circle(circle, dots)
    print(*arr, sep = "\n")

if __name__ == "__main__":
    main()