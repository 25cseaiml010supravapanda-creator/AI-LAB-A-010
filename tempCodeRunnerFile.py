def minmax(depth,nodeindex,ismax,scoress,height):
    if depth == height:
        return scoress [nodeindex]
    
    if ismax:
        return max(
            minmax(depth +1, nodeindex *2, False, scoress,height),
            minmax(depth +1, nodeindex *2 +1, False, scoress,height),
        )
    else:
        return min(
            minmax(depth +1, nodeindex *2,True,scoress, height),
             minmax(depth +1, nodeindex *2+1,True,scoress, height),
        )
# main program
scoress  = list(map(int,input("enter 8 leaf node values:").split()))
height =3
result = minmax(0,0,True,scoress,height)
print("\n the optimal value is:",result) 