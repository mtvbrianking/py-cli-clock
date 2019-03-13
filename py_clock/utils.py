def get_file_contents(file):
    """
    Utility function to read contents of a file.

    Will only read files in current path

    :param file: Specifies the file to read
    :return: File contents
    """
    return open(file).read()


# import os.path as path

# two_up =  path.abspath(path.join(__file__ ,"../.."))
