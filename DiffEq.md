# Slope fields

[Vid on Khan](https://youtu.be/8Amgakx5aII)

# Euler's Method 

[Vid on Khan](https://youtu.be/q87L9R9v274)

# Separable Differential Equations

Take the form 

$$
\frac{dy}{dx} = g(x)h(y)
$$

[Vid on Khan](https://youtu.be/DL-ozRGDlkY).  Easiest type of one to solve without needing numerical approximation methods.

These are differential equations where you can get y and dy on one side, and x and dx on the other side.  Then you can integrate both sides.

Note that this involves doing mathematically meaningless stuff with floating dys and dxs.  [Explained here on MSE](https://math.stackexchange.com/a/1252426/49487) why this works.

[add formula from wiki]

Note: Be extra careful to keep track of Constants of Integration.  They can determine the answer.

# Growth Models

[Khan Vid](https://youtu.be/_JpS8k1a9yE) covers the way $N = Ce^{rt}$ from $\frac{dN}{dt} = rN$.  Then Verhulst gave a rigorous version of Malthus which incorporated restraints which is

# Logistic Differential Equation

On AP Calc [Logistic Equations](https://youtu.be/NU1v-8VRirU), we start with the Logistic Differential Equation:

$$\frac{dN}{dt} = rN(1-\frac{N}{k})$$


And we want to get to $N(t)$. This involves algebraically rearrange the differntial equation and taking advantage of partial fractions to get it more integrable on the left hand side, til we arrive at:

$$
\frac{N}{1-\frac{N}{k}} = Ce^{rt} 
$$

Now our best bet is to take the reciprocal [Is this the general Bernoulli Diff Eq approach?]

$$
\frac{1-\frac{N}{k}}{N} = Ce^{-rt} \\
\frac{1}{N} = Ce^{-rt} +\frac{1}{k} \\
N(t) = \frac{1}{Ce^{-rt} +\frac{1}{k}} \\
$$

Now we want to solve for $C$ by looking at $N(0)$

$$
N_0 = \frac{1}{C +\frac{1}{k}} \\
\frac{1}{N_0} = C + \frac{1}{k} \\
C = \frac{1}{N_0} - \frac{1}{k} \\
$$

Plugging C back in:

$$
N(t) = \frac{1}{(\frac{1}{N_0} - \frac{1}{k})e^{-rt} +\frac{1}{k}} \\
$$

Let's clean up those fractions in the denominator by multiplying:
$$
N(t) = \left(\frac{1}{(\frac{1}{N_0} - \frac{1}{k})e^{-rt} +\frac{1}{k}}\right)\left(\frac{N_0k}{N_0k}\right) \\
$$

$$
N(t) = \frac{N_0k}{(k - N_0)e^{-rt} + N_0} \\
$$

## Inflection Point of Logistic Curve

Just like any other function, find when $f'' = 0$.




# Bernoulli Differential Equation

Logistic Differential Equation is an example of a [Bernoulli Differential Equation](https://brilliant.org/wiki/bernoullis-equation/).
