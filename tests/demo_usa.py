import matplotlib.pyplot as plt
import simplicialHomology as sh
import plotComplex as pc
import networkx as nx
import time as tm

states = {
    1  : "AL",
    2  : "FL",
    3  : "GA",
    4  : "MS",
    5  : "TN",
    6  : "AR",
    7  : "LA",
    8  : "MO",
    9  : "OK",
    10 : "TX",
    11 : "AZ",
    12 : "CA",
    13 : "NM",
    14 : "NV",
    15 : "UT",
    16 : "OR",
    17 : "CO",
    18 : "KS",
    19 : "NE",
    20 : "WY",
    21 : "CT",
    22 : "MA",
    23 : "NY",
    24 : "RI",
    25 : "DC",
    26 : "MD",
    27 : "VA",
    28 : "DE",
    29 : "NJ",
    30 : "PA",
    31 : "NC",
    32 : "SC",
    33 : "IA",
    34 : "IL",
    35 : "MN",
    36 : "SD",
    37 : "WI",
    38 : "ID",
    39 : "MT",
    40 : "WA",
    41 : "IN",
    42 : "KY",
    43 : "MI",
    44 : "OH",
    45 : "WV",
    46 : "NH",
    47 : "VT",
    48 : "ME",
    49 : "ND"
}

# [x_coord, y_coord]
coords = {
    "AL" : [1600,1235],
    "FL" : [1840,1345],
    "GA" : [1840,1130],
    "MS" : [1390,1130],
    "TN" : [1610,1010],
    "AR" : [1160,1010],
    "LA" : [1160,1235],
    "MO" : [1160,785],
    "OK" : [935,1130],
    "TX" : [935,1345],
    "AZ" : [490,1130],
    "CA" : [40,900],
    "NM" : [710,1235],
    "NV" : [265,785],
    "UT" : [490,785],
    "OR" : [40,675],
    "CO" : [710,900],
    "KS" : [935,900],
    "NE" : [935,675],
    "WY" : [710,560],
    "CT" : [2630,485],
    "MA" : [2740,340],
    "NY" : [2515,340],
    "RI" : [2850,485],
    "DC" : [2290,900],
    "MD" : [2290,675],
    "VA" : [2060,785],
    "DE" : [2515,785],
    "NJ" : [2515,560],
    "PA" : [2290,450],
    "NC" : [2060,1010],
    "SC" : [2060,1235],
    "IA" : [1160,560],
    "IL" : [1390,450],
    "MN" : [1160,340],
    "SD" : [935,450],
    "WI" : [1390,225],
    "ID" : [490,450],
    "MT" : [710,340],
    "WA" : [40,450],
    "IN" : [1840,450],
    "KY" : [1840,675],
    "MI" : [1840,225],
    "OH" : [2060,340],
    "WV" : [2060,560],
    "NH" : [2850,185],
    "VT" : [2630,185],
    "ME" : [3010,40],
    "ND" : [935,225]
}

graph_file = "usa.txt"

# ALL OF THESE ARE FOR N0 NEIGHBORHOODS
g = nx.read_edgelist(graph_file, nodetype=int)
gflag = None
gedgelist = map(list,g.edges(data=False))

startTime = tm.time()

print "finding flag complex"
cplx = sh.flag(gedgelist,3)
print "getting simplices"
cplx_grph=sh.ksimplices(cplx,0)+sh.ksimplices(cplx,1)+sh.ksimplices(cplx,2)+sh.ksimplices(cplx,3)
print "creating colors1"
colors_grph_1=[sh.localHomology(1,cplx,[spx],True) for spx in cplx_grph]
print "creating colors2"
colors_grph_2=[sh.localHomology(2,cplx,[spx],True) for spx in cplx_grph]
print "creating colors3"
colors_grph_3=[sh.localHomology(3,cplx,[spx],True) for spx in cplx_grph]

endTime = tm.time()
print "\n**** Total time = %f s ****\n" % (endTime-startTime)

print "creating locations array"
locations = [[coords[states[i]][0], -coords[states[i]][1]] for i in range(1,50)]
locations = [[0,0]] + locations

plt.figure(figsize=(24,16), tight_layout=True)
#plt.figure()
plt.hold(True)
plt.subplot(311)
plt.title("H1")
print "plotting complex 1"
pc.plot_complex(locations,cplx_grph,colors_grph_1)
x_offset = 25
y_offset = 35
for k, v in coords.iteritems():
    plt.text(v[0]-x_offset, -v[1]+y_offset, k, weight='bold', size=18)
plt.axis('off')
plt.tight_layout()
plt.subplot(312)
plt.title("H2")
print "plotting complex 2"
pc.plot_complex(locations,cplx_grph,colors_grph_2)
for k, v in coords.iteritems():
    plt.text(v[0]-x_offset, -v[1]+y_offset, k, weight='bold', size=18)
plt.axis('off')
plt.tight_layout()
plt.subplot(313)
plt.title("H3")
print "plotting complex 3"
pc.plot_complex(locations,cplx_grph,colors_grph_3)
for k, v in coords.iteritems():
    plt.text(v[0]-x_offset, -v[1]+y_offset, k, weight='bold', size=18)
plt.axis('off')
plt.tight_layout()
plt.savefig('usa_graph.png')
