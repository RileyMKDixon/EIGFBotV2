#Project: EIGF Discord Bot
#Author: Riley Dixon
#Class: BigNumber
#Version: v0.1
#Purpose: An alternate way to store numbers. Useful so user does not have
#         To type out the entire integer by hand.
#         As the game does not deal with negative numbers, this module
#         will ignore supporting negative numbers.
#         Expected Regex: "^[\d]+(\.[\d]*)?.{0,2}$"
#Changelog:
# v0.1 - Create class stub.

import re

class BigNumber():
    numberPostfix = ["", "k", "M", "B", "T", "q", "Q", "s", "S", "o", "N",
                      "d", "U", "D", "Td", "qd", "Qd", "sd", "Sd", "od", "Nd",
                      "V", "uV", "dV", "TV", "qV", "QV", "A Lot"]
    regexPattern = re.compile("^[\d]+(\.[\d]*)?.{0,2}$")
    
    def doubleToBigNumber(doubleNum):
        pass

    def bigNumberToDouble(bigNumber):
        pass

    def isValidBigNumber(bigNumber):
        return BigNumber.regexPattern.fullmatch(bigNumber)