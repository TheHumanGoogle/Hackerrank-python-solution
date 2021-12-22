if __name__ == '__main__':
    x=int(input())
    y=int(input())
    z=int(input())
    n=int(input())

    final=[]
    summa=list()
    for X in range(0,x+1):
        for Y in range(0,y+1):
            for Z in range(0,z+1):
                if X+Y+Z!=n:
                    summa=[X,Y,Z]
                    final.append(summa)

print(final)
