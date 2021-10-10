from setuptools import find_packages, setup

setup(
    name='travel-calculator',
    version='1.0.5',
    description='Handle travel salesman problem',
    author='Dusan Markovic',
    author_email='dusan91judo@gmail.com',
    url='https://github.com/dusan91judo/travel_calulator',
    packages=find_packages(exclude=('tests*', )),
    install_requires=[
        'ortools==9.1.9490'
    ]
)
