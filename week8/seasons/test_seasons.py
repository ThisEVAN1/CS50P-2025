from datetime import date
from seasons import convert
import pytest


def test_convert():
    assert convert(date(1999, 1, 1), date(2000, 1, 1)) == 525600
    assert convert(date(2001, 1, 1), date(2003, 1, 1)) == 1051200
    assert convert(date(1995, 1, 1), date(2000, 1, 1)) == 2629440
    assert convert(date(2020, 6, 1), date(2032, 1, 1)) == 6092640
