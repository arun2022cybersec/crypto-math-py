import unittest
from group_theory.group_theory import Group, Subgroup

class TestGroupTheory(unittest.TestCase):
    def setUp(self):
        self.elements = {0, 1, 2, 3}
        self.operation = lambda a, b: (a + b) % 4
        self.group = Group(self.elements, self.operation)

    def test_identity(self):
        self.assertEqual(self.group.identity(), 0)

    def test_inverse(self):
        self.assertEqual(self.group.inverse(1), 3)
        self.assertEqual(self.group.inverse(2), 2)
        self.assertEqual(self.group.inverse(3), 1)

    def test_is_group(self):
        self.assertTrue(self.group.is_group())

    def test_subgroup(self):
        subgroup_elements = {0, 2}
        subgroup = Subgroup(subgroup_elements, self.operation, self.group)
        self.assertTrue(subgroup.is_subgroup())

if __name__ == "__main__":
    unittest.main()
