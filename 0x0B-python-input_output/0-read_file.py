#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads the contents of a UTF-8 text file and prints it to the standard output.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Raises:
        FileNotFoundError: If the specified file cannot be found.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf8") as file:
        content = file.read()
        print(content)
