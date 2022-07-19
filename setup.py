# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="swl_sample_project_repository",
    version="0.0.1.dev0",
    description="Sample package for Wavelength-Project.org",
    long_description=readme,
    author="YOUR NAME",
    author_email="YOUR.NAME@simmons-simmons.com",
    url="https://gitlab.com/dashboard/projects",
    license=license,
    python_requires=">=3.6",
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "numpy",
    ],
    zip_safe=False,
    include_package_data=True,
)
