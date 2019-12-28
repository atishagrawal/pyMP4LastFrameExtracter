# -*- coding: utf-8 -*-
# @Author: Atish Agrawal
# @Date:   2019-12-28 13:15:09
# @Last Modified by:   Atish Agrawal
# @Last Modified time: 2019-12-28 13:16:16
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyMP4LastFrameExtracter-atishagrawal", # Replace with your own username
    version="0.0.1",
    author="Atish Agrawal",
    author_email="dir.atishagrawal@gmail.com",
    description="Code that extracts last frames of all the MP4 files found in the selected directory",
    long_description="Code that extracts last frames of all the MP4 files found in the selected directory",
    long_description_content_type="text/markdown",
    url="https://github.com/atishagrawal/pyMP4LastFrameExtracter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)