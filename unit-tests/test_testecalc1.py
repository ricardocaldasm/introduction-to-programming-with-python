from calculadora import quadrado


def main():
    test_quadrado()


def test_quadrado():
    try:
        assert quadrado(2) == 4
    except AssertionError:
        print("2 ao quadrado não é 4")
    try:
        assert quadrado(3) == 9
    except AssertionError:
        print("3 ao quadrado não é 9")
    try:
        assert quadrado(-2) == 4
    except AssertionError:
        print("-2 ao quadrado não é 4")
    try:
        assert quadrado(-3) == 9
    except AssertionError:
        print("-3 ao quadrado não é 9")
    try:
        assert quadrado(0) == 0
    except AssertionError:
        print("0 ao quadrado não é 0")


if __name__ == "__main__":
    main()
