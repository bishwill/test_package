from setuptools import setup, find_packages

setup(
    name='example_package_wb',
    version='0.1.0',
    packages=find_packages(include=['example_package_wb', 'example_package_wb.*']),
    install_requires=[
        'nltk'
    ]
)