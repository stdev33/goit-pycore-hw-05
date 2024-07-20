import pathlib

current_dir = pathlib.Path(__file__).parent


def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": name, "age": age})
        return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


def main():
    path_to_file = current_dir / "cats_file.txt"
    cats_info = get_cats_info(path_to_file)
    print(cats_info)


if __name__ == "__main__":
    main()
