from pathlib import Path
from pprint import pprint

path = 'cats.txt'

def get_cats_info(path):
    cats = []
    with open(path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
        for line in lines:
            id, name, age = line.split(',')
            cats.append({'id': id, 'name': name, 'age': age})
        return cats

if Path(path).exists():
    cats = get_cats_info(path)
    print(cats)
else:
    print(f'Файлу {path} не існує.')