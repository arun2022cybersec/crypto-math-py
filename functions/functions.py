from typing import Callable, Dict, Any, Set, Tuple


class Function:
    """Represents a mathematical function."""
    
    def __init__(self, domain: Set[Any], codomain: Set[Any], mapping: Dict[Any, Any]):
        """
        Initialize the function with a domain, codomain, and mapping.

        Args:
            domain (Set[Any]): The domain set.
            codomain (Set[Any]): The codomain set.
            mapping (Dict[Any, Any]): A dictionary representing the function mapping.
        """
        self.domain = set(domain)
        self.codomain = set(codomain)
        self.mapping = mapping

    def apply(self, input_value: Any) -> Any:
        """
        Apply the function to an input value.

        Args:
            input_value (Any): The input value.

        Returns:
            Any: The output value.

        Raises:
            ValueError: If the input is not in the domain.
        """
        if input_value not in self.domain:
            raise ValueError(f"{input_value} is not in the domain of the function.")
        return self.mapping[input_value]

    def is_injective(self) -> bool:
        """
        Check if the function is injective.

        Returns:
            bool: True if the function is injective, False otherwise.
        """
        return len(set(self.mapping.values())) == len(self.mapping)

    def is_surjective(self) -> bool:
        """
        Check if the function is surjective.

        Returns:
            bool: True if the function is surjective, False otherwise.
        """
        return self.codomain == set(self.mapping.values())

    def is_bijective(self) -> bool:
        """
        Check if the function is bijective.

        Returns:
            bool: True if the function is bijective, False otherwise.
        """
        return self.is_injective() and self.is_surjective()

    def inverse(self) -> 'Function':
        """
        Return the inverse of the function if it is bijective.

        Returns:
            Function: The inverse function.

        Raises:
            ValueError: If the function is not bijective.
        """
        if not self.is_bijective():
            raise ValueError("The function is not bijective, so it does not have an inverse.")
        
        inverse_mapping = {v: k for k, v in self.mapping.items()}
        return Function(set(self.codomain), set(self.domain), inverse_mapping)

    def __repr__(self) -> str:
        """
        Return a string representation of the function.

        Returns:
            str: A string representation of the function.
        """
        return f"Function(Domain: {self.domain}, Codomain: {self.codomain}, Mapping: {self.mapping})"
