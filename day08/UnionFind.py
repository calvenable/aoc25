from collections.abc import Hashable
from typing import TypeVar
Point = tuple[int,int,int]
T = TypeVar('T', bound=Hashable)

class UnionFind[T]:
    '''Stores a disjoint set data structure representing elements that are grouped by connections.'''

    def __init__(self, elements: list[T]):
        '''Create a new disjoint set with entirely separate elements.'''
        self._parent:dict[T, T] = {p: p for p in elements}
        self._size:dict[T, int] = {p: 1 for p in elements}
        self._length = len(elements)

    def __len__(self):
        return self._length

    def find(self, e:T) -> T:
        '''Finds the representative element of the set that the element e is part of.'''
        root = self._parent[e]

        # Perform path compression if this element is not directly connected to the root.
        if self._parent[root] != root:
            self._parent[e] = self.find(root)
            return self._parent[e]
        
        return root
    
    def union(self, e1:T, e2:T):
        '''Connect elements e1 and e2 by combining their groups.'''
        e1Rep = self.find(e1)
        e2Rep = self.find(e2)
        if e1Rep == e2Rep:
            return
        
        e1Size = self._size[e1Rep]
        e2Size = self._size[e2Rep]

        # if e2 isthe bigger tree, swap e1 and e2
        if e1Size < e2Size:
            e1Rep, e2Rep = e2Rep, e1Rep

        # e1Rep is now the bigger tree; add e2 under e1
        self._parent[e2Rep] = e1Rep
        self._size[e1Rep] += self._size[e2Rep]
        self._length -= 1

    def size(self, e:T) -> int:
        '''Get the number of connected elements in the group containing e.'''
        return self._size[self.find(e)]
    
    def list(self) -> list[T]:
        '''Get one representative element from each distinct group.'''
        return [p for p in iter(self._parent) if self._parent[p] == p]