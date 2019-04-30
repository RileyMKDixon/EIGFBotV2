import abc

class BaseCommand(abc.ABC):
    
    @abc.abstractmethod
    def executeCommand(self):
        pass