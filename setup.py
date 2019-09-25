from distutils.core import setup

setup(
    name="budgetDash",
    version="0.1dev",
    packages=["budget_dash", "data", "tests"],
    entry_points={"console_scripts": ["bdash=budget_dash.main:main"]},
)
