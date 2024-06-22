from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices: dict[str: int] = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10
    }

    # Some items are multi-priced: buy n of them, and they'll cost you y pounds.
    # E.g. buy 3 of item A and get them fora combined total of 130:
    multi_item_offers: dict[str: list[tuple[int, int]]] = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)]
    }

    # When some items are purchased in a specified quantity, other items are free.
    # E.g. buy 2 of item E and get an item B for free:
    free_item_offers: dict[str: tuple[int, str]] = {
        "E": (2, "B"),
        "F": (3, "F") # This offer is if 2 item Fs are purchased, an extra is free. Having it as 3 works with the current solution but 2 does not.
    }

    # For any illegal input, return -1:
    if not all(item in item_prices for item in skus):
        return -1

    item_counts: Counter[str] = Counter(skus)

    total: int = 0

    for item, count in item_counts.items():
        # Apply free item offers first:
        if item in free_item_offers.keys():
            required_quantity, free_item = free_item_offers.get(item)
            eligible_free_items = count // required_quantity
            if free_item in item_counts:
                item_counts[free_item] = max(item_counts.get(free_item) - eligible_free_items, 0)

    for item, count in item_counts.items():
        # Apply multi item offers next:
        if item in multi_item_offers.keys():
            for offer in multi_item_offers.get(item):
                required_quantity, offer_price = offer
                offers_redeemed = count // required_quantity
                count = count % required_quantity
                total += offers_redeemed * offer_price
        # Add any remaining items to the total after the offers:
        item_price: int = item_prices.get(item)
        total += count * item_price
    return total


