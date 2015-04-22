
import string
import math
import itertools

def permutation_index(permut):
        max_ind = len(permut)-1
        motif = {}
        # print permut
        for ind, i in enumerate(permut):
            motif[max_ind-ind] = len([j for j in permut[ind+1:] if j < i])

        return sum(math.factorial(k)*v for k, v in motif.iteritems())

def color_from_index(index):

    if index == 0:
        return 1
    k = 0
    new_magic = math.factorial(k)
    while new_magic <= index:
        magic = new_magic
        k += 1
        new_magic = math.factorial(k)

    # print magic
    div = index/magic
    mod = index%magic

    if div%2 == 1:
        return 1-color_from_index(mod)
    else:
        return color_from_index(mod)



# print color_from_index(37435)
# print color_from_index(55)
# print color_from_index(40000)
# for i in range(30):
#     print i, "   ", color_from_index(i)
# print color_from_index(12)


def check(p):
    players = [i for i in string.ascii_lowercase][:p]

    score = 0

    for permutation in itertools.permutations(players, p):
        # print order
        tuples = [((permutation[i],) + permutation[:i] + permutation[i+1:]) for i in range(p)]
        # print tuples
        for ktuple, mtuple in zip(tuples, tuples[1:]):

            if color_from_index(permutation_index(ktuple)) == color_from_index(permutation_index(mtuple)):
                print permutation_index(ktuple), permutation_index(mtuple)
                print "perdu"
                continue
            else:
                score += 1
    print score/(p-1)

check(4)
check(5)
check(6)
check(7)
check(8)