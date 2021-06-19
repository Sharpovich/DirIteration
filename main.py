import os
import random as r
import shutil  # Библиотека для перемещения


def main():
    PATH = os.getcwd()
    name_directory = input(
        "Введите наименование папки с миниатюрами: ")
    name_txt_file = input(
        "Введите наименование текстового файла\
            с наименованиями миниатюр .txt: ")
    all_file_directory = os.listdir(f"{PATH}\\{name_directory}")

    # Открытие и чтение файла со списком наименований изображений
    with open(f"{PATH}\\{name_directory}\\{name_txt_file}", "r") as f:
        target_file_array = f.read().split("\n")

    result_array = list(set(all_file_directory) & set(
        target_file_array))  # объединение списков

    array_list_white = []
    size_control = 0
    for i in result_array:  # берет каждый из списка
        mb_size = os.path.getsize(  # считает размер
            f"{os.getcwd()}\\{name_directory}\\{i}")/1000000
        size_control += mb_size  # увеличение до порога
        if size_control < 5.0:
            array_list_white.append(i)
        else:
            array_list_white.append(i)
            dir_name = f"Direct{r.randint(0,200)}{r.randint(0,200)}"
            new_path = f"{PATH}\\{name_directory}\\{dir_name}"
            os.mkdir(new_path)
            for i in array_list_white:
                shutil.move(f"{PATH}\\{name_directory}\\{i}",
                            f"{new_path}\\{i}")
            size_control = 0
            array_list_white.clear()
            continue
    dir_name = f"Direct{r.randint(0,200)}{r.randint(0,200)}"
    new_path = f"{PATH}\\{name_directory}\\{dir_name}"
    os.mkdir(new_path)
    for i in array_list_white:
        shutil.move(f"{PATH}\\{name_directory}\\{i}",
                    f"{new_path}\\{i}")


if __name__ == "__main__":
    main()
