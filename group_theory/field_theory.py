from group_theory.ring_theory import Ring

class Field(Ring):
    """Represents a mathematical field, inheriting from Ring."""
    
    def __init__(self, elements, addition, multiplication):
        """
        Initialize the field with elements, addition, and multiplication operations.

        Args:
            elements (set): The set of elements in the field.
            addition (callable): The addition operation for the field.
            multiplication (callable): The multiplication operation for the field.
        """
        super().__init__(elements, addition, multiplication)

    def multiplicative_inverse(self, element):
        """
        Find the multiplicative inverse of a non-zero element in the field.

        Args:
            element: The element to find the multiplicative inverse of.

        Returns:
            The multiplicative inverse element.

        Raises:
            ValueError: If the element is zero or no inverse exists.
        """
        if element == 0:
            raise ValueError("Zero does not have a multiplicative inverse.")
        
        for e in self.elements:
            if self.multiplication(element, e) == 1 and self.multiplication(e, element) == 1:
                return e
        raise ValueError("No multiplicative inverse found.")

    def is_field(self):
        """
        Check if the set and operations form a field.

        Returns:
            bool: True if the set and operations form a field, False otherwise.
        """
        if not self.is_ring():
            return False
        for a in self.elements:
            if a != 0 and self.multiplicative_inverse(a) is None:
                return False
        return True
