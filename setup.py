"""Setup text preprocessing tools package."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["emot", "nltk"]

setuptools.setup(name="textools",
                 version="1.0.0",
                 author="mboivin",
                 author_email="mboivin@student.42.fr",
                 description="Text preprocessing tools.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/matboivin/textools",
                 install_requires=requirements,
                 packages=setuptools.find_packages(),
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "Operating System :: OS Independent",
                 ],
                 python_requires=">=3.9")
