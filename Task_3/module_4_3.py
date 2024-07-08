import sys
from pathlib import Path
from colorama import Fore

def visualize_dir_structure(path, indent=''):
    directory = Path(path)

    if not directory.exists():
        print(Fore.RED + "Вказаний шлях не існує.")
        return

    for item in directory.iterdir():
        if item.is_dir():
            print(Fore.GREEN + f"{indent}[DIR] {item.name}")
            new_indent = indent + '    '
            visualize_dir_structure(item, new_indent)
        elif item.is_file():
            print(Fore.BLUE + f"{indent}[FILE] {item.name}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        print(Fore.YELLOW + f"Структура директорії для {directory_path}:")
        visualize_dir_structure(directory_path)
    else:
        print(Fore.RED + "Будь ласка, введіть шлях до директорії як аргумент командного рядка.")