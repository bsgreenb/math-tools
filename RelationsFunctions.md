# Relations

A **relation** $R$ on a set $X$ is a subset of $ X \times X $. (Note: ~ can also be used for relation in place of R).

A **binary relation** $R$ from $A$ to $B$ is a subset of $ A \times B $, which is a collection of ordered pairs $(a, b)$ where $a$ comes from $A$ and $b$ comes from $B$.  We can write $aRb$ to mean $a$ is related to $b$.

Example definition of greater than relation on the set of real numbers.

$$ R : \{(x,y) \in \mathbb{Z} | x > y\} $$

## Reflexive, Symmetric, and Transitive Relations

**Reflexive**: $\forall x[xRx]$

**Symmetric**: $\forall(x,y)[xRy \rightarrow yRx]$

**Transitive**: $\forall(x,y,z)[xRy \land yRZ \rightarrow xRZ] $

Note on syntax used here: It should be fine to use one quantifier on multiple variables https://math.stackexchange.com/questions/4323172/is-there-a-difference-between-using-two-vs-one-universal-quantifier-for-two-vari

Operators can be expressed in terms of these types of relations.  For example $\leq$ is reflexive and transitive, but not symmetric.  $=$ is all 3, making it and equivalence relation.

**Equivalence relation** means it's Reflexive, Symmetric, and Transitive.  Suppose $R$ is an equivalence relation on set $X$.  Then, we can represent the **equivalence classes** $\forall x \in X [x] = \{y|xRy\}$

Basically, $[x]$ is set of all $y$ related to $x$.  We can express an equivalence relation as $[x] = [y] \lor [x] \cap [y] = \emptyset$.  Let's get more concrete for a sec:

$$
\begin{align*}
& X = \{1,2,3\} \\
& R = \{(1,1),(2,2),(3,3),(2,3),(3,2) \} \\
& [1] = \{1\}, [2] = [3] = \{2, 3\} \quad\text{We get these equivalence classes}\\
\end{align*}
$$

Moving on, **Antisymmetry** is defined as: $ (aRb \land bRa) \rightarrow a = b$.  Example operators that fall under this definition: $\leq, \geq, \subset$.

Being a **Partial Order** means a relation is Anti-symmetric, Reflexive, and Transitive.  The previously mentioned operators can be described as such, as could alphabetical ordering.


# Functions

[Note: This writeup could definitely be improved]

$$ f : X \rightarrow Y $$

A **function** $f$ maps $X$ to $Y$.  $X$ is the **Domain**, $Y$ is the **Codomain**. **Range**/**Image** is a subset of Codomain, and is set of all values of $y = f(x)$.  The set of all $x$ in the Domain ($x \in X$) is called the **Pre-Image**. 

[Wiki](https://en.wikipedia.org/wiki/Function_(mathematics)) seems better on this than the stuff I was reading. 

The key requirement of a function is that there is never more than one value of f(x) for a given x. If this rule is broken, what you're dealing with is a relation.

You can also think of a function as the cartesian product of the domain and the co-domain, indexed by the domain.

Functions have the requirement that there's one associated image for each x in the domain.  We can call the domain initially under consideration the **Domain of Definition** (another called it **Pre-Domain**).  **Total Functions** have the whole Domain of Definition as their Domain -- every x has an image f(x). [Partial Functions](https://en.wikipedia.org/wiki/Partial_function) have values that aren't fully defined (don't have an image f(x)).  You'll typically just here a Partial Function called a Function.. because when we look at something like with no 0 allowed in denominator, we're basically dealing with a Partial Function and act accordingly.  It's basically like in coding where you either have f(x) in Y or else f(x) is undefined.

You can technically return multiple values from a function if you return them as a Set.  Then you got a [Multivalued function](https://en.wikipedia.org/wiki/Multivalued_function)
$$
\begin{align*}
& f(x) = x^2, x \in \mathbb{Z} \\
& f : X \rightarrow \mathbb{Z^+} \\
& \mathrm{range}(f) = \{x^2 \in \mathbb{Z^+} | \sqrt{x} \in \mathbb{Z} \}
\end{align*}
$$

[should have the image here]


Good overview of domain/codomain/range by [MathIsFun](https://www.mathsisfun.com/sets/domain-range-codomain.html).  Key point, is the codomain is kind of a bounding guess 
> sometimes we don't know the exact range (because the function may be complicated or not fully known), but we know the set it lies in (such as integers or reals). So we define the codomain and the range is a subset of that.

## Well-Definedness

Sometimes the same input can be written in more than one valid way (for example, an equivalence class $[x]$ has many representatives, or an element of a group can be written as different powers $a^c = a^d$). When that happens, a candidate function is only a genuine function if every valid representation of the input produces the same output. If two representations could give different outputs, the rule isn't single-valued and so isn't a function at all. Showing this can't happen is called proving the function is **well-defined**.

The proof template looks like:

$$
\begin{aligned}
& \text{Suppose } a^c = a^d \\
& \quad \vdots \\
& \text{Therefore } f(a^c) = f(a^d) \\
& \text{So } f \text{ is well-defined}
\end{aligned}
$$

That is: assume two expressions denote the same input, then derive that $f$ assigns them the same output.

## Characteristic Function
$$
f(x) =
\begin{cases}
0 ~&\text{ if }~ x \notin A \\
1 ~&\text{ if }~ x \in A
\end{cases}
$$

Acts like a truth table for set membership.

## Injective, Surjective, and Bijective Functions
Good [coverage on wiki](https://en.wikipedia.org/wiki/Function_(mathematics)#Injective,_surjective_and_bijective_functions).

Let's describe the case of 

$$ f : X \rightarrow Y $$

**Injective** - one-to-one. No repeat y values. f has a **left inverse**

If $x_1 \neq x_2$, then $f(x_1) \neq f(x_2) $.

**Surjective** - onto.  every value of Y (the co-domain) is covered by a corresponding input x.  Range = codomain in this case.  f has a **right inverse**

$ \forall y \in Y[\exists x \in X[f(x) = y]] $

**Bijective** - injective and surjective (see above).  $|X| = |Y|$ for these. f has an **inverse**

## Composite Functions
$$
\begin{align*}
& f: X \rightarrow Y \\
& g: Y \rightarrow Z \\
& g \circ f \rightarrow Z  \\
& (g \circ f)(x) = g(f(x))
\end{align*}
$$

Composite Functions are a more specific case of [Composite Relations](https://en.wikipedia.org/wiki/Composition_of_relations).

Also one thing I'm seeing is that the members of a set are implicitly the lower case of it, like element $x$ in set $X$.

Injectivity and Surjectivity of Composite Functions:

- If $f$ and $g$ are injective, then $g \circ f$ is injective.
- If $f$ and $g$ are surjective, then $g \circ f$ is surjective.
- If $f$ and $g$ are bijective, then $g \circ f$ is bijective.

## Inverse Functions

The **inverse** of $f : A \rightarrow B$ is a function $f^{-1}: B \rightarrow A$ such that

$$
x=f^{-1}(y) \text { if and only if } y=f(x)
$$

Can think of an inverse as undoing a function.  $1/x$ its own inverse, $ln(x)$ and $e^x$ each others inverses (over a restricted domain).

A function $f : A \rightarrow B$ has an inverse if and only if it is bijective. In that case, the inverse $f^{-1}$ is a bijective function from $B$ to $A$.

Functions that are their own inverses are called **involution**s.

## Image and Pre-Image

Suppose $f: A \rightarrow B$ is a function.
1. If $X \subseteq A$, the image of $X$ is the set $f(X)=\{f(x): x \in X\} \subseteq B$.
2. If $Y \subseteq B$, the preimage of $Y$ is the set $f^{-1}(Y)=\{x \in A: f(x) \in Y\} \subseteq A$.

## Periodicity

A function f is said to be **periodic** of period a if there is a number a, called the period of f, such that f(x) = f(x + na) for every x ∈  and n ∈ .”


A function $f$ is said to be **periodic** of period $a$ if there is a number $a$, called the **period** of $f$, such that $f(x) = f(x + na)$ for every $x \in \mathbb{R}$ and $n \in \mathbb{Z}$.
