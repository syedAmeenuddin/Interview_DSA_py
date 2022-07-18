def TotalSumOfString(string):
    alp = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    total = 0
    collect_str_tym={}
    if string == '':
        return '0'
    else:
        for i in string:
            if i in collect_str_tym:
                a = collect_str_tym[i]
                collect_str_tym[i]=a+alp[i]
                total+= alp[i]
            else:
                collect_str_tym[i]=0+alp[i]
                total+= alp[i]
        return total
        
print(TotalSumOfString('babca'))
