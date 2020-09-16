from typing import List

import numpy as np

from pykickloc.intuitive import KINode


def _run_iterations(ki: KINode, node: np.ndarray, beacons: List[np.ndarray], std_dev: float, iterations: int):
    for _ in range(iterations):
        for beacon in beacons:
            ki.update(beacon, 0, np.linalg.norm(node - beacon), std_dev)


def _run(kis: List[KINode], nodes: List[np.ndarray], measurement_std_dev: float):
    for i in range(len(kis)):
        for j in range(len(kis)):
            if i == j:
                continue
            else:
                dist = np.linalg.norm(nodes[i] - nodes[j])
                kis[i].update(kis[j].position, kis[j].standard_deviation, dist, measurement_std_dev)
                kis[j].update(kis[i].position, kis[i].standard_deviation, dist, measurement_std_dev)


def test_single_push():
    beacons = [
        np.array([5, 5, 5])
    ]
    node = np.array([-1, -1, -1])
    ki = KINode()

    _run_iterations(ki, node, beacons, .01, 1)

    assert np.linalg.norm(ki.position - node) < .1


def test_single_pull():
    beacons = [
        np.array([5, 5, 5])
    ]
    node = np.array([1, 1, 1])
    ki = KINode()

    _run_iterations(ki, node, beacons, .01, 1)

    assert np.linalg.norm(ki.position - node) < .1


def test_basic():
    beacons = [
        np.array([0, 0, 0]),
        np.array([10, 0, 0]),
        np.array([0, 10, 0]),
        np.array([0, 0, 10])
    ]
    node = np.array([3, 3, 3])
    ki = KINode()

    _run_iterations(ki, node, beacons, .01, 10)

    assert np.linalg.norm(ki.position - node) < .1


def test_multiple_unknowns():
    beacons = [
        np.array([0, 0, 0]),
        np.array([10, 0, 0]),
        np.array([0, 10, 0]),
        np.array([0, 0, 10]),
        np.array([10, 10, 10]),
        np.array([20, 10, 10]),
        np.array([10, 20, 10]),
        np.array([10, 10, 20])
    ]
    unknowns = [
        np.array([1, 2, 3]),
        np.array([13, 14, 15]),
        np.array([4, 5, 6]),
        np.array([7, 8, 9]),
        np.array([10, 11, 12])
    ]

    nodes = list(beacons)
    nodes.extend(unknowns)

    kis = [KINode(beacon, 0) for beacon in beacons]
    kis.extend([KINode() for _ in unknowns])

    for _ in range(40):
        _run(kis, nodes, .01)

    assert np.linalg.norm(kis[0].position - nodes[0]) < .1
    assert np.linalg.norm(kis[1].position - nodes[1]) < .1
    assert np.linalg.norm(kis[2].position - nodes[2]) < .1
    assert np.linalg.norm(kis[3].position - nodes[3]) < .1
    assert np.linalg.norm(kis[4].position - nodes[4]) < .1
