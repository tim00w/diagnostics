import os
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pytz>=2018", "numpy>=1.16.0", "matplotlib>=3.0.0"]

# upload to pypi:
#   python setup.py sdist bdist_wheel
#   python -m twine upload
setup(
    name="bonkie-diagnostics",
    version="0.2.0rc",
    author="Timo Lesterhuis",
    author_email="timolesterhuis@gmail.com",
    description="A toolbox to analyse diagnostic data!",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tim00w/diagnostics/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)
