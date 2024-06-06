from solutions.CHK.checkout_solution import checkout


class TestCheckout:
    def test_multiple_items_total(self):
        assert checkout("A B C") == 100
        assert checkout("A C") == 70
