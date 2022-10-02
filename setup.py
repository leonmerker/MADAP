#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst', encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding="utf-8") as history_file:
    history = history_file.read()

requirements = ["attrs==21.4.0",
        "matplotlib==3.5.3",
        "numpy==1.22.4",
        "pandas==1.4.2",
        "PySimpleGUI==4.60.3",
        "pytest==7.1.2",
        "scikit_learn==1.1.2",
        "impedance==1.4.1"]

test_requirements = ['pytest>=3', ]

setup(
    author="Fuzhan Rahmanian",
    author_email='fuzhanrahmanian@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="This is MADAP, a software package for the analysis of electrochemical data.",
    entry_points={
        'console_scripts': [
            'cli=src.madap_cli:main',
            'gui=src.madap_gui:main',
        ],
    },
    extra_requires={
        "dev": ["pytest>=3", ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='madap',
    name='MADAP',
    packages=find_packages(include=['src', 'src.*']),
    #package_dir = {'': 'src'},
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/fuzhanrahmanian/MADAP',
    version='0.8.0',
    zip_safe=False,
)
