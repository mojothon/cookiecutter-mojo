#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for cookiecutter-mojo."""

from setuptools import setup

__version__ = "0.1.0"

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-mojo",
    version=__version__,
    description="a template for quickly creating mojo projects with Cookiecutter.",
    long_description=long_description,
    author="llango",
    author_email="rontomai@gmail.com",
    url="https://github.com/llango/cookiecutter-mojo",
    download_url="",
    packages=[],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
    keywords=(
        """
        cookiecutter, Python, projects, project templates, mojo,
        skeleton, scaffolding, project directory, setup.py
        """
    ),
)
