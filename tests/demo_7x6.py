'''
Created on Nov 20, 2015

@author: prag717
'''

import time as tm
import simplicialHomology as sh

def closure(complx):
    n = max([len(lst) for lst in complx])
    k = n-1
    A1 = []     # A1 will contain the closure of A0 
    while k >= 0: 
        A1 += sh.ksimplices(complx,k)
        k += -1
    return A1
    
def sstar(toplexes, complx):
    i = 0
    asc = closure(toplexes)
    A = list(complx)
    i += 1
#     print A, i
    for simplex in complx:                 ## computes the star of the complex A1
        B = sh.star(asc,simplex)
        i+= 1  
#         print B, i
        for b in B:
#             print b
            if not sh.simpcluded(b,A):
#                 print "true"
                A.append(b) 
    return A 

def locHomTable(toplexes, ascdict={}):
    
    ASC = closure(toplexes)
    print "FACE" , "\t\t\t" , "H0" , "\t" , "H1" , "\t" , "H2"
    print "-"*50
    
    for splx in ASC:
    
        complx = [splx]
        A = sstar(toplexes,closure(complx))
        
        H0=sh.localHomology(0,toplexes,A,True)
        H1=sh.localHomology(1,toplexes,A,True)
        H2=sh.localHomology(2,toplexes,A,True)
         
        name = ""
        if ascdict != {}:
            for idx in range(len(complx[0])):
                name += ascdict[complx[0][idx]]
                
        if name == "":
            name = ','.join(map(str,splx))
             
        print name, "\t\t\t" , H0 , "\t" , H1 , "\t" , H2
    

toplexes = [[0,1],[0,2],[1,2,3],[2,3,4,5],[5,6]]
flagtoplexes = [[0,1,2],[1,2,3],[2,3,4,5],[5,6]]
ascdict = {0:"E", 1:"C", 2:"A", 3:"K", 4:"V", 5:"T2", 6:"T1"}
edgeList = [[0,1],[0,2],[1,2],[1,3],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5],[5,6]]

startTime = tm.time()
locHomTable(toplexes, ascdict)
print
locHomTable(flagtoplexes,ascdict)
endTime = tm.time()
print "\n**** Total time = %f s ****\n" % (endTime-startTime)