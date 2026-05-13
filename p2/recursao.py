def multiplica(a, b):
    if a == 0 or b == 0:
        return 0
    return a + multiplica(a, b - 1)

def divide(a, b):
    if a < b:
        return 0
    return 1 + divide(a - b, b)

def inverter_string(s, tam):
    if tam >= 0:
        print(s[tam], end=" ")
        inverter_string(s, tam - 1)

if __name__ == "__main__":
    print(multiplica(5, 3))
    print(divide(10, 2))
    inverter_string("Hello", len("Hello") - 1)