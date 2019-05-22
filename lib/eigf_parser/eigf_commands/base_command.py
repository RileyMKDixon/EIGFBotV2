#Project: EIGF Discord Bot
#Author: Riley Dixon
#Class: BaseCommand
#Version: v0.1
#Purpose: Provides an abstract base class for how each command issued to the
#         bot should act. Each command should instantiate itself with the
#         required data it needs, as well as to implement the required
#         function for each command.
#Changelog:
# v0.1 - Create stub class.



import abc

class BaseCommand(abc.ABC):
    
    isPrivledgedCommand = True #If a command is not privledged, this should be overriden.

    @abc.abstractmethod
    def executeCommand(self):
        pass