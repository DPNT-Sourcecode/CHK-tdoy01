from solutions.CHK.checkout_solution import checkout


class TestCheckout:
    def test_multiple_items_total(self):
        assert checkout("A B C") == 100
        assert checkout("A C") == 70
        assert checkout("A B C D") == 115

    def test_special_offers(self):
        assert checkout("A A A") == 130
        assert checkout("A A A A") == 180
        assert checkout("A A A A A") == 230
        assert checkout("A A A A A A") == 260
        assert checkout("B B") == 45

    def test_return_negative_one_when_unable_to_find_item(self):
        assert checkout("E") == -1
