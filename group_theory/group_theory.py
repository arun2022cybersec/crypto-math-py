from sets.sets import Set
from relations.relations import Relation
from functions.functions import Function

class Group(Set):
    """Represents a mathematical group, inheriting from Set."""
    
    def __init__(self, elements, operation):
        """
        Initialize the group with elements and a binary operation.

        Args:
            elements (set): The set of elements in the group.
            operation (callable): The binary operation for the group.
        """
        super().__init__(elements)
        self.operation = operation

    def identity(self):
        """
        Find the identity element of the group.

        Returns:
            The identity element of the group.
        """
        for e in self.elements:
            if all(self.operation(e, a) == a and self.operation(a, e) == a for a in self.elements):
                return e
        return None

    def inverse(self, element):
        """
        Find the inverse of an element in the group.

        Args:
            element: The element to find the inverse of.

        Returns:
            The inverse element.
        """
        identity = self.identity()
        for e in self.elements:
            if self.operation(element, e) == identity and self.operation(e, element) == identity:
                return e
        return None

    def is_group(self):
        """
        Check if the set and operation form a group.

        Returns:
            bool: True if the set and operation form a group, False otherwise.
        """
        identity = self.identity()
        if identity is None:
            return False
        for a in self.elements:
            if self.inverse(a) is None:
                return False
        return True

class Subgroup(Group):
    """Represents a subgroup, inheriting from Group."""
    
    def __init__(self, elements, operation, parent_group):
        """
        Initialize the subgroup with elements, operation, and parent group.

        Args:
            elements (set): The set of elements in the subgroup.
            operation (callable): The binary operation for the subgroup.
            parent_group (Group): The parent group.
        """
        super().__init__(elements, operation)
        self.parent_group = parent_group

    def is_subgroup(self):
        """
        Check if the set is a subgroup of the parent group.

        Returns:
            bool: True if the set is a subgroup, False otherwise.
        """
        if not self.is_group():
            return False
        for element in self.elements:
            if element not in self.parent_group.elements:
                return False
        return True
