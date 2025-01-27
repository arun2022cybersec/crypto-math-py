from group_theory.group_theory import Group

class Ring(Group):
    """Represents a mathematical ring, inheriting from Group."""
    
    def __init__(self, elements, addition, multiplication):
        """
        Initialize the ring with elements, addition, and multiplication operations.

        Args:
            elements (set): The set of elements in the ring.
            addition (callable): The addition operation for the ring.
            multiplication (callable): The multiplication operation for the ring.
        """
        super().__init__(elements, addition)
        self.multiplication = multiplication

    def is_ring(self):
        """
        Check if the set and operations form a ring.

        Returns:
            bool: True if the set and operations form a ring, False otherwise.
        """
        if not self.is_group():
            return False
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    if self.multiplication(a, self.addition(b, c)) != self.addition(self.multiplication(a, b), self.multiplication(a, c)):
                        return False
                    if self.multiplication(self.addition(a, b), c) != self.addition(self.multiplication(a, c), self.multiplication(b, c)):
                        return False
        return True
