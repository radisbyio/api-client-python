from setuptools import find_packages, setup

setup(
    name="radis-retailcrm-api",
    version="0.0.63",
    description="RetailCRM API client",
    url="https://github.com/retailcrm/api-client-python",
    author="Radis.by",
    packages=find_packages(exclude=("tests",)),
    package_data={},
    install_requires=["httpx", "pydantic"],
)
