from group_theory.field_theory import Field

class GaloisField(Field):
    """Represents a Galois field (finite field), inheriting from Field."""
    
    def __init__(self, elements, addition, multiplication):
        """
        Initialize the Galois field with elements, addition, and multiplication operations.

        Args:
            elements (set): The set of elements in the Galois field.
            addition (callable): The addition operation for the Galois field.
            multiplication (callable): The multiplication operation for the Galois field.
        """
        super().__init__(elements, addition, multiplication)

    def add(self, a, b):
        """
        Perform addition in the Galois field.

        Args:
            a: The first element.
            b: The second element.

        Returns:
            The result of the addition.
        """
        return self.addition(a, b) % len(self.elements)

    def multiply(self, a, b):
        """
        Perform multiplication in the Galois field.

        Args:
            a: The first element.
            b: The second element.

        Returns:
            The result of the multiplication.
        """
        return self.multiplication(a, b) % len(self.elements)

    def is_galois_field(self):
        """
        Check if the set and operations form a Galois field.

        Returns:
            bool: True if the set and operations form a Galois field, False otherwise.
        """
        if not self.is_field():
            return False
        for a in self.elements:
            for b in self.elements:
                if self.add(a, b) not in self.elements or self.multiply(a, b) not in self.elements:
                    return False
        return True
