from setuptools import setup

setup(
    name="model epidemii",
    version="0.1",
    packages=["sir_model"],
    install_requires=[
        "matplotlib==3.4.1",
        "numpy==1.20.2",
        "PySimpleGUI==4.55.1",
        "scipy==1.6.2",
    ],
)
