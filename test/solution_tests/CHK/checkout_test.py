from solutions.CHK.checkout_solution import checkout


class TestCheckout:
    def test_multiple_items_total(self):
        assert checkout("A B C") == 100
        assert checkout("A C") == 70
        assert checkout("A B C D") == 115

    def test_x_for_y_offers(self):
        assert checkout("A A A") == 130
        assert checkout("A A A A") == 180
        assert checkout("B B") == 45
        assert checkout("B A B A B") == 175
        assert checkout("B A B A B D") == 190

    def test_multiple_special_offers(self):
        assert checkout("A A A A A") == 200
        assert checkout("A A A A A A") == 250
        assert checkout("A A A A A A A") == 300
        assert checkout("A A A A A A A A") == 330


    def test_return_negative_one_when_unable_to_find_item(self):
        assert checkout("E") == -1

    def test_failed_trials(self):
        assert checkout("") == 0
        assert checkout("ABCD") == 115
        assert checkout("AA") == 100

    def test_buy_get_one_free_offers(self):
        assert checkout("EEB") == 80
        assert checkout("BEE") == 80
        assert checkout("EEBB") == 110
        assert checkout("BBEE") == 110
        assert checkout("BEBE") == 110




