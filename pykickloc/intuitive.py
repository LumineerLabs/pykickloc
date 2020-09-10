import copy
import math

import numpy as np


class KickLocIntuitive:
    def __init__(self, position: np.ndarray = np.array([0, 0, 0]), standard_deviation: float = 1000):
        self.standard_deviation = standard_deviation
        self.position = copy.deepcopy(position)

    def update(self,
               neighbor_position: np.ndarray,
               neighbor_standard_deviation: float,
               measured_distance: float,
               distance_standard_deviation: float):
        if self.standard_deviation == 0:
            # standard devations of 0 are beacons and should not be moved by this algorithm
            return
        if np.array_equal(self.position, neighbor_position) and measured_distance > 0:
            # this gives the algorithm a kick to work with, if they happen to be located at the same point
            delta_position = np.array([np.finfo(float).eps, np.finfo(float).eps, np.finfo(float).eps])
        else:
            delta_position = neighbor_position - self.position
        expected_distance = np.linalg.norm(delta_position)
        unity_direction = delta_position / expected_distance
        delta_distance = expected_distance - measured_distance
        update_standard_deviation = math.sqrt(math.pow(distance_standard_deviation, 2) +
                                              math.pow(neighbor_standard_deviation, 2))
        confidence = self.standard_deviation / (self.standard_deviation + update_standard_deviation)
        kick = confidence * delta_distance * unity_direction

        self.position = self.position + kick
        self.standard_deviation = confidence * update_standard_deviation + (1 - confidence) * self.standard_deviation
