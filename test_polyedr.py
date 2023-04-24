from shadow.polyedr import Polyedr
from math import sqrt


def test_sum_edgess():
    Poly = Polyedr(f"data/test_1.geom")
    Poly1 = Polyedr(f"data/ccc.geom")
    assert Poly.sum_edgess() == round(Poly1.sum_edgess() + sqrt(11), 10)


def test_sum_edgess_1():
    # 12 рёбер по 10
    Poly = Polyedr(f"data/test_2.geom")
    assert Poly.sum_edgess() == 120
