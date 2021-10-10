from setuptools import find_packages, setup

setup(
    name='travel-calculator',
    version='1.0.7',
    description='Handle travel salesman problem',
    author='Dusan Markovic',
    author_email='dusan91judo@gmail.com',
    url='https://github.com/dusan91judo/travel_calculator',
    packages=find_packages(exclude=('tests*', )),
    install_requires=[
        'ortools==9.1.9490'
    ]
)
