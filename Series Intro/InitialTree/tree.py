import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx
import brewer2mpl

# requires the library networkx

fig = plt.figure(figsize = (24,20))
ax = fig.add_subplot(111)

G=nx.Graph()
# explicitly set positions
pos = {40: (-10.08,1),0: (-10.08,-4),32: (-28.8,-2.5),1: (-23.4,-2.5),25: (-18,-2.5),34: (-12.6,-2.5),11: (-7.2,-2.5),27: (-1.8,-2.5),18: (3.6,-2.5),20: (9,-2.5),26: (-28.8,-1),7: (-23.4,-1),6: (-18,-1),8: (-12.6,-1),9: (-7.2,-1),10: (-1.8,-1),5: (3.6,-1),19: (9,-1),12: (-19.44,3),13: (2.16,3),14: (-25.92,5),15: (-12.96,5),2: (10.08,5),3: (2.16,5),16: (-33.12,7),17: (-25.92,7),21: (-17.28,7),22: (-10.08,7),29: (-29.52,9),30: (-25.92,9),31: (-21.6,9),23: (-12.96,9),24: (-7.2,9),4: (-3.6,5),28: (12.96,6.5),33: (-33.12,8.5),41: (-33.12,10),35: (-33.12,11.5),36: (-33.12,13),38: (-33.12,14.5),39: (-33.12,16),37: (-33.12,17.5),42: (-29.52,10.5),43: (-29.52,12),44: (-29.52,13.5),45: (-29.52,15),46: (-25.92,10.5),47: (-25.92,12),48: (-25.92,13.5),49: (-25.92,15),50: (-25.92,16.5),51: (-25.92,18),52: (-21.6,10.5),53: (-21.6,12),54: (-21.6,13.5),55: (-21.6,15),56: (-21.6,16.5),57: (-21.6,18),58: (-17.28,8.5),59: (-17.28,10),60: (-17.28,11.5),61: (-17.28,13),62: (-17.28,14.5),63: (-17.28,16),64: (-17.28,17.5),65: (-12.96,10.5),66: (-12.96,12),67: (-12.96,13.5),68: (-12.96,15),69: (-12.96,16.5),70: (-12.96,18),71: (-12.96,19.5),72: (-12.96,21),73: (-12.96,22.5),74: (-7.2,10.5),75: (-7.2,12),76: (-7.2,13.5),77: (-7.2,15),78: (-7.2,16.5),79: (-7.2,18),80: (-7.2,19.5),81: (-7.2,21),82: (-7.2,22.5),83: (-7.2,24),84: (-7.2,25.5),85: (2.16,6.5),86: (2.16,8),87: (2.16,9.5),88: (2.16,11),89: (2.16,12.5),90: (7.2,6.5),91: (7.2,8),92: (12.96,8),93: (12.96,9.5)}

# high level nodes lists
nodes_bs_big = [26, 7, 6, 8, 9, 10, 5, 19]
nodes_gc_big = [32,1,25,34,11,27,18,20]

# low level nodes lists
nodes_bd = [37]
nodes_bs = [39,44,45,49,50,51,56,57,62,63,64,72,73,82,83,84]
nodes_gc = [4,33,35,36,38,41,42,43,46,47,48,52,53,54,55,58,59,60,61,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,85,86,87,88,89,90,91,92,93]

# group nodes
nodes_main = [12,13,14,15,2,3,16,17,21,22,28,29,30,31,23,24]

# edges
list_list = [(16,33),(33,41),(41,35),(35,36),(36,38),(38,39),(39,37),(29,42),(42,43),(43,44),(44,45),(30,46),(46,47),(47,48),(48,49),(49,50),(50,51),(31,52),(52,53),(53,54),(54,55),(55,56),(56,57),(21,58),(58,59),(59,60),(60,61),(61,62),(62,63),(63,64),(23,65),(65,66),(66,67),(67,68),(68,69),(69,70),(70,71),(71,72),(72,73),(24,74),(74,75),(75,76),(76,77),(77,78),(78,79),(79,80),(80,81),(81,82),(82,83),(83,84),(3,85),(85,86),(86,87),(87,88),(88,89),(2,90),(90,91),(28,92),(92,93),(32,40),(1,40),(25,40),(34,40),(11,40),(27,40),(18,40),(20,40),(26,40),(7,40),(6,40),(8,40),(9,40),(10,40),(5,40),(19,40)]
main_edges = [(40,12),(40,13),(12,14),(12,15),(13,2),(13,3),(14,16),(14,17),(15,21),(15,22),(17,29),(17,30),(17,31),(22,23),(22,24),(13,4),(2,28)]

labels={}
# root
labels[0]='Higher Level Concepts'
labels[40]='Lower Level Concepts'
# level 1. 3-bet Pots
labels[12]='vs. Regulars'
labels[13]='vs. Rec Players'

# level 0.1. Core Concepts -- make this level 1
labels[32]='3-betting\n is good' #GC
labels[1]='3-bet pots\n are important' #GC
labels[25]='Fold\n Equity' #GC
labels[34]='Stack:Pot\n Ratio' #GC
labels[26]='Thinking\n EV' #BS
labels[11]='The Right\n Size Pot' #GC
labels[27]='Exploitive\n Play' #GC
labels[18]='Flop\n Texture' #GC
labels[20]='Stack\n Depth' #GC
labels[7]='Comparing\n Range vs. Range' #BS
labels[6]='Relative\n Hand Strength' #BS
labels[8]='Concept:\n Breakdown\n of Equity' #BS
labels[9]='Finesse\n in 3-bet Pots' #BS
labels[10]='Squeezing\n Theory' #BS
labels[5]='Thinking\n Runouts' #BS
labels[19]='Playing\n Deep' #BS


# level 0.12. Regulars
labels[14]='vs. 3-bet'
labels[15]='as 3-bettor'

# level 0.12.14 vs. Regular vs. 3-bet
labels[16] = '4-betting'
labels[17] = 'Calling'

#level 0.12.14.16 4-betting vs. Regular
labels[33]='Pot\n Commitment' # GC
labels[41]='Using\n Stats' # GC
labels[35]='4-bet\n Sizing' # GC
labels[36]='Getting\n All-in' # GC
labels[37]='4-betting\n Theory' # BD
labels[38]='AK Math' # GC
labels[39]='4-bet Pots\n as 4-bettor' # BS

#level 0.12.14.17
labels[29]='Calling \n (General)'
labels[30]='OOP'
labels[31]='IP'

#level 0.12.14.17.29 Calling\\(General)
labels[42]='Using\n Stats' # GC
labels[43]='vs. Missed\n C-bet' # GC
labels[44]='Folding\n Theory' # BS
labels[45]='Flop Texture\n Analysis' # BS

#level 0.1.12.14.17.30 Calling vs. Reg 3-bet OOP
labels[46]='Using\n Stats' # GC
labels[47]='Preflop\n Hands' # GC
labels[48]='Check-call or \n Check-raise?' #GC
labels[49]='Planning &\n Pot Manipulation' # BS
labels[50]='Range vs. Range\n Analysis' # BS
labels[51]='Leading' # BS

#level 0.12.14.17.31 Calling vs. Reg 3-bet IP
labels[52]='Using Stats' # GC
labels[53]='Preflop\n Hands' # GC
labels[54]='Facing c-bet' # GC
labels[55]='Betting vs.\n Missed C-bet' # GC
labels[56]='Planning &\n Pot Manipulation' # BS
labels[57]='Range vs. Range\n Analysis' # BS

# level 0.12.15. vs Regular as 3-bettor
labels[21]='vs. 5-bet'
labels[22]='vs. Call'

# leevl 0.12.15.21. vs Regular 4-bet
labels[58]='Using\n Stats' # GC
labels[59]='Fold\n Equity' # GC
labels[60]='Commitment\n Games' # GC
labels[61]='5-betting' # GC
labels[62]='Pot Odds &\n Flatting' # BS
labels[63]='4-bet Pots\n as Caller' # BS
labels[64]='Deep-Stacked' # BS

# leevl 0.12.15.22. Regular called 3-bet
labels[23]='IP'
labels[24]='OOP'

# level 0.12.15.22.23. Regular Called 3-bet and we're IP
labels[65]='Using\n Stats' # GC
labels[66]='Flop\n Texture' # GC
labels[67]='Bet\n Sizing' # GC
labels[68]='C-Betting' # GC
labels[69]='Turn\n Play' # GC
labels[70]='River\n Play' # GC
labels[71]='Facing a\n Check-Raise' # GC
labels[72]='Range vs.\n Range' # BS
labels[73]='EV(Check) vs.\n EV(Bet)' # BS

# level 0.12.15.22.24. Regular Called 3-bet and we're OOP
labels[74]='Using Stats' # GC
labels[75]='Flop\n Texture'# GC
labels[76]='Bet\n Sizing'# GC
labels[77]='C-Betting'# GC
labels[78]='Facing\n Raise'# GC
labels[79]='Turn Play'# GC
labels[80]='River\n Play'# GC
labels[81]='Facing a\n Check-Raise'# GC
labels[82]='Range vs.\n Range'# BS
labels[83]='Checking\n Strategy' # BS
labels[84]='Check-raising' # BS

# level 0.13. Rec Players
labels[2]='vs.\n 3-bet'
labels[3]='as\n 3-bettor'
labels[4]='Exploiting\n Leaks' # GC

# level 0.13.2 vs. 3-bet
labels[85]='Using\n Stats' # GC
labels[86]='Min 3-bets&\n Small 3-bets' # GC
labels[87]='4-betting' # GC
labels[88]='Preflop\n Selection' # GC
labels[89]='Postlop\n Strategy' # GC

# level 0.13.3 as 3-bettor
labels[90]='Using Stats' # GC
labels[91]='Facing 4-bet' # GC
labels[28]='Called'

# level 0.13.3.28 as 3-bettor -- called
labels[92]='C-betting' # GC
labels[93]='Multi-street\n Strategy' # GC

# root
nx.draw_networkx_nodes(G,pos,node_size=5000, node_color = '#ffffb3',
                       node_shape = 'o', alpha = 0.75, linewidths = 0, ax = ax,
                       nodelist = [0,40])

# groups
nx.draw_networkx_nodes(G,pos,node_size=3000, node_color = '#ffffb3',
                       node_shape = 'o', alpha = 1, linewidths = 0, ax = ax,
                       nodelist = nodes_main)

# green circle
nx.draw_networkx_nodes(G,pos,node_size=1500, node_color = '#33a02c',
                       node_shape = 'o', alpha = 0.25, linewidths = 0, ax = ax,
                       nodelist = nodes_gc)
# green circle big
nx.draw_networkx_nodes(G,pos,node_size=2500, node_color = '#33a02c',
                       node_shape = 'o', alpha = 0.25, linewidths = 0, ax = ax,
                       nodelist = nodes_gc_big)

# blue square
nx.draw_networkx_nodes(G,pos,node_size=1500, node_color = '#1f78b4',
                       node_shape = 's', alpha = 0.25, linewidths = 0, ax = ax,
                       nodelist = nodes_bs)
# blue square big
nx.draw_networkx_nodes(G,pos,node_size=2500, node_color = '#1f78b4',
                       node_shape = 's', alpha = 0.25, linewidths = 0, ax = ax,
                       nodelist = nodes_bs_big)

# black diamond
nx.draw_networkx_nodes(G,pos,node_size=1500, node_color = '#bababa',
                       node_shape = 'D', alpha = 0.5, linewidths = 0, ax = ax,
                       nodelist = nodes_bd)

# edges for top
top_edges = [(32,1),(1,25),(25,34),(34,11),(11,27),(27,18),(18,20),(26,7),(7,6),(6,8),(8,9),(9,10),(10,5),(5,19),(32,26),(1,7),(25,6),(34,8),(11,9),(27,10),(18,5),(20,19)
]
nx.draw_networkx_edges(G,pos,alpha=0.2,width=0.5, edgelist = top_edges)

# all lists
nx.draw_networkx_edges(G,pos,alpha=0.2,width=0.5, edgelist = list_list)

# main edges
nx.draw_networkx_edges(G,pos,alpha=0.5,width=2, edgelist = main_edges)


nx.draw_networkx_labels(G,pos,labels,font_size=12,font_weight = 'bold')


# nx.draw_networkx_nodes(G,pos,node_size=5000,nodelist=[0,1,2,3],node_color='#4eb3d3',
#                        node_shape = 's', linewidths = 0, ax=ax)


plt.axis('off') # turn this back on
plt.xlim([-36,15.6]) # really -14,0
plt.ylim([27,-5]) # really -15,-9
plt.savefig("X:/Users/Josh/Dropbox/poker/DC/3-bet Pots/tree.svg") # save as png
plt.show() # display
