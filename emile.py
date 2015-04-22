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


    p = 8
    players = [i for i in string.ascii_lowercase][:p]


    a = itertools.permutations(players, p)
    colors[permutation(a.next())] = 1
    
    new_order_gen = itertools.permutations(players, p)
    score = 0


    if p%2 == 0:
        magic_value = math.factorial(p-2)*2
    else:
        magic_value = math.factorial(p-1)*2

    # colors = [-1 for _ in range(magic_value)]
    color = {}

    while True:
        gen_permutations = itertools.permutations(players, p)
        for view in gen_permutations:
            # print view
            # print order
            tuple3 = [((view[i],) + view[:i] + view[i+1:]) for i in range(p)]
            # print tuple3
            # break
            # print view
            # print tuple3
            # print 
            for ktuple, mtuple in zip(tuple3, tuple3[1:]):
                # print k, m
                k = permutation(ktuple)
                m = permutation(mtuple)

                # print ktuple, mtuple
                # print k, m

                if k in colors and m in colors:
                    if colors[k%magic_value] == colors[m%magic_value]:
                        print "perdu"
                        print view, k, m
                        continue
                elif k in colors:
                    colors[m%magic_value] = 1-colors[k%magic_value]
                elif m in colors:
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
    print len(colors)
    for view in itertools.permutations(players, p):
        # print order
        tuple3 = [((view[i],) + view[:i] + view[i+1:]) for i in range(p)]
        # print tuple3
        for ktuple, mtuple in zip(tuple3, tuple3[1:]):

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
    # for ind, view in enumerate(itertools.permutations(players, p-1)):
    #     if ind<40320:
    #         motif[ind] = colors[view]
    #     else:
    #         if motif[ind%40320] != colors[view]:
    #             print ind, "perdu", colors[view]
    #     # # print ind, ind%4, view, colors[view]
    #     # print ind, colors[view]
    #     # if not((ind%4 in (1, 2) and colors[view]==1) or (ind%4 in (0,3) and colors[view]==0)):
    #         # print "perdu"
    #         pass









