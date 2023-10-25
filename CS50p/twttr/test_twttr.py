# Code created by Pepijn Weitzel
from twttr import shorten


def test_shorten():
    assert shorten("Kaas") == "Ks"
    assert shorten("") == ""
    assert shorten("bdaeioudb") == "bddb"
    assert shorten("bdaEOSDFdda") == "bdSDFdd"

