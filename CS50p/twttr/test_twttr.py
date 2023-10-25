# Code created by Pepijn Weitzel
from twttr import shorten


def test_shorten():
    assert shorten("Kaas") == "Ks"
    assert shorten("") == ""
    assert shorten("bdaeioudb") == "bddb"
    assert shorten("bdaEOSDFdda") == "bdSDFdd"
    assert shorten("bda213rSD") == "bd213rSD"
    assert shorten("adsg.,23!>?") == "dsg.,23!>?"

