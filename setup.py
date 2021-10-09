from setuptools import find_packages, setup

setup(
    name='Travel Calculator',
    version='1.0.0',
    description='Handle travel salesman problem',
    author='Dusan Markovic',
    author_email='dusan91judo@gmail.com',
    url='https://github.com/dusan91judo/travel_calulator',
    packages=find_packages(exclude=('tests*', ))
)