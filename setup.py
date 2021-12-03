from setuptools import setup, find_packages

setup(
    name='pysemble',
    version='0.0.4',
    license='MIT',
    zip_safe=False,
    packages=find_packages(include=['pysemble', 'pysemble.lists', "pysemble.logger"]),
)