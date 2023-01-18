from setuptools import setup


# -----------------------------------------------------------------------------
# RUN setup() FUNCTION
# -----------------------------------------------------------------------------

setup(
    name="astrowoche",
    version="0.0.1",
    description=(
        "astrowoche: All the functions I need to study my data."
    ),
    author="Markus Bonse",
    license="MIT License",
    url="https://github.com/markusbonse/demo_astrowoche.git",
    install_requires=[
        "astropy",
        "numpy",
        "pandas",
        "jupyter",
        "scikit-learn",
        "scipy>=1.7"],
    packages=["astrowoche"],
    zip_safe=False,
)
