import unittest
from sets import Set

class TestSet(unittest.TestCase):
    def setUp(self):
        self.set_a = Set({1, 2, 3})
        self.set_b = Set({3, 4, 5})
        self.universe = Set({1, 2, 3, 4, 5, 6})

    def test_add_remove(self):
        set_a = self.set_a
        set_a.add(4)
        self.assertEqual(set_a, Set({1, 2, 3, 4}))
        set_a.remove(2)
        self.assertEqual(set_a, Set({1, 3, 4}))

    def test_union(self):
        self.assertEqual(self.set_a.union(self.set_b), Set({1, 2, 3, 4, 5}))

    def test_intersection(self):
        self.assertEqual(self.set_a.intersection(self.set_b), Set({3}))

    def test_difference(self):
        self.assertEqual(self.set_a.difference(self.set_b), Set({1, 2}))

    def test_symmetric_difference(self):
        self.assertEqual(self.set_a.symmetric_difference(self.set_b), Set({1, 2, 4, 5}))

    def test_complement(self):
        self.assertEqual(self.set_a.complement(self.universe), Set({4, 5, 6}))

    def test_is_subset(self):
        self.assertTrue(Set({1, 2}).is_subset(self.set_a))
        self.assertFalse(self.set_a.is_subset(self.set_b))

    def test_is_superset(self):
        self.assertTrue(self.set_a.is_superset(Set({1, 2})))
        self.assertFalse(self.set_a.is_superset(self.set_b))

    def test_power_set(self):
        power_set = self.set_a.power_set()
        expected_power_set = Set([
            frozenset(), frozenset({1}), frozenset({2}), frozenset({3}),
            frozenset({1, 2}), frozenset({1, 3}), frozenset({2, 3}),
            frozenset({1, 2, 3})
        ])
        self.assertEqual(power_set, expected_power_set)


if __name__ == "__main__":
    unittest.main()