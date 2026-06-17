"""Traditional SPC constants for subgroup control charts."""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class SPCConstants:
    """Traditional SPC constants for a subgroup size.

    Args:
        n (int): Subgroup size.
        a2 (Optional[float]): Xbar-R chart A2 constant.
        d3 (Optional[float]): R chart D3 constant.
        d4 (Optional[float]): R chart D4 constant.
        a3 (Optional[float]): Xbar-S chart A3 constant.
        b3 (Optional[float]): S chart B3 constant.
        b4 (Optional[float]): S chart B4 constant.
        c4 (Optional[float]): Bias correction constant for subgroup standard deviation.

    Returns:
        SPCConstants: Immutable constants for a supported subgroup size.

    Raises:
        TypeError: If constants cannot be represented numerically.
        ValueError: If subgroup size is invalid.

    Examples:
        ```python
        constants = get_spc_constants(5)
        ```

    Notes:
        Constants are tabulated for common subgroup sizes from 2 through 25.
    """

    n: int
    a2: Optional[float]
    d3: Optional[float]
    d4: Optional[float]
    a3: Optional[float]
    b3: Optional[float]
    b4: Optional[float]
    c4: Optional[float]


SPC_CONSTANTS: Dict[int, SPCConstants] = {
    2: SPCConstants(2, 1.880, 0.000, 3.267, 2.659, 0.000, 3.267, 0.7979),
    3: SPCConstants(3, 1.023, 0.000, 2.574, 1.954, 0.000, 2.568, 0.8862),
    4: SPCConstants(4, 0.729, 0.000, 2.282, 1.628, 0.000, 2.266, 0.9213),
    5: SPCConstants(5, 0.577, 0.000, 2.114, 1.427, 0.000, 2.089, 0.9400),
    6: SPCConstants(6, 0.483, 0.000, 2.004, 1.287, 0.030, 1.970, 0.9515),
    7: SPCConstants(7, 0.419, 0.076, 1.924, 1.182, 0.118, 1.882, 0.9594),
    8: SPCConstants(8, 0.373, 0.136, 1.864, 1.099, 0.185, 1.815, 0.9650),
    9: SPCConstants(9, 0.337, 0.184, 1.816, 1.032, 0.239, 1.761, 0.9693),
    10: SPCConstants(10, 0.308, 0.223, 1.777, 0.975, 0.284, 1.716, 0.9727),
    11: SPCConstants(11, 0.285, 0.256, 1.744, 0.927, 0.321, 1.679, 0.9754),
    12: SPCConstants(12, 0.266, 0.283, 1.717, 0.886, 0.354, 1.646, 0.9776),
    13: SPCConstants(13, 0.249, 0.307, 1.693, 0.850, 0.382, 1.618, 0.9794),
    14: SPCConstants(14, 0.235, 0.328, 1.672, 0.817, 0.406, 1.594, 0.9810),
    15: SPCConstants(15, 0.223, 0.347, 1.653, 0.789, 0.428, 1.572, 0.9823),
    16: SPCConstants(16, 0.212, 0.363, 1.637, 0.763, 0.448, 1.552, 0.9835),
    17: SPCConstants(17, 0.203, 0.378, 1.622, 0.739, 0.466, 1.534, 0.9845),
    18: SPCConstants(18, 0.194, 0.391, 1.608, 0.718, 0.482, 1.518, 0.9854),
    19: SPCConstants(19, 0.187, 0.403, 1.597, 0.698, 0.497, 1.503, 0.9862),
    20: SPCConstants(20, 0.180, 0.415, 1.585, 0.680, 0.510, 1.490, 0.9869),
    21: SPCConstants(21, 0.173, 0.425, 1.575, 0.663, 0.523, 1.477, 0.9876),
    22: SPCConstants(22, 0.167, 0.434, 1.566, 0.647, 0.534, 1.466, 0.9882),
    23: SPCConstants(23, 0.162, 0.443, 1.557, 0.633, 0.545, 1.455, 0.9887),
    24: SPCConstants(24, 0.157, 0.451, 1.548, 0.619, 0.555, 1.445, 0.9892),
    25: SPCConstants(25, 0.153, 0.459, 1.541, 0.606, 0.565, 1.435, 0.9896),
}


def get_spc_constants(subgroup_size: int) -> SPCConstants:
    """Return traditional SPC constants for a subgroup size.

    Args:
        subgroup_size (int): Subgroup size to look up.

    Returns:
        SPCConstants: Constants for the requested subgroup size.

    Raises:
        TypeError: If subgroup size is not an integer.
        ValueError: If subgroup size is unsupported.

    Examples:
        ```python
        constants = get_spc_constants(5)
        ```

    Notes:
        Supported subgroup sizes are 2 through 25.
    """
    if not isinstance(subgroup_size, int):
        raise TypeError("subgroup_size must be an integer.")
    if subgroup_size not in SPC_CONSTANTS:
        raise ValueError("Traditional SPC constants are available for subgroup sizes 2 through 25.")
    return SPC_CONSTANTS[subgroup_size]
