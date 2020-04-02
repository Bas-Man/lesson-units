from setuptools import find_packages
from distutils.core import setup

setup(
    name='units',
    version='0.1.0',
    author='Adam Spann',
    author_email='baspann@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description='Module for handling Units for Lessons',
    long_description=open('README.md').read(),
    install_requires=[],
)
