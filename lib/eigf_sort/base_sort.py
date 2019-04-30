import abc

class BaseSort(abc.ABC):

    @abc.abstractmethod
    def sort(self):
        pass