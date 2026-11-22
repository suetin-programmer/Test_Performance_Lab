import argparse
import json
from typing import Any, Dict
from jsonpath_ng import parse

def input_data()-> tuple[str, str, str]:
    """
    Получение данных с командной строки
    :return: кортеж путей
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path_values_file",)
    parser.add_argument("path_tests_file", )
    parser.add_argument("path_result_file", )
    args = parser.parse_args()
    return args.path_values_file, args.path_tests_file, args.path_result_file


def load_json(path: str )-> Dict[Any, Any]:
    """
    Чтение json файла
    :param path: путь к файлу
    :return: Словарь из json файла
    """
    with open(path, encoding = "utf-8-sig" ) as file:
        return json.load(file)

def write_json(path: str, data:Dict[Any, Any])->None:
    """
    Запись результата в json файл
    :param path: путь к файлу
    :param data: данные
    :return:
    """
    with open(path, "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent = 2)

def get_res_id(data: dict[str, Any])-> dict[int, Any]:
    """
    Преобразование словаря values
    :param data:
    :return:
    """
    return {i.get("id"): i.get('value') for i in data.get('values')}

def fill_test(tests, values):
    """
    Заполнение словаря tests данными из values
    :param tests: словарь tests
    :param values: словарь values
    :return:
    """
    for i in parse("$..value").find(tests):
        parent = i.context.value

        if not isinstance(parent, dict):
            continue

        test_id = parent.get("id")

        if test_id is None:
            continue

        if test_id in values:
            parent["value"] = values[test_id]

def main()-> None:
    """
    Основная функция программы
    :return:
    """
    path_values, path_tests, path_result = input_data()

    values = get_res_id(load_json(path_values))
    tests = load_json(path_tests)

    fill_test(tests, values)

    write_json(path_result, tests)

if __name__ == "__main__":
    main()