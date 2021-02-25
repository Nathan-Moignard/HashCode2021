##
## EPITECH PROJECT, 2021
## HashCode2021
## File description:
## value
##

from src.read import Inputfile
from src.algorithm.algorithm import algo

def main(arguments):
    if (len(arguments) < 2):
        print("File missing")
        return 84
    inp = Inputfile(arguments[1])
    print(inp.car)
    print(inp.streets)
    return (algo(inp))