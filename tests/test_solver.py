from z3city import solver


def test_negative_prices():
    prices = [
        0.092,
        -0.051,
        -0.056,
        -0.082,
        -0.11,
        -0.245,
        -0.501,
        -1.015,
        -1.983,
        -2.001,
        -1.55,
        -1.01,
        -0.607,
        -0.154,
        -0.09,
        -0.09,
        -0.129,
        -0.175,
        -0.175,
        -0.175,
        -0.202,
        -0.199,
        -0.155,
        -0.201,
    ]
    schedule = solver.solve(prices, 10, 2)
    assert len(schedule) == 24
    assert len([b for b in schedule if b]) >= 10


def test_rising_prices():
    prices = [
        0.466,
        0.364,
        0.38,
        0.413,
        0.397,
        0.41,
        0.521,
        1.501,
        2.869,
        3.345,
        2.007,
        2.553,
        2.854,
        3.454,
        3.897,
        4.962,
        7.748,
        12.81,
        13.636,
        14.485,
        14.625,
        12.532,
        10.262,
        8.741,
    ]
    schedule = solver.solve(prices, 15, 5)
    assert len(schedule) == 24
    assert len([b for b in schedule if b]) >= 10
    for p in enumerate(zip(prices, schedule)):
        print(p)
