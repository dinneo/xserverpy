#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "requests",
    "python-dateutil",
    "termcolor",
    "tabulate",
    "pytz",
    "tzlocal"
]

test_requirements = [
    "vcrpy"
]

setup(
    name='xserverpy',
    version='0.1.0',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    long_description=readme + '\n\n' + history,
    author="Omar Abdelhafith",
    author_email='o.arrabi@me.com',
    url='https://github.com/oarrabi/xserverpy',
    packages=[
        'xserverpy',
        'xserverpy.lib',
        'xserverpy.utils',
        'xserverpy.display',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='xserverpy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    entry_points={
     'console_scripts': [
         'xserverpy=xserverpy.xserverpy:start',
     ],
    },
    tests_require=test_requirements
)