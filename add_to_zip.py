import os.path
from zipfile import ZipFile


def add_to_zip(zip_file: str, file_to_add: str) -> None:
    """
    Добавление файла в архив
    :param zip_file: Название архива zip
    :param file_to_add: Файл для добавления в архив zip_file
    :return: None
    """
    if os.path.isfile(zip_file):
        zip_mode = 'a'
    else:
        zip_mode = 'w'
    with ZipFile(zip_file, mode=zip_mode) as zip_to_write:
        zip_to_write.write(file_to_add)


add_to_zip('module1_html.zip', 'index.html')