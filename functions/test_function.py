import unittest
from functions.functions import Function

# python -m unittest ./functions/test_function.py
class TestFunction(unittest.TestCase):
    def setUp(self):
        self.domain = {1, 2, 3}
        self.codomain = {4, 5, 6}
        self.mapping = {1: 4, 2: 5, 3: 6}
        self.function = Function(self.domain, self.codomain, self.mapping)

    def test_apply(self):
        self.assertEqual(self.function.apply(1), 4)
        self.assertEqual(self.function.apply(2), 5)
        self.assertEqual(self.function.apply(3), 6)
        with self.assertRaises(ValueError):
            self.function.apply(4)  # Not in domain

    def test_is_injective(self):
        self.assertTrue(self.function.is_injective())
        non_injective_function = Function(self.domain, self.codomain, {1: 4, 2: 4, 3: 6})
        self.assertFalse(non_injective_function.is_injective())

    def test_is_surjective(self):
        self.assertTrue(self.function.is_surjective())
        non_surjective_function = Function(self.domain, self.codomain, {1: 4, 2: 4, 3: 4})
        self.assertFalse(non_surjective_function.is_surjective())

    def test_is_bijective(self):
        self.assertTrue(self.function.is_bijective())
        non_bijective_function = Function(self.domain, self.codomain, {1: 4, 2: 4, 3: 5})
        self.assertFalse(non_bijective_function.is_bijective())

    def test_inverse(self):
        inverse_function = self.function.inverse()
        expected_inverse_mapping = {4: 1, 5: 2, 6: 3}
        self.assertEqual(inverse_function.mapping, expected_inverse_mapping)

        non_bijective_function = Function(self.domain, self.codomain, {1: 4, 2: 4, 3: 5})
        with self.assertRaises(ValueError):
            non_bijective_function.inverse()  # Should raise an error

if __name__ == "__main__":
    unittest.main()