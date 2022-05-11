import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()
requires = (HERE / 'requirements.txt').read_text().split('\n')

setup(
    name="CygnusX1",
    version="1.0.2",
    description="A multithreaded tool for searching and downloading images from popular search engines. It is straightforward to set up and run!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/datnnt1997/CygnusX1",
    author="DatNgo",
    author_email="datnnt97@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=('datasets', 'outputs')),
    include_package_data=True,
    install_requires=requires,
    entry_points="""
    [console_scripts] 
    cygnusx1=cygnusx1.main:run
    """
)