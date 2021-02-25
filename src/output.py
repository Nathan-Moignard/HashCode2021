#!/usr/bin/env python3

class Street:
    name = 0
    delay = 0

    def __init__(self, new_name, new_delay):
        self.name = new_name
        self.delay = new_delay

    def print(self):
        print(f"{self.name} {self.delay}")

class Intersection:
    intersection = 0
    streets = []

    def __init__(self, intersection_nbr):
        self.intersection = intersection_nbr
        self.streets = []

    def add(self, new_name, new_delay):
        self.streets.append(Street(new_name, new_delay))

    def print(self):
        print(self.intersection)
        for street in self.streets:
            street.print()

class Output:
    lights = []
    file_name = ""

    def __init__(self, file_name):
        self.file_name = file_name

    def addIntersection(self, nbr):
        self.lights.append(Intersection(nbr))

    def addStreet(self, nbr, new_name, new_delay):
        for light in self.lights:
            if light.intersection == nbr:
                light.add(new_name, new_delay)

    def print(self):
        print(f"{len(self.lights)}")
        for light in self.lights:
            light.print()

if __name__ == "__main__":
    output = Output("output")
    output.addIntersection(0)
    output.addIntersection(1)
    output.addStreet(0, "name", 42)
    output.print()
