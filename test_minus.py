import pytest

@pytest.mark.parametrize("a, b, expected", [
(4,2,2),
(7,3,4),
(8,5,3),
(10,2,9),
])


def test_minus(a,b, expected):
    from minus import subtract
    result = subtract(a,b)
    assert result == pytest.approx(expected)
