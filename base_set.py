class BaseSet:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = set(elements)
    
    def __str__(self):
        return f'{self.elements}'
    
    def add(self, element):
        self.elements.add(element)
    
    def remove(self, element):
        self.elements.discard(element)  # discard does not raise an error if the element is not found
    
    def union(self, other_set):
        return BaseSet(self.elements.union(other_set.elements))
    
    def intersection(self, other_set):
        return BaseSet(self.elements.intersection(other_set.elements))
    
    def difference(self, other_set):
        return BaseSet(self.elements.difference(other_set.elements))
    
    def complement(self, universal_set):
        return BaseSet(universal_set.elements.difference(self.elements))
    
    def is_subset(self, other_set):
        return self.elements.issubset(other_set.elements)
    
    def is_proper_subset(self, other_set):
        return self.is_subset(other_set) and self.elements != other_set.elements
    
    def power_set(self):
        from itertools import chain, combinations
        s = list(self.elements)
        power_set_list = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
        return BaseSet([frozenset(i) for i in power_set_list])
