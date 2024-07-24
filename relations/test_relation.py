import unittest
from relations.relations import Relation

# python -m unittest ./relations/test_relation.py
class TestRelation(unittest.TestCase):
    def setUp(self):
        self.set_a = {1, 2, 3}
        self.set_b = {4, 5, 6}
        self.relation = Relation(self.set_a, self.set_b, {(1, 4), (2, 5), (3, 6)})

    def test_is_reflexive(self):
        reflexive_relation = Relation(self.set_a, self.set_a, {(1, 1), (2, 2), (3, 3)})
        self.assertTrue(reflexive_relation.is_reflexive())
        self.assertFalse(self.relation.is_reflexive())

    def test_is_symmetric(self):
        symmetric_relation = Relation(self.set_a, self.set_a, {(1, 2), (2, 1)})
        self.assertTrue(symmetric_relation.is_symmetric())
        self.assertFalse(self.relation.is_symmetric())

    def test_is_transitive(self):
        non_transitive_relation = Relation(self.set_a, self.set_a, {(1, 2), (2, 3)})
        self.assertFalse(non_transitive_relation.is_transitive())
        transitive_relation = Relation(self.set_a, self.set_a, {(1, 2), (2, 3), (1, 3)})
        self.assertTrue(transitive_relation.is_transitive())

    def test_is_anti_symmetric(self):
        anti_symmetric_relation = Relation(self.set_a, self.set_a, {(1, 2), (2, 1)})
        self.assertFalse(anti_symmetric_relation.is_anti_symmetric())
        self.assertTrue(self.relation.is_anti_symmetric())

    def test_inverse(self):
        inverse_relation = self.relation.inverse()
        expected_inverse = Relation(self.set_b, self.set_a, {(4, 1), (5, 2), (6, 3)})
        self.assertEqual(inverse_relation, expected_inverse)

    def test_equality(self):
        same_relation = Relation(self.set_a, self.set_b, {(1, 4), (2, 5), (3, 6)})
        different_relation = Relation(self.set_a, self.set_b, {(1, 4), (2, 5)})
        self.assertEqual(self.relation, same_relation)
        self.assertNotEqual(self.relation, different_relation)

if __name__ == "__main__":
    unittest.main()