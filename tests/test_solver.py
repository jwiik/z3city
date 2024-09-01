from z3city import solver


def test_solver():
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
