class File:

    def __init__(self, path):
        self.__path = path

    def getCanonicalPath(self):
        import os
        return os.path.abspath(self.__path)
