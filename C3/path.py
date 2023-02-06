import os


def dir_viewer():
    _path = input('type path to the file or folder: ')
    os.walk(_path)
    print(os.listdir())


dir_viewer()

