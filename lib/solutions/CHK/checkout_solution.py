# noinspection PyUnusedLocal
# skus = unicode string
import abc

price_table: dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15}
special_offers: dict[str, tuple] = {"A": (3, 30), "B": (2, 15)}


class SpecialOffer(abc.ABCMeta):

    @abc.abstractmethod
    def apply_offer(self):
        pass


class XForYOffer(SpecialOffer):

    def __init__(self, item_count: int, next_item_price: int):
        super().__init__()
        self.item_count = item_count
        self.next_item_price = next_item_price

    def apply_offer(self):
        return 0


def checkout(skus: str) -> int:
    skus = skus.replace(" ", "")
    total = 0
    sku_count = {}
    for sku in skus:
        if sku not in sku_count:
            sku_count.update({sku: 1})
        else:
            sku_count.update({sku: sku_count.get(sku) + 1})

        item_price = price_table.get(sku, None)
        if item_price is None:
            return -1

        if sku in special_offers:
            if sku_count.get(sku) % special_offers.get(sku)[0] == 0:
                item_price = special_offers.get(sku)[1]

        total += item_price
    return total


