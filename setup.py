from setuptools import setup, find_packages

setup(
    name='wb',
    version='0.1.0',
    packages=find_packages(include=['wb', 'wb.*']),
    install_requires=[
        'nltk'
    ]
)