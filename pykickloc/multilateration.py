import math
from typing import Dict, List

import numpy as np

import pandas as pd


def multilaterate(nodes: Dict[str, int],
                  deltas: pd.DataFrame,
                  beacons: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    return ki_multilaterate(nodes, deltas, beacons)


def ki_multilaterate(nodes: Dict[str, int],
                     deltas: pd.DataFrame,
                     beacons: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    pass

def kk_multlaterate():
    pass