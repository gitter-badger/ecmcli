#!/usr/bin/env python

from setuptools import setup, find_packages

README = 'README.md'


def long_desc():
    try:
        import pypandoc
    except ImportError:
        with open(README) as f:
            return f.read()
    else:
        return pypandoc.convert(README, 'rst')

setup(
    name='ecmcli',
    version='2.4.0',
    description='Command Line Interface for Cradlepoint ECM',
    author='Justin Mayfield',
    author_email='tooker@gmail.com',
    url='https://github.com/mayfield/ecmcli/',
    license='MIT',
    long_description=long_desc(),
    packages=find_packages(),
    test_suite='test',
    install_requires=[
        'syndicate==1.2.0',
        'shellish>=0.8.0',
        'humanize'
    ],
    entry_points = {
        'console_scripts': ['ecm=ecmcli.main:main'],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
    ]
)
