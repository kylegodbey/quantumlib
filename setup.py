# -*- coding: utf-8 -*-

"""Distutils setup.py."""

from setuptools import setup, find_packages

from quantumlib import __version__

setup(
    name='quantumlib',
    version=__version__,
    description='Fork of IBM Quantum Challenge API',
    long_description='Fork of IBM Quantum Challenge API implementing changes for a more cutesy visualizer',
    url='',
    author='IBM Quantum Community Team',
    author_email='me@kyle.ee',
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6.9",
        "Topic :: Scientific/Engineering",
    ],
    keywords="iqx quantum flask challenge may 4th anniversary birthday",
    packages=find_packages(include=[
        'quantumlib',
        'quantumlib.*',
        'qlib_common',
        'qlib_common.*'
    ]),
    install_requires=[
        'seaborn',
        'requests',
        'qiskit-terra>=0.13',
        'qiskit-aer>=0.5',
        'numpy',
        'ipython',
        'ipywidgets',
        'matplotlib'
    ],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6.9",
)
