from pathlib import Path

path = 'info.txt'

def total_salary(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
        total = 0
        for line in lines:
            _,salary = line.split(',')
            total += int(salary)
        average = int(total / len(lines))
        return total, average


if Path(path).exists():
    total, average = total_salary(path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
    print(f'Файлу {path} не існує.')