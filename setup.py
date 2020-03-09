import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = 'WhatsPy',  
    version = '0.0.2',
    scripts = [
        'whatspy.sh'
    ],
    author = "Matheus Vanzan",
    author_email = "matheusvnzn@gmail.com",
    description = "Python Whatsapp API based on Selenium and ChromeDriver",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/matheusvanzan/whatspy",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)