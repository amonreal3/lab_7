"""
Adrian Monreal
lab 7
CS2302 Olac Fuentes

"""

import dsf
import matplotlib.pyplot as plt
import numpy as np
import random

import time



"""
# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joining any two cells
# Programmed by Olac Fuentes
"""

class Queue:
    def __init__(self):
        self.items = []


    def isEmpty(self):
        return self.items == []


    def enqueue(self, item):
        self.items.insert(0, item)


    def dequeue(self):
        return self.items.pop()


    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off')
    ax.set_aspect(1.0)
    plt.show()
    fig.savefig('maze.png')

              #M          #n
def wall_list(maze_rows , maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

plt.close("all")

def dsfMaze(rows,columns,wallList):
    cells = rows * columns
    s = dsf.DisjointSetForest(cells)
    while dsf.NumSets(s)> 1:
        adjIndex = 0
        curr = random.randint(0,len(wallList)-1)
        wall = wallList[curr]
        if dsf.find(s,wall[0]) != dsf.find(s,wall[1]):
            dsf.union(s, wall[0], wall[1])
            wallList.pop(curr)
    return wallList
"""
1. Modify your maze-building program to allow for both cases mentioned above. 
***Your program should display n, the number of cells, 
***and ask the user for m, the number of walls to remove, 
***then display a message indicating one of the following:
(a) A path from source to destination is not guaranteed to exist (when m < n − 1)
 (b) The is a unique path from source to destination (when m = n − 1)
(c) There is at least one path from source to destination (when m > n − 1)
"""

def Maze2(rows,columns,wallList):
    n = rows * columns #number of cells
    print("there are ", n, "cells ")
    m = input("How many walls would you like to remove")
    m = int(m)
    s = dsf.DisjointSetForest(n)
    #a
    if m<n-1:
        print("A path from source to destination is not guaranteed to exist (when m < n − 1)")
    #b
    if m == n-1:
        print("The is a unique path from source to destination (when m = n − 1)")
    #c
    if m>n-1:
        print("There is at least one path from source to destination (when m > n − 1)")
    if m > len(wallList) :
        while m > 0:

            x = random.randint(0, len(wallList) - 1)
            wallList.pop(x)
            m -= 1
        return wallList
    while m> 0:
        curr = random.randint(0,len(wallList)-1)
        wall = wallList[curr]
        if dsf.find(s,wall[0]) != dsf.find(s,wall[1]):
            dsf.union(s, wall[0], wall[1])
            wallList.pop(curr)
            m-=1
    return wallList

"--------------------------------------------------------------------------------------"


"""
2. Write a method to build the adjacency list representation of your maze.
 Cells in the maze should be represented by vertices in the graph. 
 If two cells u and v are contiguous and there is no wall separating them, 
 then there must be an edge from u to v in the graph. 
 The example below shows a maze and the corresponding graph representation.
 """
def adjListdsfMaze(rows,columns,wallList):
    cells = rows * columns
    s = dsf.DisjointSetForest(cells)
    G = [[] for i in range(len(cells))]
    while dsf.NumSets(s)> 1:
        curr = random.randint(0,len(wallList)-1)
        wall = wallList[curr]
        if dsf.find(s,wall[0]) != dsf.find(s,wall[1]):
            dsf.union(s, wall[0], wall[1])
            newEntry = wallList.pop(curr)
            G[newEntry[0]].append(newEntry[1])
    return G
"------------------------------------------------------------------------"

"""
3. Implement the following algorithms to solve the maze you created, 
assuming the starting position is bottom-left corner and the goal position is the top-right corner.
(a) Breadth-first search.
(b) Depth-first search using a stack. This is identical to breadth-first search but the queue is replaced by a stack.
(c) Depth-first search using recursion.
"""
#a
def breadthFirstsearch(G,v ):
    visited = np.zeros(len(G),dtype=bool)
    prev = np.zeros(len(G),dtype=int)-1
    q = Queue()
    q.enqueue(v)
    visited[v] = True
    while not q.isEmpty():
        u = q.dequeue()
        for t in G[u]:
            if not visited[G]:
                visited[t] = True
                prev[t] = u
                q.enqueue(t)
    return prev
#b
def depthFirstSearchS(G,v):
    s = Stack()
    s.push(v)#source
    visited = []





"______________________________________________________________________________"


maze_rows = 10

maze_cols = 15


walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True)

new = dsfMaze(maze_rows,maze_cols,walls)

""""
start = time.time()
draw_maze(new,maze_rows,maze_cols,cell_nums=False)
end = time.time()
print(end - start)
"""
print("____________________________________________")
F1 = Maze2(maze_rows,maze_cols,walls)
draw_maze(F1,maze_rows,maze_cols,cell_nums=False)
print("____________________________________________")
F2 = adjListdsfMaze(maze_rows,maze_cols,F1)
print(F2)
print("____________________________________________")
F3a = breadthFirstsearch(F2, 0)
print(F3a)
print("____________________________________________")
""""

F3b = Maze2(maze_rows,maze_cols,walls)
draw_maze(F3,maze_rows,maze_cols,cell_nums=False)

"""
print("____________________________________________")
""""
F3c = Maze2(maze_rows,maze_cols,walls)
draw_maze(F3,maze_rows,maze_cols,cell_nums=False)

"""
print("____________________________________________")