import argparse
from multiprocessing import Pool


def checking(value: str) -> int:
    """
    Вспомогательная функция для проверки корректности введённых данных
    :param value: значение с командной строки
    :return: int значение
    """
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} не является целым числом")
    if number <= 0:
        raise argparse.ArgumentTypeError(f"{value} должен быть положительным числом")
    return number


def input_data()-> list[int]:
    """
    Получение данных с командной строки
    :return: список int
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("values", type=checking, nargs=4, help="Две пары чисел: n1 m1 n2 m2")
    args = parser.parse_args()
    return args.values

def get_path(n: int, m: int)-> list[int]:
    """
    Функция вычисления пути
    :param n: длина массива
    :param m: интервал
    :return: путь
    """
    path = list()
    cur = 0

    while True:
        path.append(cur + 1)
        cur = (cur + m - 1) % n

        if cur == 0:
            break

    return path

def main()-> None:
    """
    Функция выводит в консоль объединенные пути
    p.s не совсем понял, что значит, что программа должна обрабатывать 2 массива одновременно,
    поэтому я выбрал реальную параллельность, потоки в питоне это имитация параллельности, поскольку gil все равно один,
    а каждый процесс имеет свой личный gil, поэтому в таком случае задачи реально выполняются параллельно
    :return:
    """
    n1, m1, n2, m2 = input_data()

    with Pool(processes = 2) as pool:
        path1, path2 = pool.starmap(get_path, [(n1, m1), (n2, m2)])

    print("".join(map(str, path1 + path2)))

if __name__ == "__main__":
    main()