import os
from time import strftime, localtime

directory = '.'
directory_norm = os.path.normpath(directory)
for root, dirs, files in os.walk(directory_norm):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(file)
        formatted_time = strftime('%d.%m.%Y %H:%M', localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(__file__)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')