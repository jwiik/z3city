import z3


def avg(lst: list[float | int]) -> float:
    return sum(lst) / len(lst)


def _extract_schedule(model: z3.ModelRef, hours: list[z3.Int]) -> list[bool]:
    return [bool(model[h].as_long()) for h in enumerate(hours)]


def _compute_avg_price(result: list[bool], prices: list[float]) -> float:
    selected_prices = [p for h, p in zip(result, prices) if h]
    return avg(selected_prices)


def solve(
    prices: list[float],
    min_hours: int,
    max_gap: int,
    fixed_base_price: int = 7.5
) -> list[bool]:
    if len(prices) != 24:
        raise ValueError("prices must have 24 elements")
    print("Unoptimized avg", avg(prices))
    schedule = [True] * 24

    solver = z3.Optimize()
    # Each hour is denoted by a variable, each have value 0 or 1
    hours = [z3.Int(f"h{i}") for i in range(24)]
    for h in hours:
        solver.add(z3.Or(h == 0, h == 1))

    # Ensure that the number of heating hours are at least min_hours
    solver.add(z3.Sum(hours) >= min_hours)

    # Ensure that there are no off-periods longer than max-gap
    for i in range(24 - max_gap + 1):
        end = i + max_gap - 1
        solver.add(z3.Or([h == 1 for h in hours[i : end + 1]]))

    # Ensure that all on-periods are at least 2 hours long
    for i in range(1, 24 - 1):
        solver.add(
            z3.Implies(hours[i] == 1, z3.Or(hours[i - 1] == 1, hours[i + 1] == 1))
        )

    solver.push()
    # For each hour, add a soft assert where the weight is the price
    for h, p in zip(hours, prices):
        weight = fixed_base_price + p
        solver.add_soft(h == 0, str(weight))

    if solver.check() == z3.sat:
        schedule = _extract_schedule(solver.model(), hours)
        avg_price = _compute_avg_price(schedule, prices)
        solver.pop()

        for (_, r), h in zip(schedule, hours):
            if r:
                solver.add(h == 1)

        solver.push()
        for h, p in zip(hours, prices):
            weight = p - avg_price
            solver.add_soft(h == 0, str(weight))
        if solver.check() == z3.sat:
            schedule = _extract_schedule(solver.model(), hours)

    return schedule

