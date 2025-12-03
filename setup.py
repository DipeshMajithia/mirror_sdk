from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="mirrorsdk",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Dipesh Majithia",
    description="Python SDK for Mirror Chat API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.7",
)
