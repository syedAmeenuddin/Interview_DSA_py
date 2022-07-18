def MaxNumberInList(numbersList):
    numbersList.sort()
    CollectIntCount = {}
    strr = ''
    for i in numbersList:
        if i in CollectIntCount:
            a = CollectIntCount[i]
            CollectIntCount[i]=a+1
        else:
            CollectIntCount[i]=1
    for k,v in CollectIntCount.items():
        a = str(k) + '(' + str(v) + ') '
        strr +=str(a)
    print(strr)
MaxNumberInList(numbersList=[2,3,4,2,2,5,5])
# return max number repeated in list
