# noinspection PyUnusedLocal
# skus = unicode string
import abc

price_table: dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15}
special_offers: dict[str, list[tuple]] = {"A": [(5, 50), (3, 20)], "B": [(2, 15)]}


# class SpecialOffer(abc.ABC):
#
#     @abc.abstractmethod
#     def apply_offer(self):
#         pass
#
#
# class XForYOffer(SpecialOffer):
#
#     def __init__(self, item_count: int, next_item_price: int):
#         self.item_count = item_count
#         self.next_item_price = next_item_price
#
#     def check_item_has_offer(self):
#         if
#
#     def apply_offer(self):
#         return self.next_item_price


def checkout(skus: str) -> int:
    skus = skus.replace(" ", "")
    total = 0
    sku_count = {}
    # count skus
    for sku in skus:
        if sku not in sku_count:
            sku_count.update({sku: 1})
        else:
            sku_count.update({sku: sku_count.get(sku) + 1})

    # apply discounts
    for sku, count in sku_count.items():
        item_price = price_table.get(sku, None)
        if item_price is None:
            return -1

        total += item_price * count

        if sku in special_offers:
            total = apply_discounts(count, sku, total)

    return total


def apply_discounts(count: int, sku: str, total: int) -> int:
    number_of_discounts_to_apply = count // special_offers.get(sku)[0][0]
    if number_of_discounts_to_apply > 0:
        discount = special_offers.get(sku)[1] * number_of_discounts_to_apply
        total -= discount
    return total


