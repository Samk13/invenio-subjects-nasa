# -*- coding: utf-8 -*-

"""Nasa subject terms for InvenioRDM"""

from setuptools import find_packages, setup

readme = open("README.md", encoding="utf-8").read()
history = open("CHANGES.md", encoding="utf-8").read()

tests_require = [
    "pytest-invenio>=1.4.0",
]

dev_requires = ["click>=7.0", "pyyaml>=5.4.1"]

extras_require = {"tests": tests_require, "dev": dev_requires}

extras_require["all"] = []
for reqs in extras_require.values():
    extras_require["all"].extend(reqs)

packages = find_packages()

setup(
    name="invenio-subjects-nasa",
    description=__doc__,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    keywords="invenio inveniordm subjects nasa",
    license="MIT",
    author="KTH Royal Institute of Technology",
    author_email="info@kth.se",
    url="https://github.com/Samk13/invenio-subjects-nasa",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    extras_require=extras_require,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
