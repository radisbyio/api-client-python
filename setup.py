from setuptools import setup, find_packages

setup(
    name='retailcrm',
    version='0.0.17',
    description='RetailCRM API client',
    url='https://github.com/retailcrm/api-client-python',
    author='Radis.by',
    license='MIT',
    packages=find_packages(exclude=("tests",)),
    package_data={},
    install_requires=[
        "httpx",
        "pydantic"
    ],
)
