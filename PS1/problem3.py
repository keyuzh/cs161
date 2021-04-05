
def is_resolute(n: int) -> bool:
    return (n**2 + 2 * n) % 3 == 0


if __name__ == "__main__":
    for i in range(1, 1001, 2):
        if not is_resolute(i):
            print(f"{i} is not resolute")