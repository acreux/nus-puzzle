if __name__ == "__main__":
    import string
    import math
    p = 4
    players = [i for i in string.ascii_lowercase][:p]

    colors = {}
    import itertools

    # gen = itertools.permutations(players, 3)
    # for ind, order in enumerate(gen):
    #     if ind%2:
    #         colors[order] = 1
    #     else:
    #         colors[order] = 0

    # print sum([i for i in colors.values()])
    a = itertools.permutations(players, p-1)
    colors[a.next()] = 1
    
    new_order_gen = itertools.permutations(players, p)
    score = 0
    while True:
        gen_permutations = itertools.permutations(players, p)
        for view in gen_permutations:
            # print view
            # print order
            tuple3 = [view[:i] + view[i+1:] for i in range(p)]
            # print tuple3
            # break
            # print view
            # print tuple3
            # print 
            for k, m in zip(tuple3, tuple3[1:]):
                # print k, m
                if k in colors and m in colors:
                    if colors[k] == colors[m]:
                        print view, k, m
                        continue
                elif k in colors:
                    colors[m] = 1-colors[k]
                elif m in colors:
                    colors[k] = 1-colors[m]
                else:
                    pass
        if len(colors) == math.factorial(p):
            break
        else:
            print len(colors)

    score = 0
    print len(colors)
    for view in itertools.permutations(players, p):
        # print order
        tuple3 = [view[:i] + view[i+1:] for i in range(p)]
        # print tuple3
        for k, m in zip(tuple3, tuple3[1:]):
            if colors[k] == colors[m]:
                continue
            else:
                score += 1


    from pprint import pprint
    pprint(colors)
    print score/(p-1)

    for ind, view in enumerate(itertools.permutations(players, p-1)):
        # print ind, ind%4, view, colors[view]
        print ind, colors[view]
        if not((ind%4 in (1, 2) and colors[view]==1) or (ind%4 in (0,3) and colors[view]==0)):
            # print "perdu"
            pass








