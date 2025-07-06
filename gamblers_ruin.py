import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():

    import marimo as mo

    return (mo,)


@app.cell
def header(mo):
    mo.md(rf"""# Gambler's ruin""")
    return


if __name__ == "__main__":
    app.run()
