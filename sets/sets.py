from typing import Set as SetType

class Set:
    """Represents a mathematical set."""
    
    def __init__(self, elements):
        """Initialize the set with unique elements.

        Args:
            elements (Set): A set of unique elements.
        """
        self.elements = set(elements)

    def __eq__(self, other):
        if isinstance(other, Set):
            return self.elements == other.elements
        return False

    def add(self, element):
        """Add an element to the set."""
        self.elements.add(element)

    def remove(self, element):
        """Remove an element from the set."""
        self.elements.discard(element)

    def union(self, other: 'Set') -> 'Set':
        """Return the union of two sets.

        Args:
            other (Set): Another set to union with.

        Returns:
            Set: A new set containing the union of both sets.
        """
        return Set(self.elements | other.elements)

    def intersection(self, other: 'Set') -> 'Set':
        """Return the intersection of two sets.

        Args:
            other (Set): Another set to intersect with.

        Returns:
            Set: A new set containing the intersection of both sets.
        """
        return Set(self.elements & other.elements)

    def difference(self, other: 'Set') -> 'Set':
        """Return the difference of two sets.

        Args:
            other (Set): Another set to subtract.

        Returns:
            Set: A new set containing elements in this set but not in the other.
        """
        return Set(self.elements - other.elements)

    def symmetric_difference(self, other: 'Set') -> 'Set':
        """Return the symmetric difference of two sets.

        Args:
            other (Set): Another set to compare.

        Returns:
            Set: A new set containing elements in either set but not in both.
        """
        return Set(self.elements ^ other.elements)

    def complement(self, universe: 'Set') -> 'Set':
        """Return the complement of the set with respect to a universe.

        Args:
            universe (Set): The universal set.

        Returns:
            Set: A new set containing elements in the universe but not in this set.
        """
        return Set(universe.elements - self.elements)

    def is_subset(self, other: 'Set') -> bool:
        """Check if this set is a subset of another set.

        Args:
            other (Set): Another set to compare.

        Returns:
            bool: True if this set is a subset of the other, False otherwise.
        """
        return self.elements.issubset(other.elements)

    def is_superset(self, other: 'Set') -> bool:
        """Check if this set is a superset of another set.

        Args:
            other (Set): Another set to compare.

        Returns:
            bool: True if this set is a superset of the other, False otherwise.
        """
        return self.elements.issuperset(other.elements)

    def power_set(self) -> 'Set':
        """Return the power set of the set.

        Returns:
            Set: A new set containing all subsets of this set.
        """
        power_set = set()
        elements_list = list(self.elements)
        n = len(elements_list)

        for i in range(1 << n):  # 2^n combinations
            subset = {elements_list[j] for j in range(n) if (i & (1 << j))}
            power_set.add(frozenset(subset))  # Use frozenset to make it hashable

        return Set(power_set)

    def __repr__(self):
        return f"Set({self.elements})"