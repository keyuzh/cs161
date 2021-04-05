# assume the array A is a list of tuples in the following format: (name, difficulty, humor)
A = [
    ("Venabili", 4, 65),
    ("Jones Jr", 8, 15),
    ("Jones Sr", 8.5, 2),
    ("Grant", 2, 35),
    ("Moriarty", 10, 0),
    ("Plum", 9, 85),
    ("Walsh", 8.2, 90),
]
# n is the length of array A
n = len(A)

# index in tuple
NAME = 0
DIFFICULTY = 1
HUMOR = 2

def find_best_prof(A: list, n: int) -> set:
    best = set()
    # add the professor with the lowest difficulty to the set
    best.add(min(A, key=lambda x: x[DIFFICULTY]))
    # then add the professor with the highest humor to the set
    best.add(max(A, key=lambda x: x[HUMOR]))

    # then for each professor (P) in array A, 
    # if P is not already in set "best", and
    # there is no professor in set "best" that is both more funny and 
    # less difficult than P
    # then add P to set "best"
    for p in A:
        if p not in best:
            # only check for p if not in set
            should_add_to_set = True
            for i in best:
                if i[DIFFICULTY] < p[DIFFICULTY] and i[HUMOR] > p[HUMOR]:
                    # found a professor that is less difficult and more funny
                    # do not add to set
                    should_add_to_set = False
                    break
            if should_add_to_set:
                # there is no professor in best that is more funny and less difficult
                # we can add them to set
                best.add(p)
    return best

if __name__ == "__main__":
    print(find_best_prof(A, n))
