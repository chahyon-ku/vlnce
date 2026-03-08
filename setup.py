from setuptools import setup, find_packages

setup(
    name="vlnce",
    packages=find_packages(include=["vlnce_baselines", "habitat_extensions"]),
)