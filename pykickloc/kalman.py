import copy

import pandas as pd


class KickLocKalman:
    def __init__(self, position: pd.DataFrame = pd.DataFrame([0, 0, 0]), standard_deviation: float = 1000):
        self.standard_deviation = standard_deviation
        self.position = copy.deepcopy(position)

    def update(self,
               neighbor_position: pd.DataFrame,
               neighbor_standard_deviation: float,
               measured_distance: float,
               distance_standard_deviation: float):
        raise NotImplementedError()
