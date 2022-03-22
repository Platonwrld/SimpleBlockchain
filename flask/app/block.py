import json         # для работы с json форматом
import os
import hashlib


bd = os.curdir + '/blocks/'


# хеш будет считаться из предыдущего блока
def get_hash(filename):
    
    file = open(bd + filename, "rb").read()     # rb - означает, что файл будет откнываться как бинарный файл
    return hashlib.md5(file).hexdigest()


def get_files():

    files = os.listdir(bd)                                 # получение списка файлов из папки blockchain (список несортированных строк)
    return sorted([int(i) for i in files])                             # сортировка полученных строк по целому числу и по порядку
    


def check_integrity():                                              # считывает хеш предыдущего блока,вычисляет хеш предыдущего блока и сравнивает оба эти значения

    files = get_files()

    results = []

    for file in files[1:]:                                          # итерация файла, берется каждый из списка файл и прокручивается через цикл
        f = open(bd + str(file))
        h = json.load(f)['hash']                                   # method load - take object and return json object, hash - it is key in the block file, we get hash from the block file and compare it with hash that we get after function get_hash
        prev_file = str(file - 1)                                   # previouse hash
        actual_hash = get_hash(prev_file)                           # getting the actual hash
        if h == actual_hash:
            res = 'OK'
        else:
            res = 'Corrupted'
        
        results.append({'block': prev_file, 'result': res})

    return results


def write_block(name, amount, to_whom, prev_hash=''):                      # создание записи
    
    files = get_files()

    prev_file = files[-1]
    file_name = str(prev_file + 1)

    prev_hash = get_hash(str(prev_file))        # хеш предыдущего блока
    
    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash}
    
    with open(bd + file_name, "w") as file:                             # сохранение файла в формате json
        json.dump(data, file, indent=4, ensure_ascii=False)     # ensure_ascii - строки будут записываться, такими какие они есть


def main():
    write_block("Katya", '890', "Stepan")
    print(check_integrity())


if __name__ == "__main__":      # значит, что если скрипт будет запущен из консоли, то будет выполнена функция main, если этот код будет как import block, то функция не будет выполнена
    main()