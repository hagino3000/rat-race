import os
from setuptools import setup

version = '0.0.1'
name = 'trading-machine'
short_description = ''


setup(
    name=name,
    version=version,
    requirements=[],
    author='Takashi Nishibayashi',
    author_email="hagino.3000@gmail.com",
    description=short_description,
    url='https://github.com/hagino3000/rat-race',
    packages=['trading_machine'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
