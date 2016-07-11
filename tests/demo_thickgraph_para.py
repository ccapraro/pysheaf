# Local homology demos

import numpy as np
import time as tm
import numpy.random as random
import matplotlib.pyplot as plt
import simplicialHomology as sh
import plotComplex as pc

if __name__ == '__main__':
    # Example: A "thick" graph
    startTime = tm.time()
    random.seed(100)
    
    locations=[]
    while len(locations)<100:
        loc=random.rand(2)
        if np.sqrt((loc[0]-0.5)**2+(loc[1]-0.5)**2)<0.5:
            locations.append(loc)
    cplx=sh.vietorisRips(locations,0.1,maxdim=2)

    # Demo multiple processes
    Hks,cplx_grph=sh.localHomologyMultiproc(2,cplx,2,None,True,True)
    
    # Demo multiple threads
#     Hks,cplx_grph=sh.localHomologyMultithread(2,cplx,2)
                                              
    colors_grph_1=Hks[0]
    colors_grph_2=Hks[1]
    
    endTime = tm.time()
    print "\n**** Total time = %f s ****\n" % (endTime-startTime)
    
    plt.figure()
    plt.hold(True)
    plt.subplot(121)
    pc.plot_complex(locations,cplx_grph,colors_grph_1)
    plt.subplot(122)
    pc.plot_complex(locations,cplx_grph,colors_grph_2)
    plt.savefig('thick_graph_para.png')