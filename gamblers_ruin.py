import marimo

__generated_with = "0.14.10"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    import polars as pl

    rng = np.random.default_rng(seed=12345)
    return mo, rng


@app.cell
def header(mo):
    mo.md(
        rf"""
    # Gambler's ruin

    This notebook provides both a calculation and a simulation of the Gambler's ruin problem.

    In short the problem is stated like this: 

    > Given two players $A$ and $B$ where player $A$ has $i$ points (coins/euro...) and player $B$ has $N-i$ points.
    > They play a game repeatedly where the probability that $A$ wins is $p$ and the probability that $B$ wins is $q=1-p$.
    > 
    > At each game each player puts down a point and the winner collects both points.
    >
    > They play repeateadly until either $A$ or $B$ end up winning all the money, i.e. they end up with $N$ points.

    What is the probability that $A$ wins all the money?
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    $$
    P_i = 
    \left\{ 
    \begin{array}{rcl} 
        \frac {1 - \bigl(\frac{q}{p}\bigl)^i}{1 - \bigl( \frac{q}{p}\bigl)^N} & for & p \neq q \\ 
    	i \over N & for & p = q
    \end{array}
    \right.
    $$
    """
    )
    return


@app.cell
def _(mo, rng):
    top_p = mo.ui.slider(start=0, stop=1, step=0.01, label="Top P", full_width=True, value=1)
    _num_samples = 20
    top_p_dist = rng.random(_num_samples)
    return (top_p,)


@app.cell(hide_code=True)
def top_p_graph(mo, top_p):
    _description = mo.md(
        """
        ## Top P (nucleus) sampling

        Sum the top most likely outcomes until you get to P.

        If you take top 0 ... you sample just the most probable

        If you take top 1 ... you sample from all probabilites
        """
    )

    _slider = mo.hstack([top_p, mo.md(f"Has value: {top_p.value:0.2f}")])

    mo.vstack([_description, _slider])
    return


if __name__ == "__main__":
    app.run()
