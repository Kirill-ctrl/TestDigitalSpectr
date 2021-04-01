import itertools
import math
from random import randint
from typing import List, Tuple


class Plane:
    first_elem = None
    parameter_reverse = {
        "I": True,
        "II": True,
        "III": False,
        "IV": False
    }

    def __init__(self,
                 n: int,
                 cords: List[Tuple]):
        self.n = n
        self.cords = cords
        self.angle = (math.pi + 1, 10001)
        self.arr_I = []
        self.arr_II = []
        self.arr_III = []
        self.arr_IV = []

    def sorted_by_part_plane(self, array):
        for cord, distance, acos_angle in array:
            if math.isfinite(acos_angle):
                if 0 <= acos_angle <= math.pi / 2:
                    if (math.pi / 2 - acos_angle) <= self.angle[0] and distance < self.angle[1]:
                        if self.first_elem:
                            self.arr_I.append(self.first_elem)
                        self.first_elem = (cord, distance, acos_angle)
                        self.angle = ((math.pi / 2 - acos_angle), distance)
                    else:
                        self.arr_I.append((cord, distance, acos_angle))
                if math.pi / 2 < acos_angle <= math.pi:
                    self.arr_II.append((cord, distance, acos_angle))
                if -math.pi < acos_angle <= -(math.pi / 2):
                    self.arr_III.append((cord, distance, acos_angle))
                if -(math.pi / 2) <= acos_angle < 0:
                    self.arr_IV.append((cord, distance, acos_angle))
            else:
                self.first_elem = (cord, distance, acos_angle)
        return self.assembly_result()

    @staticmethod
    def sorted_with_lambda(*args, **kwargs):
        for arg, part in zip(args, kwargs['dict']):
            arg.sort(key=lambda x: (x[0], x[1]), reverse=kwargs['dict'][part])
        return [*args]

    def assembly_result(self):
        sorted_array = self.sorted_with_lambda(self.arr_I, self.arr_II, self.arr_III, self.arr_IV,
                                               dict=self.parameter_reverse)
        sorted_array.append(sorted_array.pop(0))
        if self.first_elem:
            return [self.first_elem] + list(itertools.chain.from_iterable(sorted_array))
        return [self.first_elem] + list(itertools.chain.from_iterable(sorted_array))

    def get_acos_angle(self, distances_array):
        acos_angle = []
        for cord, distance in list(zip(self.cords, distances_array)):
            if distance == 0:
                acos_angle.append(math.nan)
            elif cord[1] >= 0:
                acos_angle.append(math.acos(cord[0] / distance))
            elif cord[1] < 0:
                acos_angle.append(-(math.acos(cord[0]/distance)))
        array = list(zip(self.cords, distances_array, acos_angle))
        return self.sorted_by_part_plane(array)

    def get_list_distances(self):
        distances_array = [math.sqrt(item[0] ** 2 + item[1] ** 2) for item in self.cords]
        return self.get_acos_angle(distances_array), distances_array

    def get_result(self):
        result_arr, distances_array = self.get_list_distances()
        return min(distances_array), max(distances_array), sum(distances_array) / self.n, result_arr


if __name__ == "__main__":
    n = int(input())
    arr = [(randint(-100, 100), randint(-100, 100)) for i in range(n)]
    min_result, max_result, average, result_array = Plane(n, arr).get_result()
    print("Min: ", min_result)
    print("Max: ", max_result)
    print("Average: ", average)
    for elem, i in zip(result_array, range(n)):
        print(elem[0])
