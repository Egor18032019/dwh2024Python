import shutil

import requests


def download_file(URL, temp_dir):
    # Отправляем GET-запрос и получаем содержимое файла
    response = requests.get(URL)

    # Проверяем, что ответ содержит данные
    if response.status_code == 200:
        # Создаем папку для хранения загрузок
        temp_dir.mkdir(exist_ok=True)

        # Сохраняем файл в папку
        with open(temp_dir / 'archive.zip', 'wb') as file:
            file.write(response.content)
    else:
        print('Ошибка при скачивании файла. Код статуса:', response.status_code)


def unzip_file(file_name, temp_dir):
    # Распаковываем архив
    shutil.unpack_archive(temp_dir / file_name, temp_dir)
