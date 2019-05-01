#Project: EIGF Discord Bot
#Author: Riley Dixon
#Class: BaseSort
#Version: v0.1
#Purpose: An abstract class for the different sorting algorithms that can be
#         implemented, depending on what kind of sort is wanted.
#         This class should return a string of the teams constructed. 
#Changelog:
# v0.1 - Create stub class.


import abc

class BaseSort(abc.ABC):

    @abc.abstractmethod
    def sort(self):
        pass