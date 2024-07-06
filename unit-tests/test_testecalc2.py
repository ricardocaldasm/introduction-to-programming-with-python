import pytest  # o pytest só funciona a arquivos com nome test_ como prefixo ou _test anexado ao nome
from calculadora import quadrado


def test_positivo():
    assert quadrado(2) == 4
    assert quadrado(3) == 9


def test_negativo():
    assert quadrado(-2) == 4
    assert quadrado(-3) == 9


def test_zero():
    assert quadrado(0) == 0
