import sys

sys.path.append("")

price_data = [
    {
        "price": 0.092,
        "startDate": "2024-08-25T20:00:00.000Z",
        "endDate": "2024-08-25T21:00:00.000Z",
    },
    {
        "price": -0.051,
        "startDate": "2024-08-25T19:00:00.000Z",
        "endDate": "2024-08-25T20:00:00.000Z",
    },
    {
        "price": -0.056,
        "startDate": "2024-08-25T18:00:00.000Z",
        "endDate": "2024-08-25T19:00:00.000Z",
    },
    {
        "price": -0.082,
        "startDate": "2024-08-25T17:00:00.000Z",
        "endDate": "2024-08-25T18:00:00.000Z",
    },
    {
        "price": -0.11,
        "startDate": "2024-08-25T16:00:00.000Z",
        "endDate": "2024-08-25T17:00:00.000Z",
    },
    {
        "price": -0.245,
        "startDate": "2024-08-25T15:00:00.000Z",
        "endDate": "2024-08-25T16:00:00.000Z",
    },
    {
        "price": -0.501,
        "startDate": "2024-08-25T14:00:00.000Z",
        "endDate": "2024-08-25T15:00:00.000Z",
    },
    {
        "price": -1.015,
        "startDate": "2024-08-25T13:00:00.000Z",
        "endDate": "2024-08-25T14:00:00.000Z",
    },
    {
        "price": -1.983,
        "startDate": "2024-08-25T12:00:00.000Z",
        "endDate": "2024-08-25T13:00:00.000Z",
    },
    {
        "price": -2.001,
        "startDate": "2024-08-25T11:00:00.000Z",
        "endDate": "2024-08-25T12:00:00.000Z",
    },
    {
        "price": -1.55,
        "startDate": "2024-08-25T10:00:00.000Z",
        "endDate": "2024-08-25T11:00:00.000Z",
    },
    {
        "price": -1.01,
        "startDate": "2024-08-25T09:00:00.000Z",
        "endDate": "2024-08-25T10:00:00.000Z",
    },
    {
        "price": -0.607,
        "startDate": "2024-08-25T08:00:00.000Z",
        "endDate": "2024-08-25T09:00:00.000Z",
    },
    {
        "price": -0.154,
        "startDate": "2024-08-25T07:00:00.000Z",
        "endDate": "2024-08-25T08:00:00.000Z",
    },
    {
        "price": -0.09,
        "startDate": "2024-08-25T06:00:00.000Z",
        "endDate": "2024-08-25T07:00:00.000Z",
    },
    {
        "price": -0.09,
        "startDate": "2024-08-25T05:00:00.000Z",
        "endDate": "2024-08-25T06:00:00.000Z",
    },
    {
        "price": -0.129,
        "startDate": "2024-08-25T04:00:00.000Z",
        "endDate": "2024-08-25T05:00:00.000Z",
    },
    {
        "price": -0.175,
        "startDate": "2024-08-25T03:00:00.000Z",
        "endDate": "2024-08-25T04:00:00.000Z",
    },
    {
        "price": -0.175,
        "startDate": "2024-08-25T02:00:00.000Z",
        "endDate": "2024-08-25T03:00:00.000Z",
    },
    {
        "price": -0.175,
        "startDate": "2024-08-25T01:00:00.000Z",
        "endDate": "2024-08-25T02:00:00.000Z",
    },
    {
        "price": -0.202,
        "startDate": "2024-08-25T00:00:00.000Z",
        "endDate": "2024-08-25T01:00:00.000Z",
    },
    {
        "price": -0.199,
        "startDate": "2024-08-24T23:00:00.000Z",
        "endDate": "2024-08-25T00:00:00.000Z",
    },
    {
        "price": -0.155,
        "startDate": "2024-08-24T22:00:00.000Z",
        "endDate": "2024-08-24T23:00:00.000Z",
    },
    {
        "price": -0.201,
        "startDate": "2024-08-24T21:00:00.000Z",
        "endDate": "2024-08-24T22:00:00.000Z",
    },
]

hourly_prices = [price["price"] for price in price_data]
print(hourly_prices)

# hourly_prices = [price["price"] for price in reversed(price_data)]
# hourly_prices = [10 for _ in range(24)]

# solve(hourly_prices, 8, 6)
