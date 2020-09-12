# pykickloc

![build](https://travis-ci.com/LumineerLabs/pykickloc.svg?branch=master) ![PyPI](https://img.shields.io/pypi/v/pykickloc)

A python implementation of the KickLoc Intuitive distributed localization algorithm.

## Install

```bash
pip3 install pykickloc
```

## Usage

To create a beacon, create a KINode with the beacon's position and a standard deviation of 0:

```python
beacon = KINode(np.array([0, 1, 0]), 0)
```

To create an unknown node, create a KINode with no parameters:

```python
unknown = KINode()
```

Whenever a distance update is received, call update on the local node to update the local node's position:

```python
node.update(neighbor_position, neighbor_std_dev, distance, distance_std_dev)
```

If the nodes standard deviation was set to 0 (beacon), the update call will have no effect.

## References

* Xiong, H., & Sichitiu, M. L. (2019). [A Lightweight Localization Solution for Small, Low Resources WSNs.](https://www.mdpi.com/2224-2708/8/2/26/pdf) Journal of Sensor and Actuator Networks, 8(2), 26.

*  Xiong, H.; Sichitiu, M.L. [KickLoc: Simple, Distributed Localization for Wireless Sensor Networks.](http://ieeexplore.ieee.org/iel7/7814392/7814995/07815031.pdf) In Proceedings of the 2016 IEEE 13th International Conference on Mobile Ad Hoc and Sensor Systems (MASS), 10–13 October 2016; pp. 228–236.
