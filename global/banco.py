balanco = 0

def main():
    print("Balanço:", balanco)
    deposito(100)
    saque(50)
    print("Balanço:", balanco)

def deposito(n):
    global balanco
    balanco += n

def saque(n):
    global balanco
    balanco -= n

if __name__== "__main__":
    main()