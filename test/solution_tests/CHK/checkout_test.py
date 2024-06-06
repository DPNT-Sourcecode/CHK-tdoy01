from solutions.CHK.checkout_solution import checkout


class TestCheckout:
    def test_multiple_items_total(self):
        assert checkout("A B C") == 100
        assert checkout("A C") == 70
        assert checkout("A B C D") == 115

    def test_return_negative_one_when_unable_to_find_item(self):
        assert checkout("E") == -1

