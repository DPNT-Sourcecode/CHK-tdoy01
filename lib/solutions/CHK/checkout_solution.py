

# noinspection PyUnusedLocal
# skus = unicode string

price_table: dict = {"A": 50, "B": 30, "C": 20, "D": 15}

def checkout(skus: str) -> int:
    skus = skus.split(" ")
    total = 0
    for sku in skus:
        item_price = price_table.get(sku, None)
        if item_price is None:
            return -1
        total += item_price
    return total


