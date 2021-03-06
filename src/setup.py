import pathlib
from setuptools import setup
from setuptools import find_packages, setup

# The directory containing this file
# HERE = pathlib.Path(__file__).parent

# The text of the README file
# README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="myapp",
    version="1.0.1",
    description="Just greets you",
    # long_description=README,
    # long_description_content_type="text/markdown",
    # url="https://github.com/realpython/reader",
    author="Just Local User",
    author_email="abc@example.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    # include_package_data=True,
    # install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "myapp=StarterApp.__main__:main",
        ]
    },
)