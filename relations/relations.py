from typing import Set as SetType, Tuple, Any

class Relation:
    """Represents a mathematical relation between two sets."""
    
    def __init__(self, set_a: SetType[Any], set_b: SetType[Any], pairs: SetType[Tuple[Any, Any]]):
        """
        Initialize the relation with two sets and ordered pairs.

        Args:
            set_a (SetType[Any]): The first set.
            set_b (SetType[Any]): The second set.
            pairs (SetType[Tuple[Any, Any]]): A set of ordered pairs.
        """
        self.set_a = set(set_a)
        self.set_b = set(set_b)
        self.pairs = set(pairs)
    
    def __eq__(self, other: Any) -> bool:
        """
        Check if two Relation objects are equal.

        Args:
            other (Any): The other Relation object to compare with.

        Returns:
            bool: True if the relations are equal, False otherwise.
        """
        if isinstance(other, Relation):
            return (self.set_a == other.set_a and
                    self.set_b == other.set_b and
                    self.pairs == other.pairs)
        return False

    def is_reflexive(self) -> bool:
        """
        Check if the relation is reflexive.

        Returns:
            bool: True if the relation is reflexive, False otherwise.
        """
        return all((a, a) in self.pairs for a in self.set_a)

    def is_symmetric(self) -> bool:
        """
        Check if the relation is symmetric.

        Returns:
            bool: True if the relation is symmetric, False otherwise.
        """
        return all((b, a) in self.pairs for (a, b) in self.pairs)

    def is_transitive(self) -> bool:
        """
        Check if the relation is transitive.

        Returns:
            bool: True if the relation is transitive, False otherwise.
        """
        for (a, b) in self.pairs:
            for (c, d) in self.pairs:
                if b == c and (a, d) not in self.pairs:
                    return False
        return True

    def is_anti_symmetric(self) -> bool:
        """
        Check if the relation is anti-symmetric.

        Returns:
            bool: True if the relation is anti-symmetric, False otherwise.
        """
        for (a, b) in self.pairs:
            if (b, a) in self.pairs and a != b:
                return False
        return True

    def inverse(self) -> 'Relation':
        """
        Return the inverse of the relation.

        Returns:
            Relation: The inverse relation.
        """
        inverse_pairs = {(b, a) for (a, b) in self.pairs}
        return Relation(self.set_b, self.set_a, inverse_pairs)

    def __repr__(self) -> str:
        """
        Return a string representation of the relation.

        Returns:
            str: A string representation of the relation.
        """
        return f"Relation({self.set_a}, {self.set_b}, {self.pairs})"
