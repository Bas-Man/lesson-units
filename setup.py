from setuptools import find_packages
from distutils.core import setup

requirements = []

setup(
    name='units',
    version='0.1.0',
    author='Adam Spann',
    author_email='baspann@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description='Module for handling Units for Lessons',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7'
    ],
    python_requires='>=3',
    install_requires=requirements,
    extra_requires={
        'dev': [
            'pytest',
            'unittest',
            'coverage',
            'pytest-cov'
        ],
    }
)
