from setuptools import setup, find_packages

setup(
    name="financial_stochastic_processes",
    version="0.1.3",
    author="Hao Quan",
    author_email="h5quan@uwaterloo.ca",
    description="A package for simulating financial stochastic processes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MasonQ0813/FiancialStochasticProcesses",  # Example URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
    ],
)
