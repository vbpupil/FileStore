import os


class Directory:
    path = None

    def set_path(self, path):
        if isinstance(path, str):
            if self.__directory_exists(path):
                self.path = path
            else:
                raise IOError('Directory does not exist')
        else:
            raise ValueError('Incorrect TYPE, string is required')

    def get_path(self):
        if self.__directory_is_set():
            return self.path
        raise Exception('Directory has not been set.')

    def __directory_is_set(self):
        return self.path != None

    def __directory_exists(self, path):
        return os.path.isdir(path)
