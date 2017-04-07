#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="Tornado-MySQL",
    version="0.5.2",
    url='https://github.com/PyMySQL/Tornado-MySQL',
    author='INADA Naoki',
    author_email='songofacandy@gmail.com',
    description='Pure Python MySQL Driver for Tornado',
    install_requires=['tornado>=4.0'],
    license="MIT",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Database',
    ],
)
