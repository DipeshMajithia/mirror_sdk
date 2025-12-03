from setuptools import setup, find_packages

setup(
    name="mirror_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Dipesh Majithia",
    description="Python SDK for Mirror Chat API",
    python_requires=">=3.7",
)
