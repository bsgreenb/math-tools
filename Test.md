Let $\langle a\rangle$ be cyclic of order $mn$, where $\gcd(m,n)=1$. 
Prove that $\langle a\rangle \cong \langle a^m\rangle \times \langle a^n\rangle.$ 

Define

$$
f:\langle a\rangle \to \langle a^m\rangle \times \langle a^n\rangle
$$

by

$$
f(a^x) = \bigl((a^x)^m,(a^x)^n\bigr)  \text{ for } x \in \mathbb{Z}.
$$

$f$ is well-defined, because if we suppose that $a^c=a^d$ then:
$$
f(a^c)
=
\bigl((a^c)^m,(a^c)^n\bigr)
=
\bigl((a^d)^m,(a^d)^n\bigr)
=
f(a^d).
$$

Since $|a|=mn$,

$$
|\langle a^m\rangle|
=
|a^m|
=
\frac{mn}{\gcd(mn,m)}
=
\frac{mn}{m}
=
n.
$$

Similarly, $|\langle a^n\rangle|=m.$

Therefore, $|\langle a^m\rangle \times \langle a^n\rangle| = |\langle a^m\rangle|\,|\langle a^n\rangle| = nm = |\langle a\rangle|$.

$f$ is injective, because if we suppose

$$
\begin{aligned}
f(a^c) &= f(a^d) \\
\bigl((a^c)^m,(a^c)^n\bigr)
&=
\bigl((a^d)^m,(a^d)^n\bigr)
\end{aligned}
$$

Comparing first coordinates gives

$$
\begin{aligned}
(a^m)^c &= (a^m)^d \\
(a^m)^{c-d} &= e
\end{aligned}
$$

Since $|a^m|=n$, it follows that $n\mid(c-d).$ Likewise, comparing second coordinates gives $m\mid(c-d)$.

Since $\gcd(m,n)=1$, we have

$$
mn\mid(c-d).
$$

Because $|a|=mn$,

$$
\begin{aligned}
a^{c-d} &= e \\
a^c &= a^d
\end{aligned}
$$

Thus $f$ is injective.

Since $f$ is an injection between finite sets of equal cardinality, $f$ is bijective.

Finally, for all $c,d\in\mathbb Z$,

$$
\begin{aligned}
f(a^c a^d)
&= f(a^{c+d}) \\
&= \bigl((a^m)^{c+d},(a^n)^{c+d}\bigr) \\
&= \bigl((a^m)^c,(a^n)^c\bigr)
   \bigl((a^m)^d,(a^n)^d\bigr) \\
&= f(a^c)f(a^d).
\end{aligned}
$$

Therefore $f$ is a bijective homomorphism, so

$$
\langle a\rangle \cong \langle a^m\rangle \times \langle a^n\rangle.
$$