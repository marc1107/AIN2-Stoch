def fak(n: int):
    if n > 0:
        return n * fak(n - 1)
    else:
        return 1


def fak2(n: int):
    if n % 2 != 0:
        raise Exception("nicht durch 2 teilbar!")
    else:
        if n > 0:
            return n * fak2(n - 2)
        else:
            return 1


print("3.7.1")
# a)
print("a)", fak(20))

# b)
print("\nb)", fak2(20))
print("\nb)", fak(10) * fak(10))

print("\nc)", 10 * fak(10) * fak(10))
