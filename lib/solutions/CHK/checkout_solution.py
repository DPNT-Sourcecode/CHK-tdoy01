# noinspection PyUnusedLocal
# skus = unicode string
import abc
import functools

price_table: dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
x_for_y_offers: dict[str, list[tuple]] = {"A": [(5, 50), (3, 20)], "B": [(2, 15)]}
buy_x_get_y_free_offers: dict[str, tuple] = {"E": (2, "B")}


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
    skus = sorted(skus.replace(" ", ""))
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

        if sku in x_for_y_offers:
            remaining_count = count
            for special_offer in x_for_y_offers.get(sku):
                number_of_discounts_to_apply = remaining_count // special_offer[0]
                remaining_count = count % special_offer[0]
                if number_of_discounts_to_apply > 0:
                    discount = special_offer[1] * number_of_discounts_to_apply
                    total -= discount

        if sku in buy_x_get_y_free_offers:
            #           7 E means up to 3 B free
            number_of_free_items = count // buy_x_get_y_free_offers.get(sku)[0]
            free_item_sku = buy_x_get_y_free_offers.get(sku)[1]
            number_of_free_items = sku_count.get(free_item_sku, 0) if sku_count.get(free_item_sku, 0) < number_of_free_items else number_of_free_items
            discount = number_of_free_items * price_table.get(free_item_sku)


    return total


