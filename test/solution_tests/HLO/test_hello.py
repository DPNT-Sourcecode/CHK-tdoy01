from solutions.HLO.hello_solution import hello


class TestHello():
    def test_hello(self):
        assert hello("Craftsman") == "Hello, World!"
