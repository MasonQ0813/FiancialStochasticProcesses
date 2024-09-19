Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from setuptools import setup, find_packages
... 
... setup(
...     name="financial-stochastic-processes",  
...     version="0.1.0",  # Initial release version
...     author="Hao Quan",
...     author_email="h5quan@uwaterloo.ca",
...     description="A package for simulating financial stochastic processes (GBM, Jump Diffusion, Heston, Regime-Switching)",
...     long_description=open("README.md").read(),
...     long_description_content_type="text/markdown",
...     url="https://github.com/MasonQ0813/FiancialStochasticProcesses"
...     packages=find_packages(),
...     classifiers=[
...         "Programming Language :: Python :: 3",
...         "License :: OSI Approved :: MIT License",
...         "Operating System :: OS Independent",
...     ],
...     python_requires=">=3.6",
... )
