from twttr import shorten
import pytest


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("bye") == "by"
    assert shorten("hola") == "hl"
    assert shorten("IOU") == ""
    assert shorten("123") == "123"
    assert shorten("@#$@#!") == "@#$@#!"
