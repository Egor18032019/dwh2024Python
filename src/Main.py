# This is a sample Python script.
from pathlib import Path

import FileService
import Worker
import logging

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('log_file.log')
file_handler.setLevel(logging.DEBUG)
# Форматируем сообщение
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
# Добавляем файловый handler к logger
logger.addHandler(file_handler)


def work(name):
    # Use a breakpoint in the code line below to debug your script.
    logger.info("Запуск приложения.")
    URL = 'https://storage.googleapis.com/kaggle-data-sets/107706/256873/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240723%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240723T061608Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=97a93e78ae4f2fc6786c3ebc576fa5e589ed4e906dfe80e180f5b175df44b9cb249556f133a305ce23d115bb039fe2b33576297c051e6fa69a067485e330b5d6af4a18621f065bc65bb66e2d8deef4a76b6710874f4d25c1b2da1af5ea3e6a6a08ce412f66c1190e474b7eeee7cc561878ca9e248ab615a4983732e9207a502b7cf58faaf1aa1cb699a47e1b87b6ccfeb6b23c0ea4570d3223224dd29d6934a4055ded64d7ed723dc5b9da5d42a4fd23d7df4c4684e883c3c5721268f7c9d1b9e01c640c185cfd64b50789d7ebda7f134508d98567b67843d2391218d1315efaa11f1681489fe9147b66b04972d281bef9ca968f3eb11823f08ff0031f30b6a1'
    file_name = 'archive.zip'
    temp_dir = Path('../temp_dir')
    FileService.download_file(URL, temp_dir, logger)
    try:
        FileService.unzip_file(file_name, temp_dir)
    except Exception as e:
        logger.error('Ошибка при распаковке файла', e)
    data = 'temp_dir/cardio_train.csv'
    try:
        Worker.save_data(data)
    except Exception as e:
        logger.error('Ошибка при сохранении данных', e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    work('PyCharm')
