from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices: dict[str: int] = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    # Some items are multi-priced: buy n of them, and they'll cost you y pounds.
    # E.g. buy 3 of item A and get them fora combined total of 130:
    multi_item_prices: dict[str: tuple[int, int]] = {
        "A": (3, 130),
        "B": (2, 45)
    }

    # For any illegal input, return -1:
    if not all(item in item_prices for item in skus):
        return -1

    item_counts: Counter[str] = Counter(skus)

    total: int = 0
    for item, count in item_counts.items():
        # Apply multi item offers first:
        if item in multi_item_prices.keys():
            required_quantity, offer_price = multi_item_prices.get(item)
            offers_redeemed = count // required_quantity
            count = count % required_quantity
            total += offers_redeemed * offer_price
        item_price: int = item_prices.get(item)
        total += count * item_price
    return total

