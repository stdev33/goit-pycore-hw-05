import sys
import pathlib
from colorama import init, Fore, Style


init(autoreset=True)


def print_directory_structure(path, indent=""):
    try:
        base_path = pathlib.Path(path)

        if not base_path.exists():
            print(f"Шлях {path} не існує.")
            return
        if not base_path.is_dir():
            print(f"Шлях {path} не є директорією.")
            return

        for item in base_path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{Style.BRIGHT}{item.name}{Style.RESET_ALL}")
                print_directory_structure(item, indent + "  ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")

    except Exception as e:
        print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python task_3.py /шлях/до/директорії")
    else:
        directory_path = sys.argv[1]
        print_directory_structure(directory_path)