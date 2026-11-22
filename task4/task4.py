import argparse

import numpy as np

def input_data()-> str:
    """
    Получение данных с командной строки
    :return: путь к файлу
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path_nums")
    args = parser.parse_args()
    return args.path_nums

def read_file(path)->list[int]:
    """
    Чтение данных с файла
    :param path: путь к файлу
    :return: массив целых чисел
    """
    with open(path, "r", encoding = "utf-8-sig") as file:
        nums = [int(line) for line in file if line.strip()]
    return nums

def get_median(nums: list[int])->int:
    """
    Преобразует список в массив numpy для ускорения вычислений при большом n.
    Медиана ищется numpy.median() - выполняется за линейное время т.к. используется алгоритм медианы медиан, что
    быстрее чем сортировка питона (n log n)+ выбор медианы
    :param nums: список целых чисел
    :return: медиана
    """
    nums_np = np.array(nums)
    return int(np.median(nums_np, overwrite_input = True))

def get_count_step(nums: list[int], target: int)-> int:
    """
    Вычисляет минимальное число ходов
    :param nums: список целых чисел
    :param target: число, к которому мы приводим остальные
    :return: число ходов
    """
    return sum(abs(target - i) for i in nums)

def print_res(count_step:int)->None:
    """
    Выводит в консоль ответ
    :param count_step: количество ходов
    :return:
    """
    if count_step <= 20:
        print(count_step)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")


def main()-> None:
    """
    Основная функция программы
    :return:
    """
    path_nums = input_data()
    nums = read_file(path_nums)
    median = get_median(nums)
    count_step = get_count_step(nums, median)
    print_res(count_step)

if __name__ == "__main__":
    main()