# Mathematical Sets

## 1. Basic Concepts

**Definition**: A set is a well-defined collection of distinct objects, which can be anything: numbers, letters, symbols, or even other sets.

**Notation**:
- **Roster or Tabular Form**: Elements are listed within curly braces, separated by commas. 
  - Example: A = {1, 2, 3, 4, 5}
- **Set-Builder Form**: Describes the properties that its members must satisfy.
  - Example: B = {x | x is a positive even number}

## 2. Types of Sets

**Empty Set**: 
- Also called the null set, denoted by ∅ or {}. 
- Example: The set of all real numbers less than 0 that are also greater than 5, ∅.

**Finite and Infinite Sets**:
- **Finite Set**: Contains a limited number of elements.
  - Example: C = {a, b, c}
- **Infinite Set**: Contains an unlimited number of elements.
  - Example: The set of all natural numbers ℕ = {1, 2, 3, ...}

**Equal Sets**: Two sets A and B are equal if they contain exactly the same elements.
  - Example: A = {1, 2, 3} and B = {3, 2, 1}, so A = B.

**Subset and Proper Subset**:
- **Subset**: A ⊆ B if every element of A is also an element of B.
  - Example: A = {1, 2} ⊆ B = {1, 2, 3}
- **Proper Subset**: A ⊂ B if A ⊆ B and A ≠ B.
  - Example: A = {1, 2} ⊂ B = {1, 2, 3}

**Universal Set**:
- The set that contains all the objects under consideration, usually denoted by U.
  - Example: If U is the set of all natural numbers, A = {1, 2} ⊆ U.

**Power Set**:
- The set of all subsets of a given set A, denoted by P(A).
  - Example: If A = {1, 2}, then P(A) = {∅, {1}, {2}, {1, 2}}.

## 3. Operations on Sets

**Union**:
- The set of all elements that are in A or B or both, denoted by A ∪ B.
  - Example: A = {1, 2}, B = {2, 3}, A ∪ B = {1, 2, 3}

**Intersection**:
- The set of all elements that are in both A and B, denoted by A ∩ B.
  - Example: A = {1, 2}, B = {2, 3}, A ∩ B = {2}

**Difference**:
- The set of all elements that are in A but not in B, denoted by A - B.
  - Example: A = {1, 2, 3}, B = {2, 4}, A - B = {1, 3}

**Complement**:
- The set of all elements in the universal set U that are not in A, denoted by A' or A̅.
  - Example: If U = {1, 2, 3, 4} and A = {1, 2}, then A' = {3, 4}

## 4. Venn Diagrams

**Definition**: A Venn Diagram is a visual representation of sets and their relationships using circles.

- **Union**: Represented by the total area covered by circles of A and B.
- **Intersection**: Represented by the overlapping area of circles of A and B.
- **Difference**: Represented by the area of circle A excluding the overlapping part with B.
- **Complement**: Represented by the area outside the circle of A.

## 5. Advanced Concepts

**Cartesian Product**:
- The set of all ordered pairs from sets A and B, denoted by A × B.
  - Example: If A = {1, 2} and B = {a, b}, then A × B = {(1, a), (1, b), (2, a), (2, b)}

**Cardinality**:
- The number of elements in a set. For finite sets, it's simply the count of elements. For infinite sets, concepts like countable and uncountable infinity are used.
  - Example: |A| = 3 for A = {1, 2, 3}.

**Countable and Uncountable Sets**:
- **Countable Set**: A set is countable if its elements can be put into a one-to-one correspondence with the natural numbers.
  - Example: The set of all integers ℤ.
- **Uncountable Set**: A set that is not countable.
  - Example: The set of all real numbers ℝ.

## 6. Applications of Sets

**Database Management**:
- **Relations**: Tables can be viewed as sets of tuples.
- **Operations**: SQL operations like UNION, INTERSECT, and EXCEPT are based on set operations.

**Computer Science**:
- **Algorithms**: Use of sets in designing efficient algorithms.
- **Data Structures**: Sets are implemented in various data structures like hash sets.

**Probability Theory**:
- Events are considered as sets, and probabilities are calculated using set operations.

**Logic and Reasoning**:
- Sets are foundational in formulating and understanding logical statements and proofs.

## 7. Properties of Sets

**Idempotent Laws**:
- A ∪ A = A
- A ∩ A = A

**Identity Laws**:
- A ∪ ∅ = A
- A ∩ U = A

**Domination Laws**:
- A ∪ U = U
- A ∩ ∅ = ∅

**Complement Laws**:
- A ∪ A' = U
- A ∩ A' = ∅

**Associative Laws**:
- (A ∪ B) ∪ C = A ∪ (B ∪ C)
- (A ∩ B) ∩ C = A ∩ (B ∩ C)

**Commutative Laws**:
- A ∪ B = B ∪ A
- A ∩ B = B ∩ A

**Distributive Laws**:
- A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
- A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

## 8. Set Theory Paradoxes and Issues

**Russell's Paradox**:
- Considers the set of all sets that do not contain themselves.
  - Example: Let R = { x | x ∉ x }. Does R ∈ R hold? If R ∈ R, then R ∉ R, leading to a contradiction.

**Cantor's Theorem**:
- States that the power set of any set A has a strictly greater cardinality than A itself.
  - Example: There is no one-to-one correspondence between a set and its power set.

**Zermelo-Fraenkel Set Theory (ZF)**:
- A formal system that avoids paradoxes in naive set theory by using axioms.
- **Axioms include**: Extensionality, Pairing, Union, Power Set, Infinity, Replacement, Regularity, Choice.