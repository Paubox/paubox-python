import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paubox-python",
    version="1.0.0",
    author="Paubox",
    author_email="info@paubox.com",
    description="Python SDK for Paubox Email REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Paubox/paubox-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=[
        'requests >= 2, < 3',
        'six >= 1, < 2',
    ],
)