from addition import add
from difference import subtract
from product import multiply

def main():
    a, b = 10, 5
    print("a =", a, ", b =", b)
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))

if __name__ == "__main__":
    main()
