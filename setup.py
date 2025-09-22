"""Setup."""
import os

from setuptools import find_packages, setup


def read_requirements(filename):
    """Lê um arquivo de requirements e retorna uma lista de pacotes."""
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


REQUIRED_PACKAGES = read_requirements("requirements.txt")


DEV_PACKAGES = []
if os.path.exists("requirements.dev.txt"):
    DEV_PACKAGES = read_requirements("requirements.dev.txt")

README = ""
if os.path.exists("README.md"):
    README = open("README.md").read()

setup(
    name="pqc",
    version="0.0.1",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=REQUIRED_PACKAGES,
    extras_require={"dev": DEV_PACKAGES},
    packages=find_packages(include=["pqc", "pqc.*"]),
    platforms="any",
)
