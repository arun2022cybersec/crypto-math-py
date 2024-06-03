from string_set import StringSet

# Demonstration class
class Demo:
    @staticmethod
    def run_demo():
        # Creating sets
        set_a = StringSet([1, 2, 3])
        set_b = StringSet([3, 4, 5])
        
        # Performing union
        union_set = set_a.union(set_b)
        print(f'Union of {set_a} and {set_b}: {union_set}')
        
        # Performing intersection
        intersection_set = set_a.intersection(set_b)
        print(f'Intersection of {set_a} and {set_b}: {intersection_set}')
        
        # Performing difference
        difference_set = set_a.difference(set_b)
        print(f'Difference of {set_a} and {set_b}: {difference_set}')
        
        # Performing complement
        universal_set = StringSet([1, 2, 3, 4, 5, 6, 7])
        complement_set = set_a.complement(universal_set)
        print(f'Complement of {set_a} with respect to {universal_set}: {complement_set}')
        
        # Checking subset
        print(f'Is {set_a} a subset of {universal_set}? {set_a.is_subset(universal_set)}')
        
        # Checking proper subset
        print(f'Is {set_a} a proper subset of {universal_set}? {set_a.is_proper_subset(universal_set)}')
        
        # Getting power set
        power_set = set_a.power_set()
        print(f'Power set of {set_a}: {power_set}')

# Running the demonstration
Demo.run_demo()
