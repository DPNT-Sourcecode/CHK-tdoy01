from solutions.HLO.hello_solution import hello


class TestHello:
    def test_hello(self):
        assert hello() == "Hello, World!"

    def test_hello_friend_name(self):
        assert hello("John") == "Hello, John!"

