if __name__ == "__main__":

    import string
    import math
    import itertools

    def permutation(permut):
        max_ind = len(permut)-1
        motif = {}
        # print permut
        for ind, i in enumerate(permut):
            motif[max_ind-ind] = len([j for j in permut[ind+1:] if j < i])

        return sum(math.factorial(k)*v for k, v in motif.iteritems())

    p = 9

    if p%2 == 0:
        magic_value = math.factorial(p-2)*2
    else:
        magic_value = math.factorial(p-1)*2


    players = [i for i in string.ascii_lowercase][:p]

    colors = [-1 for _ in range(magic_value)]

    a = itertools.permutations(players, p)
    colors[permutation(a.next())] = 1

    while True:
        gen_permutations = itertools.permutations(players, p)
        for permutation in gen_permutations:
            # print permutation
            # print order
            tuples = [((permutation[i],) + permutation[:i] + permutation[i+1:]) for i in range(p)]
            # print tuples
            # break
            # print permutation
            # print tuples
            # print 
            for ktuple, mtuple in zip(tuples, tuples[1:]):
                # print k, m
                k = permutation(ktuple)
                m = permutation(mtuple)
                # print m, k
                # print len(colors)
                # print ktuple, mtuple
                # print k, m

                if colors[k%magic_value] != -1 and colors[m%magic_value] != -1:
                    if colors[k%magic_value] == colors[m%magic_value]:
                        print "perdu"
                        print permutation, k, m
                        continue
                elif colors[k%magic_value] != -1:
                    colors[m%magic_value] = 1-colors[k%magic_value]
                elif colors[m%magic_value] != -1:
                    colors[k%magic_value] = 1-colors[m%magic_value]
                else:
                    pass

        # if len(colors) == math.factorial(p):
        if len(colors) == magic_value:
            break
        else:
            print "len(colors)"
            print len(colors)

    score = 0
    print 'Number of permutatations filled: %d out of %d' %(len(colors), math.factorial(p))

    for permutation in itertools.permutations(players, p):
        # print order
        tuples = [((permutation[i],) + permutation[:i] + permutation[i+1:]) for i in range(p)]
        # print tuples
        for ktuple, mtuple in zip(tuples, tuples[1:]):

            k = permutation(ktuple)
            m = permutation(mtuple)
            
            if colors[k%magic_value] == colors[m%magic_value]:
                continue
            else:
                score += 1


    from pprint import pprint
    # pprint(colors)
    print score/(p-1)

    # motif = {}
    # for ind, permutation in enumerate(itertools.permutations(players, p-1)):
    #     if ind<40320:
    #         motif[ind] = colors[permutation]
    #     else:
    #         if motif[ind%40320] != colors[permutation]:
    #             print ind, "perdu", colors[permutation]
    #     # # print ind, ind%4, permutation, colors[permutation]
    #     # print ind, colors[permutation]
    #     # if not((ind%4 in (1, 2) and colors[permutation]==1) or (ind%4 in (0,3) and colors[permutation]==0)):
    #         # print "perdu"
    #         pass









