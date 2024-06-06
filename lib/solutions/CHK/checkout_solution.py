# noinspection PyUnusedLocal
# skus = unicode string

price_table: dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15}
special_offers: dict[str, tuple] = {"A": (3, 130), "B": (2, 45)}


def checkout(skus: str) -> int:
    skus = skus.split(" ")
    total = 0
    sku_count = {}
    for sku in skus:
        if sku not in sku_count:
            sku_count.update({sku: 1})
        else:
            sku_count.update({sku: sku_count.get(sku) + 1})
        sku_count.update({})

        item_price = price_table.get(sku, None)
        if item_price is None:
            return -1
        total += item_price
    return total

