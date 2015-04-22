if __name__ == "__main__":

    import string
    import math
    import itertools

    def permutation_index(permut):
        """Give the index of the permutation
        """
        max_ind = len(permut)-1
        motif = {}
        for ind, i in enumerate(permut):
            motif[max_ind-ind] = len([j for j in permut[ind+1:] if j < i])
        return sum(math.factorial(k)*v for k, v in motif.iteritems())

    # Number of players
    p = 8
    players = [i for i in string.ascii_lowercase][:p]

    # Initiate it
    colors = [-1 for _ in range(math.factorial(p))]
    colors[permutation_index(itertools.permutations(players, p).next())] = 1

    while True:
        gen_permutations = itertools.permutations(players, p)
        for permutation in gen_permutations:
            tuples = [((permutation[i],) + permutation[:i] + permutation[i+1:]) for i in range(p)]
            for ktuple, mtuple in zip(tuples, tuples[1:]):
                k = permutation_index(ktuple)
                m = permutation_index(mtuple)

                if colors[k] != -1 and colors[m] != -1:
                    if colors[k] == colors[m]:
                        print "perdu"
                        print permutation, k, m
                        continue
                elif colors[k] != -1:
                    colors[m] = 1-colors[k]
                elif colors[m] != -1:
                    colors[k] = 1-colors[m]
                else:
                    pass
        if not len([i for i in colors if i == -1]):
            break

    print 'Number of permutations filled: %d out of %d' %(len(colors), math.factorial(p))

    score = 0
    # Check that for each 14 permutation, if I 
    for permutation in itertools.permutations(players, p):
        tuples = [((permutation[i],) + permutation[:i] + permutation[i+1:]) for i in range(p)]
        # Our method is based on the fact that each player will memorize a hashmap key -> value where key is the order of the friends he sees
        # Let's try to build this huge table.
        # Let s say we have 4 players, and their number. But let s just say they are ordered according to those numbers, and just memorize this order.
        # Each player will see the other 3 players. These 3 players will be ordered. So each player will just have to remember a color for each order of those 3 friends.
        # 
        # Is it possible to create a table respecting the rules, that means for any order of my 4 players, each player will compute a color depending on what he sees (the order of the other 3 players), 
        # and the color will be always alternate, whatever the order of those 4 friends are.
        # Yes, we built it. We have seen that the permutation table thus created respect a pattern that we found.

        # 4 players are 'a', 'c', 'd', 'e', and we assume their order is the same.
        # The views seen by each player will be:
        # [('a', 'c', 'd', 'e'), ('c', 'a', 'd', 'e'), ('d', 'a', 'c', 'e'), ('e', 'a', 'c', 'd'), ]
        # 
        # For each t in tuple represents a view from the first item:
        # In ('a', 'c', 'd', 'e'), 'a' will see in order 'c', 'd', 'e'
        # In ('c', 'a', 'd', 'e'), 'c' will see in order 'a', 'd', 'e'
        # ...

        # In our game, if a, c, d and e are in that order, a and c should give a different color. So permutations ('a', 'c', 'd', 'e') and ('c', 'a', 'd', 'e') will be set at different colors in our table
        #  We will have the same for ('c', 'a', 'd', 'e') and ('d', 'a', 'c', 'e'), and for ('d', 'a', 'c', 'e') and ('e', 'a', 'c', 'd')

        # But we only did that for the order 'a', 'c', 'd', 'e'.
        # What if we change it to 'a', 'c', 'e', 'd'. 

        # The views will be:
        # [('a', 'c', 'e', 'd'), ('c', 'a', 'e', 'd'), ('e', 'a', 'c', 'd'), ('d', 'a', 'c', 'e'), ]
        # In the same way, ('a', 'c', 'e', 'd') and ('c', 'a', 'e', 'd') should have different colors.
        #  Will we have conflicts? No




        for ktuple, mtuple in zip(tuples, tuples[1:]):

            k = permutation_index(ktuple)
            m = permutation_index(mtuple)
            
            if colors[k] == colors[m]:
                break
        else:
            score += 1

    print "Score: {0} out of {1}".format(score, math.factorial(p))

