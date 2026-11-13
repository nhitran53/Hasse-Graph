import toponetx as tnx
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

cc=tnx.CombinatorialComplex()
for v in [1,2,3,4]:
    cc.add_node(v)

edges = [(1,2),(1,3),(2,3),(2,4),(3,4)]
for edge in edges:
    cc.add_cell(edge,rank=1)

cc.add_cell((1,2,3),rank=2)
cc.add_cell((2,3,4),rank=2)

print("shape of the combinatorial complex:",cc.shape)

B01=cc.incidence_matrix(0,to_rank=1)
B12=cc.incidence_matrix(1,to_rank=2)
B02=cc.incidence_matrix(0,to_rank=2)

print("Incidence matrix B01:\n",B01.toarray())
print("Incidence matrix B12:\n",B12.toarray())
print("Incidence matrix B02:\n",B02.toarray())

A01=cc.adjacency_matrix(0,via_rank=1)
A12=cc.adjacency_matrix(1,via_rank=2)

print("Adjacency matrix A01:\n",A01.toarray())
print("Adjacency matrix A12:\n",A12.toarray())

coA01=cc.coadjacency_matrix(1,via_rank=0)
coA12=cc.coadjacency_matrix(2,via_rank=1)
print("Coadjacency matrix coA01:\n",coA01.toarray())
print("Coadjacency matrix coA12:\n",coA12.toarray())



# Create Hasse graph
H = nx.DiGraph()
vertices = [(1,), (2,), (3,), (4,)]
edges = [(1,2), (1,3), (2,3), (2,4), (3,4)]
faces = [(1,2,3), (2,3,4)]

cells = vertices + edges + faces

H.add_nodes_from(cells)

# Connect v to e 
for v in vertices:
    for e in edges:
        if set(v).issubset(set(e)):
            H.add_edge(v, e)

# Connect e to f 
for e in edges:
    for f in faces:
        if set(e).issubset(set(f)):
            H.add_edge(e, f)

print("Hasse graph nodes:", H.number_of_nodes())
print("Hasse graph edges:", H.number_of_edges())


# Position cells based on their ranks
pos = {}

for i, v in enumerate(vertices):
    pos[v] = (i, 0)
#Places rank-0 vertices at the bottom (y=0).
for i, e in enumerate(edges):
    pos[e] = (i - 0.5, 1)
#Places rank-1 edges in the middle (y=1).
for i, f in enumerate(faces):
    pos[f] = (i + 0.5, 2)
#Places rank-2 faces at the top (y=2).
plt.figure(figsize=(10, 6))

nx.draw(H,pos,with_labels=True,node_color="lightblue",node_size=1400,font_size=9,arrows=True)
#replace 
plt.title("Hasse Graph of Combinatorial Complex")
plt.show()
