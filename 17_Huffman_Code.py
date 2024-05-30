#Your task in this problem is to run the Huffman coding algorithm
#from lecture on this data set. What is the maximum and minimum lengths of a codeword? 

import heapq 

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l:
            return self._find(val, node.l)
        elif val > node.v and node.r:
            return self._find(val, node.r)
        elif val != node.v:
            return "NOT FOUND"

    def delete_tree(self):
        # garbage collector will do this for us.
        if self.root:
            self.root = None

    def view_tree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.l)
            print(node.v, end = " ")
            self._view_tree(node.r)

    def total(self,node):
        if self.root: 
            return self._total(node)

    def _total(self,node):
        if node: 
            return self._total(node.l) + node.v + self._total(node.r)
        else:
            return 0 
    
    def merge(self,B):
        if type(B) is Tree:
            if self.root and B.root:
                self._merge(B.root)
            elif B.root and not self.root: 
                self.root = B.root
        elif type(B) is Node: 
            if self.root and B: 
                self._merge(B)
            elif B and not self.root: 
                self.root = B 
        
    def _merge(self,node):
        new_root = Node(0)
        if self.total(self.root)<self.total(node):
            new_root.l = self.root
            new_root.r = node
        else: 
            new_root.l = node
            new_root.r = self.root
        self.root = new_root
    

    def depthfind(self,node):
        if node: 
            return self._depthfind(node)
        
    def _depthfind(self,node):
        if node == self.root: 
            return max(self.depthfind(node.l),self.depthfind(node.r)) + 1 
        if node.r or node.l: 
            return max(self.depthfind(node.l),self.depthfind(node.r)) + 1 
        else:
            return 0
    
    def minfind(self,node):
        if node: 
            return self._minfind(node)
        
    def _minfind(self,node):
        if node == self.root: 
            return min(self.minfind(node.l),self.minfind(node.r)) + 1
        if node.r or node.l: 
            return min(self.minfind(node.l),self.minfind(node.r)) + 1
        else:
            return 0
    

A = []
with open('ENTER FILE DESTINATION','r') as file: 
    for line in file: 
        A.append(int(line))
A = A[1::]

for (i,j) in enumerate(A):
    A[i] = (j,i+1,Node(j))

heapq.heapify(A)


while len(A) != 1: 
    T = Tree()
    a = heapq.heappop(A)
    b = heapq.heappop(A)
    T.merge(a[2])
    T.merge(b[2])
    heapq.heappush(A,(T.total(T.root),a[1]+b[1],T))
    

ans = A[0][2]

print(ans.depthfind(ans.root))

print(ans.minfind(ans.root))
