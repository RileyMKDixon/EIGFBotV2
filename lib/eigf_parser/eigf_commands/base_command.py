#Project: EIGF Discord Bot
#Author: Riley Dixon
#Class:
#Version:
#Purpose:
#Changelog:



import abc

class BaseCommand(abc.ABC):
    
    @abc.abstractmethod
    def executeCommand(self):
        pass