from utils.dtime import now


def save_to_file(content, filename):
    with open(filename, "w") as f:
        f.write(content)

    print(f"File [{filename}] Was Saved at [{now()}]")


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()  # entire string


def read_lines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
