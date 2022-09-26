def num_pals(x):
    if x < 99:
        return False
    return x // 100 == x % 10

print(num_pals(131))