import sys
sys.setrecursionlimit(100000)

casos = int(raw_input())
for i in range(casos):
    entrada = raw_input()
    buscas = int(raw_input())
     
    def pd(i):
        if i == len(entrada):
            array.append('')
            return
        pd(i + 1)
        aux = array[:]
        for x in aux:
            if not dic.has_key(entrada[i] + x):
                dic[entrada[i] + x] = True
                array.append(entrada[i] + x)

    array = []
    dic = {}
     
    for i in range(buscas):
        sequencia = raw_input()
        pd(0)
        if dic.has_key(sequencia):
            print 'Yes'
        else:
            print 'No'
 
        array = []
        dic = {}