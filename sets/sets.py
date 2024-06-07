class Set:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = set()
        else:
            self.elements = set(elements)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.elements})'
    
    def __str__(self):
        return '{' + ', '.join(map(str, self.elements)) + '}'
    
    def add(self, element):
        self.elements.add(element)
    
    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("Element not found in the set")
    
    def union(self, other):
        if isinstance(other, Set):
            return Set(self.elements | other.elements)
        else:
            raise TypeError("Argument must be of type Set")
    
    def intersection(self, other):
        if isinstance(other, Set):
            return Set(self.elements & other.elements)
        else:
            raise TypeError("Argument must be of type Set")
    
    def difference(self, other):
        if isinstance(other, Set):
            return Set(self.elements - other.elements)
        else:
            raise TypeError("Argument must be of type Set")
    
    def is_subset(self, other):
        if isinstance(other, Set):
            return self.elements <= other.elements
        else:
            raise TypeError("Argument must be of type Set")
    
    def is_proper_subset(self, other):
        if isinstance(other, Set):
            return self.elements < other.elements
        else:
            raise TypeError("Argument must be of type Set")

    def is_equal(self, other):
        if isinstance(other, Set):
            return self.elements == other.elements
        else:
            raise TypeError("Argument must be of type Set")

    def complement(self, universal_set):
        if isinstance(universal_set, Set):
            return Set(universal_set.elements - self.elements)
        else:
            raise TypeError("Argument must be of type Set")

    def power_set(self):
        from itertools import chain, combinations
        s = list(self.elements)
        power_set_elements = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
        return Set([frozenset(e) for e in power_set_elements])

class FiniteSet(Set):
    pass

class InfiniteSet(Set):
    def __init__(self, generator):
        self.generator = generator

    def __repr__(self):
        return f'{self.__class__.__name__}(generator={self.generator})'

    def __str__(self):
        return f'{self.__class__.__name__}(generator={self.generator})'

    def generate_elements(self, n):
        return Set([next(self.generator) for _ in range(n)])

class EmptySet(Set):
    def __init__(self):
        super().__init__(set())

class UniversalSet(Set):
    def __init__(self, elements):
        super().__init__(elements)

class Symbol:
    def __init__(self, symbol, description):
        self.symbol = symbol
        self.description = description

    def __str__(self):
        return f'{self.symbol} ({self.description})'

class Symbols:
    UNION = Symbol('∪', 'Union')
    INTERSECTION = Symbol('∩', 'Intersection')
    DIFFERENCE = Symbol('-', 'Difference')
    COMPLEMENT = Symbol("'", 'Complement')
    EMPTY_SET = Symbol('∅', 'Empty Set')
    SUBSET = Symbol('⊆', 'Subset')
    PROPER_SUBSET = Symbol('⊂', 'Proper Subset')
    POWER_SET = Symbol('P', 'Power Set')
    EQUALS = Symbol('=', 'Equals')

# Example Usage
A = FiniteSet([1, 2, 3])
B = FiniteSet([2, 3, 4])

print(f"A = {A}")
print(f"B = {B}")
print(f"A {Symbols.UNION} B = {A.union(B)}")
print(f"A {Symbols.INTERSECTION} B = {A.intersection(B)}")
print(f"A {Symbols.DIFFERENCE} B = {A.difference(B)}")
print(f"A {Symbols.SUBSET} B = {A.is_subset(B)}")
print(f"A {Symbols.PROPER_SUBSET} B = {A.is_proper_subset(B)}")
print(f"A {Symbols.EQUALS} B = {A.is_equal(B)}")

U = UniversalSet(range(1, 5))
print(f"A {Symbols.COMPLEMENT} U = {A.complement(U)}")

P_A = A.power_set()
print(f"{Symbols.POWER_SET}A = {P_A}")
