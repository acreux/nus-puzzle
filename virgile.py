
import string
import math
import itertools

def permutation_index(permut):
    """Give the index of the permutation
    """
    max_ind = len(permut)-1
    motif = {}
    # print permut
    for ind, i in enumerate(permut):
        motif[max_ind-ind] = len([j for j in permut[ind+1:] if j < i])

    return sum(math.factorial(k)*v for k, v in motif.iteritems())

def color_from_index(index):
    """From the index of the permutation, return 0 or 1
    """

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


import random
import itertools

def generate_players(p=14, minin=0, maxim=10000):
    """
    :param p: number of players
    :type p: int
    """
    # Generate p random numbers 
    # Make sure we have different numbers
    numbers = set()
    while len(numbers) < p:
        numbers.add(random.randint(minin, maxim))

    return dict(list(enumerate(numbers)))


def check_result(color_list):
    """
    Check the result of the game.
    Numbers should appear alternatively
    :param color_list: List of colors
    :type color_list: List of {0, 1}
    """
    for i, j in zip(color_list, color_list[1:]):
        if i==j:
            return False
    return True


def game(players_numbers):
    """
    :param players_numbers: Set of players with their associated numbers
    :type players_numbers: Dict of (int, int)
    :return: List of colors in the ascending order of players
    :rtype: list of {0, 1}
    """

    def color_from_other_players(p, other_players):
        """Return color based on the information available to player p
        :param p: p name
        :type p: int
        :param other_players: dict of the other players with their associated numbers
        :type other_players: dict of int
        :return: 0 or 1, the color of player p
        :rtype: int
        """
        increase_players = [(k, v) for k, v in other_players.iteritems()]
        increase_players.sort(key=lambda x: x[1])

        sorted_tuple_players = [i[0] for i in increase_players]

        tuple_p = (p, ) + tuple(sorted_tuple_players) 

        return color_from_index(permutation_index(tuple_p))        

    # Color associated to p
    colors = {}

    for p in players_numbers:
        info_player = dict(players_numbers)
        # Remove p information
        del info_player[p]

        colors[p] = color_from_other_players(p, info_player)

    # Sorting by the game master
    items_players = [(k, v) for k, v in players_numbers.iteritems()]
    items_players.sort(key=lambda x: x[1])
    # Is our result correct?

    return [colors[i[0]] for i in items_players]


def check_many_games(p=14, n=10000):
    for i in range(n):
        players = generate_players(p)
        if not game(players):
            print "You lose"
            return
        if not i%1000:
            print i, " done"
    print "Win"

check_many_games()




