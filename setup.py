import re
from codecs import open
from os import path, environ

from setuptools import setup

VERSION = "0.1.0"

PACKAGE_NAME = "QuartzEngine"
HERE = path.abspath(path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()

extras = {
    "lint": ["colorama", "getkey"]
}

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author="Bloodhaven Studios",
    author_email="",
    description="An advanced game-engine for creating advanced text-based games in the terminal.",
    extras_require=extras,
    include_package_data=True,
    install_requires=["colorama", "git+https://github.com/li-rupert/getkey"],
    license="MIT License",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BloodhavenStudios/QuartzEngine",
    packages=["Quartz"],
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Lincense :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Software Development :: Libaries :: Python Modules",
        "Topic :: Software Development :: Libaries",
        "Topic :: Utilities",
    ],
)