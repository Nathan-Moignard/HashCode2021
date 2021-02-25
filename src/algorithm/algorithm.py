from src.read import Inputfile
from src.output import Output

from sys import argv


def algo(inp: Inputfile):
    output = Output(argv[1])
    
    for index in range(0, inp.intersection):
        output.addIntersection(index)
    for street in inp.streets:
        for inter in output.lights:
            if street[1] == inter.intersection:
                inter.add(street[3], street[2])
    output.print()
    return 0