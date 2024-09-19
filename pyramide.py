def pyramide(n):
    for x in range(n):
        print(" "*(n-x),"*"*(x+((x*2)-(x-1))))
        #print(x,"+",(x*2)," - ",(x-1),"=",(x+((x*2)-(x-1))))

pyramide(5)