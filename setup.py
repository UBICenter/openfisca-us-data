from setuptools import setup, find_packages

setup(
    name="openfisca-us-data",
    version="0.1.2",
    description=(
        "A Python package to manage OpenFisca-US-compatible microdata"
    ),
    url="http://github.com/PolicyEngine/openfisca-us-data",
    author="Nikhil Woodruff",
    author_email="nikhil.woodruff@outlook.com",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pathlib",
        "tqdm",
        "tables",
        "h5py",
        "synthimpute @ git+https://github.com/PSLmodels/synthimpute",
        "pytest",
        "pytest-dependency",
    ],
    entry_points={
        "console_scripts": ["openfisca-us-data=openfisca_us_data.cli:main"],
    },
)
