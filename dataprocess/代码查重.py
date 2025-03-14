import difflib


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


def calculate_similarity(file1, file2):
    file1_lines = read_file(file1)
    file2_lines = read_file(file2)

    diff = difflib.SequenceMatcher(None, file1_lines, file2_lines)
    similarity = diff.ratio()

    return similarity


def main(file1, file2):
    similarity = calculate_similarity(file1, file2)
    print(f"The similarity between the files is: {similarity * 100:.2f}%")


if __name__ == "__main__":
    # Replace 'file1.py' and 'file2.py' with the paths to the files you want to compare
    file1 = 'file1.py'
    file2 = 'file2.py'
    main(file1, file2)
