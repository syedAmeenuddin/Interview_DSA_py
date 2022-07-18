def SumOfDigit(list):
    list.sort()
    sumofdigit = {}
    for i in list:
        tot=0
        con_str = ''
        con_str=str(i)
        for j in con_str:
            tot+=int(j)
        sumofdigit[i]=tot
    soli = {k: v for k, v in sorted(sumofdigit.items(), key=lambda item: item[1])}
    return soli

print(SumOfDigit( list = [11,12,43,51]))
print(SumOfDigit( list = [21,12,34,43]))

#input = [11,12,43,51]
#output = 11:2,12:3,43:7,51:6 ... ex: 11 = 1+1 = 2, 12 = 1+2=3....
