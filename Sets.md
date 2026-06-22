Note: I wrote this out a while ago, before I did _The Book of Proof_.  I would recommend to go through The Book of Proof for learning the stuff you see here which was pulled from less organized or complete sources.

See also: [Logic](Logic.md)

A **Set** is a collection of of objects called elements.  Sets can be finite or infinite.

$$ A = \{1,2,3\} $$

$$ \mathbb{Z}^+ = \{1,2,3,4...\} $$

There is no repitition or order in sets:

$$ \{3,2,1\} = \{1,2,3,3\} $$

Our **Universe** is the set containing all the elements in our scope.

# Sets of Numbers

$ \mathbb{R} $ The set of real numbers.

$ \mathbb{Z} $ The set of integers. The numbers \{...,-3,-2,-1,0,1,2,3,\}.

$ \mathbb{N} $ The set of natural numbers. The numbers \{1,2,3,4,...\}

$ \mathbb{C} $ The set of complex numbers.

# Elements and Cardinality

$ \in $ is an element of

$ \notin $ is not an element of 

$ |S| $ number of elements of S (**Cardinality**)

# The empty set

$$ \emptyset = \{\} $$

$$ |\emptyset| = 0 $$

$$ |\{\emptyset\}| = 1 $$ 

# Set Builder and Interval Notation

**Set Builder Notation**: Elements on the left, conditions (or really predicate) on the right.

$$ \{\frac{m}{n} | m,n\in\mathbb{Z},n \ne 0\} $$

**Interval Notation**: 

- [ ] a square bracket when we want to include the end value, or
- ( ) a round bracket when we do Not want to

# Cartesian Products

An **ordered pair** $ (a, b) $ is a set 

$$ \{\{a\}, \{a,b\}\} $$

This provides order without sets having built in order.  This allows you to distinguish $(2,1)$ from $(1,2)$.

The **Cartesian Product** $ A \times B $, which is the set: 

$$ \{(x,y) | x \in A, y \in B\} $$

Don't confuse these with regular math products, they dont't have the same associativity and commutativity, via the order mattering.  Note that the cardinality does follow those rules tho..

Cardinality of Cartesian Products

$$ |A| \times |B| = |A \times B| $$

Empty set times anything will get you back the empty set:

$$ \emptyset \times A = \emptyset $$

# Subsets
If A is a **Subset** of B, then every element in A must also be in B. Subset

$$ \{1,2\} \subset \{1,2,3\} $$
$$ \{1,2\} \subset \{1,2\} $$

Proper subset means its not the same set, the subset being smaller. People diverge in their use here https://math.stackexchange.com/questions/1114920/does-anyone-use-subset-for-proper-subset-anymore

$$ \{1,2\} \subsetneq \{1,2,3\} $$

The empty set is a Subset of everything:

$$ \emptyset \subset A$$

# Power Sets
A **Power Set** of A, is the set containing all possible subsets of A.  We can use $p(A)$ for this, since I dont wanna use the BB notation for dis.

$$ 
\begin{align*}
& A = \{a,b\} \\
& p(A) = \{\{a,b\}, \{a\}, \{b\}, \emptyset \} \\
\end{align*}
$$

The size/cardinality of the powerset of a set is a power of 2 of that set's cardinality.

$$ |p(A)| = 2^{|A|} $$
$$ p(\emptyset) = \{\emptyset\} $$

# Set Operations

**Complement**: $ A' = \bar{A} = \{ x | x \notin A  \} $.  

**Intersection**: $ A \cap B = \{ x | x \in A, x \in B \} $

**Union**: $ A \cup B = \{ x | x \in A \lor x \in B \} $

**Difference**: $ A - B = A \setminus B = \{ x | x \in A,x \notin B \} $

**Symmetric Difference** or **Disjoint Union**: $ A \oplus B = A \triangle B = A \{ x | x \in A \oplus x \in B \} $

Note I wrote out both notations I'm seein out there for Complement, Difference, and Symmetric Difference. 

# Set Laws

Note that these rules have corresponding Logic Laws.  I believe this is because they're both boolean algebras.

https://web.uvic.ca/~gmacgill/LFNotes/LawsOfSetTheory.pdf 

# Indexed Sets

You can iterate over Union and Intersection with this notation:

**Union of Indexed Set** 
$$ 
\bigcup_{i=0}^{n} F_{i} = {A}_{0}\cup{A}_{1}\cup{A}_{2}\cup\dots\cup{A}_n 
$$

**Intersection of Indexed Set** 
$$ 
\bigcap_{i=0}^{n} F_{i} = {A}_{0}\cap{A}_{1}\cap{A}_{2}\cap\dots\cap{A}_n 
$$


# Partition

A **partition** of a set $A$ is a set of non-empty subsets of $A$, such that the union of all the subsets equals $A$, and the intersection of any two subsets is $\emptyset$.


# See Also

[Relations/Functions](RelationsFunctions.md) which are based like everything else on sets.
