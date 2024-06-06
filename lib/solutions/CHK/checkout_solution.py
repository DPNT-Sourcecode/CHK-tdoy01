

# noinspection PyUnusedLocal
# skus = unicode string

price_table: dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15}
special_offers: dict[str, tuple] = {"A": (3, 130), "B": (2, 45)}

def checkout(skus: str) -> int:
    skus = skus.split(" ")
    total = 0
    for sku in skus:
        item_price = price_table.get(sku, None)
        if item_price is None:
            return -1
        total += item_price
    return total
