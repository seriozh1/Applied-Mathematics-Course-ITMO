from math import isclose

import numpy as np

from math_util import (
    DIFFERENTIATION_STEP,
    gradient,
    norm,
    norm_gradient,
    normalize,
    partial_derivative,
)


def test_partial_derivative_hyperbola():
    fn = lambda x: x ** 3

    assert isclose(
        partial_derivative(fn, [-2.0], 0),
        12.0,
        abs_tol=DIFFERENTIATION_STEP,
    )

    assert isclose(
        partial_derivative(fn, [2.0], 0),
        12.0,
        abs_tol=DIFFERENTIATION_STEP,
    )

    assert isclose(
        partial_derivative(fn, [0.0], 0),
        0.0,
        abs_tol=DIFFERENTIATION_STEP,
    )


def test_partial_derivative_paraboloid():
    fn = lambda x, y: x ** 2 + y ** 2

    assert isclose(
        partial_derivative(fn, [1.0, 2.0], 0),
        2.0,
        abs_tol=DIFFERENTIATION_STEP,
    )

    assert isclose(
        partial_derivative(fn, [1.0, 2.0], 1),
        4.0,
        abs_tol=DIFFERENTIATION_STEP,
    )

    assert isclose(
        partial_derivative(fn, [0.0, 2.0], 0),
        0.0,
        abs_tol=DIFFERENTIATION_STEP,
    )


def test_partial_derivative_with_numpy_arrays():
    fn = lambda x, y: x ** 2 + y ** 2

    assert isclose(
        partial_derivative(fn, np.array([1.0, 2.0]), 1),
        4.0,
        abs_tol=DIFFERENTIATION_STEP,
    )


def test_gradient_paraboloid():
    fn = lambda x, y: x ** 2 + y ** 2
    actual = gradient(fn, [1.0, 2.0])
    expected = [2.0, 4.0]

    assert type(actual) == type(expected)
    assert len(actual) == len(expected)

    for actual_num, expected_num in zip(actual, expected):
        assert isclose(actual_num, expected_num, abs_tol=DIFFERENTIATION_STEP)


def test_gradient_paraboloid_with_numpy_arrays():
    fn = lambda x, y: x ** 2 + y ** 2
    actual = gradient(fn, np.array([1.0, 2.0]))
    expected = np.array([2.0, 4.0])

    assert type(actual) == type(expected)
    assert len(actual) == len(expected)

    for actual_num, expected_num in zip(actual, expected):
        assert isclose(actual_num, expected_num, abs_tol=DIFFERENTIATION_STEP)


def test_norm():
    assert isclose(norm([3.0, 4.0]), 5.0)
    assert isclose(norm(np.array([3.0, 4.0])), 5.0)


def test_normalize():
    actual = normalize([0.0, 17.0, 0.0])
    expected = [0.0, 1.0, 0.0]

    for actual_num, expected_num in zip(actual, expected):
        assert isclose(actual_num, expected_num)

    actual = normalize(np.array([0.0, 17.0, 0.0]))

    for actual_num, expected_num in zip(actual, expected):
        assert isclose(actual_num, expected_num)


def test_norm_gradient():
    fn = lambda x, y, z: x ** 2 + y ** 2 + z ** 2

    actual = norm_gradient(fn, [1.0, 1.0, 1.0])
    expected = [1.0 / 3 ** (1 / 2)] * 3

    for actual_num, expected_num in zip(actual, expected):
        assert isclose(actual_num, expected_num)

    actual = norm_gradient(fn, np.array([1.0, 1.0, 1.0]))
    expected = [1.0 / 3 ** (1 / 2)] * 3

    for actual_num, expected_num in zip(actual, expected):
        assert isclose(actual_num, expected_num)
