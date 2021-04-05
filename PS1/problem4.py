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

# def find_best_prof(A: list, n: int) -> set:
#     best = set()
#     # add the professor with the lowest difficulty to the set
#     best.add(min(A, key=lambda x: x[DIFFICULTY]))
#     # then add the professor with the highest humor to the set
#     best.add(max(A, key=lambda x: x[HUMOR]))

#     # then for each professor (P) in array A, 
#     # if P is not already in set "best", and
#     # there is no professor in set "best" that is both more funny and 
#     # less difficult than P
#     # then add P to set "best"
#     for p in A:
#         if p not in best:
#             # only check for p if not in set
#             should_add_to_set = True
#             for i in best:
#                 if i[DIFFICULTY] < p[DIFFICULTY] and i[HUMOR] > p[HUMOR]:
#                     # found a professor that is less difficult and more funny
#                     # do not add to set
#                     should_add_to_set = False
#                     break
#             if should_add_to_set:
#                 # there is no professor in best that is more funny and less difficult
#                 # we can add them to set
#                 best.add(p)
#     return best

def find_best_prof(A: list, n: int) -> set:
    best = set()
    # sort the array of professors by increasing difficulty
    # (alternatively, we can also sort by decreasing humor and get the same result)
    by_difficulty = sorted(A, key=lambda x: x[DIFFICULTY])

    # this variable stores the highest humor score of professors added to the set.
    # Initiate it as -1 since the range is [0, 100] so that the first (easiest)
    # professor will be included in set
    highest_humor = -1
    for p in by_difficulty:
        # since the array is sorted by increasing difficulty, the difficulty
        # of professor p will be greater than every other professor in the set.
        # therefore, p must have a higher humor score than every professor 
        # currently in the set to satisfy our selection criteria and be added to set.
        # Otherwise, p is less funny and more difficult and cannot be added.
        if p[HUMOR] > highest_humor:
            # update the highest humor score
            highest_humor = p[HUMOR]
            best.add(p)
    return best



if __name__ == "__main__":
    print(find_best_prof(A, n))
    print(find_best_2(A, n))
