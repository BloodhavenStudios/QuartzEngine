import re
from codecs import open
from os import path, environ

from setuptools import setup

PACKAGE_NAME = "Quartz"
HERE = path.abspath(path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()

try:
    VERSION = (
        environ["TRAVIS_TAG"].lstrip("v")
        if "TRAVIS" in environ and environ["TRAVIS"] == "true"
        else environ["VERSION_NUMBER"]
    )
except KeyError:
    with open(path.join(HERE, PACKAGE_NAME, "const.py"), encoding="utf-8") as fp:
        VERSION = re.search('version = "([^"]+)"', fp.read()).group(1)

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
    install_requires=requirements,
    license="MIT License",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BloodhavenStudios/QuartzEngine",
    packages=["quartzengine"],
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
