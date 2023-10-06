import pytest
from src.suma import suma

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (1, 1, 2),
      (0, 0, 0),
      (100, -100, 0),
      (-15, -1, -16),
      (-3, 8, 5),
      (9, suma(-1, -2), 6)
    ]
  )
def test_suma_params(input_n1, input_n2, expected):
    assert suma(input_n1, input_n2) == expected