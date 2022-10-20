figg1=(((3,4),1),((2,2),10))
figg2=(((4,6),1),((4,4),1))
table1=8,10
resfigg=()
for tup in [figg1,figg2]:
    resfigg+=tup
print(resfigg)
print(table1)



#Первоначальная проверка
def GeneralCheck(table,figures):
    #Задаем стартовые переменные.
    #buff - максимальное значение стороны "стола",
    #buffresp - переменная, которая подсчитывает количество занимаемого места in total фигурами,
    #buffp - считает количество занимаемого места отдельной фигурой
    buff=max(table)
    buffresp=0
    buffp=0
    #За каждый отдельный тип фигуры...
    for tup in figures:
        buffresp+=buffp
        buffp=1
    #По каждому отдельно взятому критерию типа фигуры...
        for i in tup:
    #Если критерий - обозначение сторон...
            if type(i)==tuple:
                buffp+=(i[0]-1)*2+i[1]
                if(i[0]>buff or i[1]>buff):
                        return False
            else:
                buffp*=i
                if(i>buff):
                    return False
    #Последняя проверка - действительно ли количество точек, занимаемое фигурами,
    #удовлетворяет "столу"
    print(buffresp)
    return (buffresp<=(table[0]*table[1]))

#print(GeneralCheck(table1,resfigg))
#print(len(resfigg))
#Перечисление всевозможных фигур, которые могут сложиться без потерь
def ListGoodFigs(figures):
    bufffig=()
    for tup in figures:
        if (tup[0][0]-2==0.5*(tup[0][1]-2)):
            bufffig+=(tup,)
    return bufffig
#print(ListGoodFigs(resfigg))

def ConcatGoodFigs(gfigures):
    bufftup=()
    for tup in gfigures:
        bufftup+=(tup[0],)
    totalreq=()
    for i in range(len(gfigures)):
        if ((i+2,i*2+2)) in bufftup:
            for fig in gfigures:
                if ((i+2,i*2+2)) in fig:
                    #print(fig)
                    totalreq=fig
        else:
            i=len(gfigures)
            if(totalreq != None):
                return totalreq,(totalreq[0][0]*totalreq[0][1])
            else:
                return False,False
    return totalreq,(totalreq[0][0]*totalreq[0][1])    
#test1,test2 = ConcatGoodFigs(ListGoodFigs(resfigg))    
#print(test1)
#print(test2)
def lossfunc(bfigures,ssbf):
    for fig in bfigures:
        if fig[0][1] % 2 !=0 and fig[1]%2!=0:
            ssbf+=(fig[0][0]-2)*(fig[0][1]-2)
        elif fig[0][1] % 2 !=0:
            ssbf+=(fig[0][0]-2)*(fig[0][1]-3)+2
        else:
            ssbf+=2
    return ssbf
    

def mainfunc(table,figures):
    tableS=table[0]*table[1]
    if not GeneralCheck(table,figures):
        return False
    goodfigs=ListGoodFigs(figures)
    badfigs=()
    totalbuffsgf=0
    for fig in figures:
        if(fig not in goodfigs):
            badfigs+=(fig,)
    print(badfigs)
    for fig in goodfigs:
        if ((2,2)) in fig:
            buffi = fig[1]
            #print(buffi)
    for i in range(buffi):
        buffgf,buffsgf = ConcatGoodFigs(goodfigs)
        for j in range(buffgf[0][0]-1):
            buffqq=()
            for fig in goodfigs:
                if j+2==fig[0][0]:
                    if fig[1]!=1:
                        buffqq+=(((fig[0][0],fig[0][1]),fig[1]-1),)                        
                else:
                    buffqq+=(fig,)
            #print(buffqq)
            goodfigs=buffqq
        totalbuffsgf+=buffsgf
        print(totalbuffsgf)
    tableS-=totalbuffsgf
    sbf=0
    for fig in badfigs:
        sbf+=((fig[0][0]-1)*2 + fig[0][1])*fig[1]
    sbf=lossfunc(badfigs,sbf)
    if tableS<sbf:
        return False
    else:
        return True
print(mainfunc(table1,resfigg))
