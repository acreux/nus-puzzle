import string
import math
import random
import itertools

def parity(permut):
    """Give the parity of the permutation
    """
    permut = list(permut)
    b = sorted(permut)
    inversions = 0
    while permut:
        first = permut.pop(0)
        inversions += b.index(first)
        b.remove(first)
    return inversions % 2


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

    # Set is not oredered, and thus each player are assigned a random number.
    return dict(enumerate(numbers))

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

        # Let s generate the view of our player
        tuple_p = (p, ) + tuple(sorted_tuple_players) 

        return parity(tuple_p)  

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

    return [colors[i[0]] for i in items_players]


def check_many_games(p=14, n=10000):
    """Generate many games and check the results
    """
    for i in range(n):
        players = generate_players(p)
        if not game(players):
            print "You lose"
            return
        if not i%1000:
            print i, " checked"
    print "{} games have been checked without errors.".format(n)

if __name__ == "__main__":
    check_many_games()




