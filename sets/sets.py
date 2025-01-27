from typing import Set as SetType, Any, FrozenSet

class Set:
    """Represents a mathematical set."""
    
    def __init__(self, elements: SetType[Any]):
        """Initialize the set with unique elements.

        Args:
            elements (SetType[Any]): A set of unique elements.
        """
        self.elements = set(elements)

    def __eq__(self, other: Any) -> bool:
        """Check if two sets are equal.

        Args:
            other (Any): Another set to compare.

        Returns:
            bool: True if the sets are equal, False otherwise.
        """
        if isinstance(other, Set):
            return self.elements == other.elements
        return False

    def add(self, element: Any) -> None:
        """Add an element to the set.

        Args:
            element (Any): The element to add.
        """
        self.elements.add(element)

    def remove(self, element: Any) -> None:
        """Remove an element from the set.

        Args:
            element (Any): The element to remove.
        """
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

    def __repr__(self) -> str:
        """Return a string representation of the set.

        Returns:
            str: A string representation of the set.
        """
        return f"Set({self.elements})"
