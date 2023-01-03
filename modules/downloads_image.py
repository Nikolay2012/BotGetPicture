'''
    У файлі downloads_image.py ми створюємо функцію search_path, 
    яка задає абсолютний шлях до вказаного імені файлу
'''
# Підключаємо модуль операційної системи для пошуку абсолютного шляху до файлу
import os
# Створюємо функцію пошуку шляху файлу за ім'ям цього файлу
def search_path(name_file):
    # Створюємо змінну яка зберігає в собі 
    # значення абсолютного шляху до файлу download_image.py
    abs_path = os.path.abspath(__file__ + "/..")
    # print(f"\n\tЦе абсолютний шлях до файлу downloads_image.py - {abs_path}\n")
    # Створюємо список імен папок, прибираючи слеш
    abs_path = abs_path.split("/")
    # print(f"\n\tРозділили назви папок по / {abs_path}\n")
    # видаляємо останнє значення з списку імен папок (modules)
    del abs_path[-1]
    # print(f"\n\tВидалили останню папку з шляху - {abs_path}\n")
    # метод join перетворює список в рядковий тип данних додаючи між назвами папок слеш
    abs_path = "/".join(abs_path)
    # print(f"\n\tНовий абсолютний шлях до папки BotGetPicture - {abs_path}\n")
    #До абсолюного шляху, який знайшли, додаемо ім'я файлу
    file_path = os.path.join(abs_path, name_file)
    # print(file_path)
    return file_path
