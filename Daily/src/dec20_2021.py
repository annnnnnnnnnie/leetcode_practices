# No 475. Heaters
# https://leetcode-cn.com/problems/heaters/
import math
from typing import List


def find_radius(house_positions, heater_positions):
    house_positions = sorted(house_positions)
    heater_positions = sorted(heater_positions)

    assert heater_positions
    heater_start_index = 0

    distances = []
    for house_position in house_positions:
        h_index, distance = find_nearest_heater(house_position, heater_positions, heater_start_index)
        distances.append(distance)
        heater_start_index = h_index
    result = max(distances)
    return result


def find_nearest_heater(house_position, heater_positions, heater_start_index):
    """
    Find the index of the nearest heater as well as the distance to that heater
    Will start finding from heater_start_index.
    :param house_position: Sorted list of the positions
    :param heater_positions: Sorted list of the positions
    :param heater_start_index: Only consider index >= start index
    :return: (index, distance)
    """
    min_distance = abs(house_position - heater_positions[heater_start_index])
    best_h_index = heater_start_index
    for h_index in range(heater_start_index, len(heater_positions)):
        current_distance = abs(house_position - heater_positions[h_index])
        if current_distance < min_distance:
            min_distance = current_distance
            best_h_index = h_index
        elif current_distance > min_distance:
            break
    return best_h_index, min_distance


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        return find_radius(houses, heaters)
