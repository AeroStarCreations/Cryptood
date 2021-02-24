""" This is an abstract class for objects that represents entries/rows in SQLite databases """

import abc

class DbEntry(object, metaclass=abc.ABCMeta):
    _NOT_IMPLEMENTED_ERROR_MESSAGE = 'Method __str__ must be defined to use this class.'

    @abc.abstractmethod
    def get_tuple(self):
        raise NotImplementedError(self._NOT_IMPLEMENTED_ERROR_MESSAGE)

    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError(self._NOT_IMPLEMENTED_ERROR_MESSAGE)

