import os


def dir():
    while True:
        way = input('Введите путь к файлу:')
        if os.path.isdir(way) == True:
            return way
        else:
            print('Вы ввели неправильный путь к файлу')


def dict_way_size(way):
    dict1 = {}
    for root, dirs, files in os.walk(way):
        for file in files:
            newkey = {os.path.join(root, file): os.path.getsize(root + '\\' + file)}
            dict1.update(newkey)
    print(dict1)


def analysis():
    pass


def duplicate():
    pass


if __name__ == '__main__':
    dict_way_size(dir())
