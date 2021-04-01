import itertools
import math
from random import randint
from typing import Tuple, List


class Plane:
    parameter_reverse = {
        "I": True,
        "II": True,
        "III": False,
        "IV": False
    }
    coord_x = 100

    def __init__(self,
                 n: int,
                 cords: List[Tuple]):
        self.n = n
        self.cords = cords
        self.arr_I = []
        self.arr_II = []
        self.arr_III = []
        self.arr_IV = []
        self.first_elem = None

    def sorted_by_part_plane(self):
        for j in range(self.n):
            x = self.cords[j][0]
            y = self.cords[j][1]
            if x >= 0 and y >= 0:
                if x < self.coord_x:
                    if self.first_elem:
                        self.arr_I.append(self.first_elem)
                    self.first_elem = (x, y)
                    self.coord_x = x
                else:
                    self.arr_I.append((x, y))
            if x < 0 <= y:
                self.arr_II.append((x, y))
            if x <= 0 and y < 0:
                self.arr_III.append((x, y))
            if x > 0 >= y:
                self.arr_IV.append((x, y))

    @staticmethod
    def sorted_with_lambda(*args, **kwargs):
        for arg, part in zip(args, kwargs['dict']):
            arg.sort(key=lambda x: (x[0], x[1]), reverse=kwargs['dict'][part])
        return [*args]

    def assembly_result(self):
        sorted_array = self.sorted_with_lambda(self.arr_I, self.arr_II, self.arr_III, self.arr_IV, dict=self.parameter_reverse)
        sorted_array.append(sorted_array.pop(0))
        if self.first_elem:
            return [self.first_elem] + list(itertools.chain.from_iterable(sorted_array))  # self.arr_II + self.arr_III + self.arr_IV + self.arr_I
        return [self.first_elem] + list(itertools.chain.from_iterable(sorted_array))

    def get_list_distances(self):
        distances_array = []
        for item in self.assembly_result():
            print(item)
            distances_array.append(math.sqrt(item[0] ** 2 + item[1] ** 2))
        return distances_array

    def get_result(self):
        distances_array = self.get_list_distances()
        return min(distances_array), max(distances_array), sum(distances_array) / self.n

    def main(self):
        self.sorted_by_part_plane()
        return self.get_result()


if __name__ == "__main__":
    n = int(input())
    arr = [(randint(-100, 100), randint(-100, 100)) for i in range(n)]
    min_result, max_result, average = Plane(n, arr).main()
    print("Min: ", min_result)
    print("Max: ", max_result)
    print("Average: ", average)
