import io
import os
import sys

from setuptools import Command, find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pymodorino",
    version="0.0.2",
    author="Dominick Vale",
    author_email="dominickveil@gmail.com",
    description="Very simple and cross-platform (hopefully) pomodoro timer script.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DominickVale/Pymodorino",
    python_requires=">=3.6.0",
    keywords = ['pomodoro timer', 'pomodoro', 'timer'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=[
        "blessed",
        "notifypy"
    ],
)