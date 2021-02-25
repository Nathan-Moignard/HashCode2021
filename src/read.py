from typing import Tuple, List, Union

t_begin = int
t_end = int
t_time = int
t_roads = Tuple[t_begin, t_end, t_time, str]
t_car = List[str]


class Inputfile:
    def __init__(self, adress):
        self.time = 0
        self.intersection = 0
        self.street_number = 0
        self.car_number = 0
        self.points = 0
        self.car: List[t_car] = []
        self.streets: List[t_roads] = []
        self.get(adress)

    def read_file(self, adress):
        f = open(adress)
        txt = f.readlines()
        separation = []
        for k in txt:
            separation.append(k.rsplit())
        f.close()
        return separation

    def add_road(self, line):
        temp: t_roads = (int(line[0]), int(line[1]), int(line[3]), line[2])
        self.streets.append(temp)

    def add_car(self, line):
        temp: t_car = []
        for k in line[1:]:
            temp.append(k)
        self.car.append(temp)

    def first_line_info(self, f_line):
        if len(f_line) != 5:
            print("NO good first line")
            return
        self.time = int(f_line[0])
        self.intersection = int(f_line[1])
        self.street_number = int(f_line[2])
        self.car_number = int(f_line[3])
        self.points = int(f_line[4])

    def get(self, adress):
        mfile = self.read_file(adress)
        self.first_line_info(mfile[0])
        for i in range(1, self.street_number + 1):
            self.add_road(mfile[i])
        for line in mfile[self.street_number + 1:]:
            self.add_car(line)