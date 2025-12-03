from setuptools import setup, find_packages

setup(
    name="mirrorsdk",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Dipesh Majithia",
    description="Python SDK for Mirror Chat API",
    python_requires=">=3.7",
)
