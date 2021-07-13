#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    README = fh.read()

NAME = "archABM"
DESCRIPTION = "Agent based simulation for architectural spaces"
URL = "https://github.com/VicomtechV3/ArchABM"
AUTHOR = "VicomtechV3"
AUTHOR_EMAIL = "imartinez@vicomtech.org"
CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]
ENTRY_POINTS = {
    "console_scripts": [
        #'tsclust=tsclust:main',
    ],
}
PROJECT_URLS = {
    "Bug Reports": URL + "/issues",
    "Documentation": "https://archABM.readthedocs.io",
    "Source Code": URL,
}
REQUIRES_PYTHON = ">=3.5, <4"
EXTRAS_REQUIRE = {}
KEYWORDS = ["agent simulation", "architecture", "building", "workplace", "discrete-event"]
LICENSE = "MIT license"
TEST_SUITE = "tests"
REQUIREMENTS = ["simpy", "tqdm", "jsonschema"]
SETUP_REQUIREMENTS = []
TEST_REQUIREMENTS = ["pytest", "pytest-cov"]
VERSION = "0.0.1"

setuptools.setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=CLASSIFIERS,
    description=DESCRIPTION,
    entry_points=ENTRY_POINTS,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=False,
    install_requires=REQUIREMENTS,
    keywords=KEYWORDS,
    license=LICENSE,
    long_description=README,
    name=NAME,
    package_data={},
    packages=setuptools.find_packages(),
    project_urls=PROJECT_URLS,
    python_requires=REQUIRES_PYTHON,
    setup_requires=SETUP_REQUIREMENTS,
    test_suite=TEST_SUITE,
    tests_require=TEST_REQUIREMENTS,
    url=URL,
    version=VERSION,
    zip_safe=False,
)
