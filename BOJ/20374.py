import sys
from decimal import Decimal

if __name__ == "__main__":
    res = 0

    for line in sys.stdin.readlines():
        res += Decimal(line.strip())

    print(f"{res:.2f}")
