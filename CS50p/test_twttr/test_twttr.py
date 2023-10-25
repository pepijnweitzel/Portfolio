# Code created by Pepijn Weitzel
import twttr

def main():
    print(shorten("test"))


def test_shorten():
    assert shorten("Kaas") == "Ks"
    assert shorten("") == ""
    assert shorten("bdaeioudb") == "bddb"

main()