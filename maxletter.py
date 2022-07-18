def maxletter(string):
    CollectStringCount = {}
    MaxLetter = ''
    if string=='':
        return ''
    else:
        for i in string:
            if i in CollectStringCount:
                a = CollectStringCount[i]
                CollectStringCount[i]=a+1
                MaxLetter = i
            else:
                CollectStringCount[i]=1
        return MaxLetter
print(maxletter('ameenuddin'))
# return max letter repeated in string
