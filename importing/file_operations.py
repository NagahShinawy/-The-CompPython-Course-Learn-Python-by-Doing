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


if (
    __name__ == "__main__"
):  # means checking Are you running the file as script or running it from as module from another file ?
    print(f"You are Running {__name__}")

    # if you are running it as script from itself ==> __name__ = main
    # if you are running it as module from another file  ==>
    # __name__ = "filename" ==> in this case filename is "file_operations"
