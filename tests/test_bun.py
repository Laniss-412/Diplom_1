import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("name, price",
                        [("Краторная булка N-200i", 1255),
                         ("Флюоресцентная булка R2-D3", 988)])
    def test_create_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price