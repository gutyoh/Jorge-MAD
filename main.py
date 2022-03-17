import os
import sys
import hashlib


def get_args() -> list[str]:
    args = sys.argv
    if len(args) != 2:
        print("Directory is not specified")
        exit()
    return args


def get_extension() -> str:
    return input("Enter file format:\n")


def get_sorting() -> int:
    print("\nSize sorting options:\n1. Descending\n2. Ascending\n")
    while True:
        sorting = int(input("Enter a sorting option:\n"))
        if sorting in {1, 2}:
            return sorting
        print("\nWrong option\n")


def find_files_size(args, ext='', sorting=1) -> dict:  # find files with the same size and sort it
    files = dict()
    for r, d, f in os.walk(args[1], topdown=False):
        for name in f:
            if ext == '' or ('.' + ext) == os.path.splitext(name)[1]:
                path = os.path.join(r, name)
                files[path] = os.path.getsize(path)

    sizes = [value for value in files.values()]
    sorted_sizes = sorted({s for s in sizes if sizes.count(s) > 1}, reverse=False if sorting == 2 else True)

    result = {i: list() for i in sorted_sizes}
    for key, value in files.items():
        if value in sorted_sizes:
            result[value].append(key)
    return result


def show_files_size(table):
    for key in table.keys():
        print(f"\n{key} bytes", '\n'.join(table.get(key)), sep='\n', end='\n')


def get_user_input(message):
    while True:
        choice = input(message)
        if choice in {"yes", "no"}:
            print()
            return choice
        print("\nWrong option")


def find_duplicates(table) -> dict:  # calculate hash, find duplicates, store it
    checked_files = dict()

    for size, files in table.items():
        for file in files:
            with open(file, 'rb') as f:
                m = hashlib.md5()
                m.update(f.read())
                hash = m.hexdigest()

                if (size, hash) in checked_files:
                    checked_files[(size, hash)].append(file)
                else:
                    checked_files[(size, hash)] = [file]

    return {keys: values for keys, values in checked_files.items() if len(values) > 1}


def show_duplicates(table):
    count = 0
    current_size = -1
    for key in table.keys():
        if key[0] != current_size:
            current_size = key[0]
            print(f"{key[0]} bytes")
        print(f"Hash: {key[1]}")
        for file in table.get(key):
            count += 1
            print(f"{count}. {file}")


def get_del_numbers(table) -> list[int]:
    while True:
        numbers = input("Enter file numbers to delete:\n").split()
        if not numbers:
            print("\nWrong format")
            continue
        for i in numbers:
            if not i.isdigit() or int(i) not in range(1, len(table) + 1):
                print("\nWrong format")
                break
        else:
            return [int(i) for i in numbers]


def delete_duplicates(table):
    files = [(file, key[0]) for key, value in table.items() for file in value]
    numbers = get_del_numbers(files)

    free_space = 0
    for i in numbers:
        os.remove(files[i - 1][0])
        free_space += files[i - 1][1]

    print(f"\nTotal freed up space: {free_space} bytes")


def main():
    args = get_args()
    ext = get_extension()
    sorting = get_sorting()
    files = find_files_size(args, ext, sorting)
    show_files_size(files)
    if get_user_input("\nCheck for duplicates?\n") == "yes":
        checked_files = find_duplicates(files)
        show_duplicates(checked_files)
        if get_user_input("\nDelete files?\n") == "yes":
            delete_duplicates(checked_files)


if __name__ == '__main__':
    main()