#Project: EIGF Discord Bot
#Author: Riley Dixon
#Class:
#Version:
#Purpose:
#Changelog:



import abc

class BaseSort(abc.ABC):

    @abc.abstractmethod
    def sort(self):
        pass