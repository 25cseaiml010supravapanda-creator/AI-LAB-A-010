import math
#alpha-beta purning function
def alpha_beta (depth, nodeindex,maximizingPlayer,values,alpha,beta,height):
    #base case: leaf node reached
    if depth == height:
        return values[nodeindex]
    if maximizingPlayer:
        best = -math.inf
    for i in range(2):
        values = alpha_beta(
            depth +1,
            nodeindex *2 +i,
            False,
            values,
            alpha,
            beta,
            height
        )      
        best = max(best, values)
        alpha = max(alpha,best)
        #BETA cut-off
        if beta <=alpha:
            break

        return best
    else:
        best =math.inf

        for 