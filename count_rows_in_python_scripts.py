import datetime
import os


def get_count_rows_in_python_scripts(work_dir, venv_folder_name):
    c_lines = 0

    for filename in os.listdir(work_dir):
        filepath = os.path.join(work_dir, filename)

        # Исключаем директории с именем venv_folder_name
        if os.path.isdir(filepath) and filename == venv_folder_name:
            continue

        # Рекурсивно обрабатываем вложенные директории
        if os.path.isdir(filepath):
            c_lines += get_count_rows_in_python_scripts(filepath, venv_folder_name)
            continue

        # Считаем количество строк в файле с расширением .py
        if filename.endswith(".py"):
            # Проверяем, что дата создания файла не позже года назад
            file_created = os.path.getctime(filepath)
            file_created_date = datetime.date.fromtimestamp(file_created)
            today = datetime.date.today()
            one_year_ago = today - datetime.timedelta(days=365)

            if file_created_date >= one_year_ago:
                with open(filepath, encoding="utf-8") as f:
                    lines = f.readlines()
                    c_lines += len(lines)

    return c_lines


if __name__ == "__main__":

    while True:
        directory = input('Укажите директорию, в которой лежат Python проекты ( "." - текущая директория): ')
        venv_folder_name = input('Укажите имя виртуальной среды, которое используется в проектах: ')

        if len(directory) == 0 or venv_folder_name == 0:
            print("Пожалуйста, введите название директории и имя виртуальной среды")

        if not os.path.isdir(directory):
            print("Неверно указан путь к директории. Пожалуйста, повторите попытку")

        else:
            print(get_count_rows_in_python_scripts(work_dir=directory, venv_folder_name=venv_folder_name))
            break
