See also: [Sets](Sets.md)

# Propositional Logic

**Statement** is a a declarative sentence that can be True (1) or False (0).  A **Proposition** is the meaning expressed by that statement.

Syntax: **well formed formulas (WFFs)** are combinations of Propositions, Connectives, punctuation, and other woofs.  Propositions cannot be based around variables, like in first order logic.

$ \top \quad$ Tautology.  Unconditionally True.

$ \bot \quad$ Contradiction.   

A woof that is neither a Tautology nor a Contradiction is called Contingent.

## Logical Operators

$ \lnot A \quad$ Not A

$ A \land B \quad$ A And B 

$ A \lor B \quad$ A Or B

$ A \oplus B \quad$ A Xor B

$ A \uparrow B \quad$ A NAnd B

$ A \rightarrow B = \lnot A \lor B \quad$ A Implies B = A or Not B. Material implication.

$ A \leftrightarrow B = (A \rightarrow B) ^ (B \rightarrow A) \quad$ Biconditional, material equivalence. If and only if (iff)

$ x := y \quad$ x is defined as y. $:=$ is Definition.

$ \therefore \quad$ Therefore.

### Meta-logical operators

A quick note on meta-logic.  The operators used above are for specific A's and B's, but meta-logic is meant to apply to any wffs, in other words, these operators deal in tautologies and logical equivalence, rather than material equivalence.  See [Material vs Logical Implication on SE](https://math.stackexchange.com/questions/68932/whats-the-difference-between-material-implication-and-logical-implication).

Here are our meta-logical operators:

$ A \Rightarrow B \quad$ Logical Implication. 

$ A \Leftrightarrow B \quad$ Logical Equivalence. $ \equiv $ is also used here. 

$ A \vdash B \quad $ A Proves B

$ A \models B \quad $ A Models B

Note that in a logical system that is meta-logically **Sound** (like First Order Logic):

$$ A \vdash B \implies A \models B $$

And in a logical system that is meta-logically **Complete** (like First Order Logic):

$$ A \models B \implies A \vdash B $$

We will use these meta-logical operators (specficallty $ \Leftrightarrow $ and $ \vdash $) to define the following Logic Laws themselves, whereas you would use the logical operators above when actually applying these rules.

Note: Many of these symbols are overridden by different logical conventions, especially the double arrow may be material equivalence to some people.  Still, I'll use it here and maintain the single (material) vs double (logical) arrow distinction.

## Logic Laws

Note that these rules have corresponding [Set](Sets.md) Laws.

### Rules of Replacement

The Rules of Replacement go both ways, and are thus indicated with logical equivalence operator $ \Leftrightarrow $.

**Identity**: 
$$ P \land \top \Leftrightarrow P $$
$$ P \lor \bot \Leftrightarrow P $$

**Domination**:
$$ P \lor \top \Leftrightarrow \top $$
$$ P \land \bot \Leftrightarrow \bot $$

**Double Negation**:
$$ \lnot \lnot P \Leftrightarrow P $$

**De Morgans's Law**:
$$ \lnot (P \lor Q) \Leftrightarrow \lnot P \land \lnot Q $$
$$ \lnot (P \land Q) \Leftrightarrow \lnot P \lor \lnot Q $$

**Distributive**:
$$ P \lor (Q \land R) \Leftrightarrow (P \lor Q) \land (P \lor R) $$
$$ P \land (Q \lor R) \Leftrightarrow (P \land Q) \lor (P \land R) $$

**Composition**:
$$ ((p \rightarrow q)\land (p\to r)) \Leftrightarrow (p \rightarrow (q\land r)) $$


**Absorption**:
https://math.stackexchange.com/questions/4323450/why-is-the-absorption-law-considered-a-rule-of-inference-instead-of-replacement

**Commutativity**:

$$ P \lor Q \Leftrightarrow Q \lor P $$
$$ P \land Q \Leftrightarrow Q \land P $$

**Associativity**:

$$ P \lor (Q \lor R) \Leftrightarrow (P \lor Q) \lor R $$
$$ P \land (Q \land R) \Leftrightarrow (P \land Q) \land R $$

**Inverse**:

$$ P \lor \lnot P \Leftrightarrow \top $$
$$ P \land \lnot P \Leftrightarrow \bot $$

**Material Implication**:
$$ P \rightarrow Q \Leftrightarrow \lnot P \lor Q $$

### Rules of Inference 

A set of **Premises** $ p_1,p_2,\dots,p_n $ prove some conclusion $q$ in an **Argument**.  

$$
(p_1 \land p_2 \land \dots \land p_n) \implies q
$$

An argument is **Valid** if the premises logically entail the conlcusion.  An argument is **Sound** if the premises are also true.

The Rules of Inference go in one direction, unlike the Rules of Replacement.  We use the Proves operator $ \vdash $ here, even though we could use $ \Rightarrow $ to indicate Logical Implication.  We favor the less ambiguous operator, since it's possible here. 

**Modus Ponens (MPP)**:

$$ ((P \rightarrow Q) \land P) \vdash Q $$

**Modus Tollens (MT)**:

$$ ((P \rightarrow Q) \land \lnot Q) \vdash \lnot P $$ 

**Hypothetical Syllogism (HS)**:

$$ ((P \rightarrow Q) \land (Q \rightarrow P)) \vdash P \rightarrow R $$

**Disjunctive Syllogism (DS)**:

$$ ((P \lor Q) \land \lnot P) \vdash Q $$

**Disjunction Introduction ( $\lor$ I)**  aka **Addition (A)** :

$$ P \vdash (P \lor Q) $$

**Disjunction Elimination ( $\lor$ E)** aka **Elimination**:

$$ ((P \rightarrow Q) \land (R \rightarrow Q) \land (P \lor R)) \vdash Q$$

**Conjunction Elimination ( $\land$ E)** aka **Simplification (S)**:

$$ (P \land Q) \vdash P $$

**Conjunction Introduction ( $\land$ I)** aka just **Conjunction**:

$$ P,Q \vdash (P \land Q) $$

### Conditionals

**Conditional**: $ A \rightarrow B $

**Converse**: $ B \rightarrow A $

**Inverse**: $ \lnot A \rightarrow \lnot B $

**Contrapositive**: $ \lnot B \rightarrow \lnot A $

Only Contrapositive is equivalent to the Conditional via Material Implication.

# First Order Logic

In **First Order Logic** aka **Predicate Logic** we get some extra abiltiies.  Now we can use Open Formulas like "x is greater than y" which are not evaluated to True or False (as opposed to a closed formula like 6 is greater than 2).

And more importantly we get Quantifiers.  Here be the quantifiers

$ \forall $ This symbol means for all (or sometimes, for every). For example, “∀ squares D, D is a rectangle”. **Universal Quantifier**.

$ \exists $ This symbol means there exists.  It can actually imply "there exists... such that" For example, “∃ a horse”. **Existential Quantifier**.

$ \nexists $ This symbol means there does not exist. For example, " $ \nexists $ a unicorn". (yet)

$ \exists! $ This symbol means only one exists. **Unique Quantifier**.


## Predicate Logic Rules

**Equivalencies**:

$$ \forall x P(x) \Leftrightarrow \lnot \exists x[\lnot P(x)] $$
$$ \exists x P(x) \Leftrightarrow \lnot \forall x[\lnot P(x)] $$
$$ \lnot \forall x[P(x)] \Leftrightarrow \exists x[\lnot P(x)] $$
$$ \lnot \exists x[P(x)] \Leftrightarrow \forall x[\lnot P(x)] $$

Note the pattern in terms of flipping quantifiers and negations.

**Universal Elimination** or **Universal Instantiation**: $ \forall x[P] \vdash P(a) $

**Universal Introduction** or **Universal Generalization**: $ P(x) \text{For arbitrary x} \vdash \forall x[P(x)] $

**Existential Elimination** or **Existential Instantiation**: $ (\exists x[P(x)] \vdash P(c) \text{For some c} $

**Existential Introduction** or **Existential Generalization**: $ P(c) \text{For some element c} \vdash \exists x[P(x)] $



# Proofs

**Theorem**s are what you prove with **axioms** and other theorems. A theorem is a wff that is true/a tautology without any premises/assumptions required.

The end of the proof may be signaled by the letters Q.E.D. (quod erat demonstrandum) or by one of the tombstone marks, such as "□" or "∎"

In a **Direct Proof**, you assume the **antecedent** is true, and prove the **consequent**.A

**Proof by Contraposition**: $ A \implies B $. Assume $ \lnot B $. Prove $A$.

**Proof by Case (Proof by Exhaustion)**: [give formal def]

**Proof by Contradiction**: We want to prove $A$.  Assume $\lnot A$, and show that this causes a Contradiction.

## Induction

Giving this its own section cus its so big. Note that induction is a form of Deductive Reasoning, so what we're doing here is not to be confused with other uses of the term.

**Base Case**: $n=1$ case is true

**Inductive Hypothesis**: Assume it's true for previous step $n \leq k$, show $k + 1$ is true.

Conclusion: Every $n$ is true.

[I'll def write more on this later.  I'll need more experience on Induction proofs in practice.]

[Also I think Induction itself depends on some set theory stuff like the successor function or the well ordering principle or somethin.. understand dat chain of logic.  "..err, successor is not an axiom, it is built up with von neumann ordinals.  but would like to reduce this from successor to sets in explanation.]

## Fitch Style Proof of Squeeze Theorem
My overly formal and yet unlabeled proof of Squeeze Theorem 

$$
\def\fitch#1#2{~~\begin{array}{|l} #1 \\ \hline #2 \end{array}}
\fitch{
    \forall \epsilon > 0 ~\exists \delta_1 > 0 ~\forall x[|x-c| < \delta_1 \rightarrow |f(x)-L| < \epsilon] \\
    \forall \epsilon > 0 ~\exists \delta_2 > 0 ~\forall x[|x-c| < \delta_2 \rightarrow |h(x)-L| < \epsilon] \\
    \forall \epsilon > 0 ~\exists \delta_3 > 0 ~\forall x[|x-c| < \delta_3 \rightarrow f(x) \leq g(x) \leq h(x)]}{
    \fitch{
        \epsilon > 0, x \in \mathbb{R}}{
        \fitch{
            \delta_1 > 0}{
            \begin{aligned}
            |x - c| < \delta_1 &\rightarrow |f(x) - L| < \epsilon \\
            \dots &\rightarrow -\epsilon < f(x) - L < \epsilon \\
            \end{aligned}
        } \\
        \fitch{
            \delta_2 >0}{
            \begin{aligned}
            |x - c| < \delta_2 &\rightarrow |h(x) - L| < \epsilon \\
            \dots &\rightarrow -\epsilon < h(x) - L < \epsilon \\
            \end{aligned}
        } \\
        \fitch{
            \delta_3 >0}{
            \begin{aligned}
            |x - c| < \delta_3 &\rightarrow f(x) \leq g(x) \leq h(x) \\
            \dots &\rightarrow f(x) - L \leq g(x) -L \leq h(x) -L \\
            \end{aligned}
        } \\
        \delta := \min(D := \{\delta_1, \delta_2, \delta_3\}) \\
        \forall \delta_{i} \in D ~(\delta > 0 \rightarrow \delta_{i} > 0) \land (|x-c| < \delta \rightarrow |x-c| < \delta_{i}) \\
        \fitch{
            \delta > 0}{
                \begin{aligned}
                |x - c| < \delta \rightarrow& -\epsilon < f(x) - L < \epsilon, \\
                &-\epsilon < h(x) - L < \epsilon, \\
                &f(x) -L \leq g(x) - L \leq h(x) -L \\
                \dots \rightarrow& -\epsilon<g(x)-L<\epsilon
                \end{aligned}
        }
    } \\
    \forall \epsilon > 0 ~\exists \delta > 0 \forall x[|x-c| < \delta \rightarrow |g(x) - L| < \epsilon] \\
    \lim\limits_{x\to c} g(x) = L
}
$$
