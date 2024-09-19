def pyramide(n):
    for x in range(n):
        print(" "*(n-x),"*"*(x+((x*2)-(x-1))))
        #print(x,"+",(x*2)," - ",(x-1),"=",(x+((x*2)-(x-1))))

pyramide(10)    #pyramide de 10 lignes

print("\n Belle pyramide!")
