import statistics

GROUP = [
    {978, 167, 103, 386, 987},
    {335, 448, 298, 582, 215},
    {842, 640, 868, 943, 998},
    {384, 594, 966, 724, 231},
    {948, 163, 578, 903, 748},
    {784, 598, 740, 145, 595},
    {794, 928, 663, 702, 220},
    {556, 937, 569, 659, 520},
    {589, 502, 966, 457, 351},
]

MEDIANS = [386, 335, 868, 594, 748, 598, 702, 569, 502]

def select_all_median(groups: [{int}]) -> [int]:
    return [select_median(g) for g in groups]


def select_median(iterable) -> int:
    return statistics.median(iterable)


if __name__ == "__main__":
    print(select_all_median(GROUP))

    print(select_median(MEDIANS))

