'''
Author: WildboarG
version: 1.0
Date: 2022-08-24 20:36:57
LastEditors: WildboarG
LastEditTime: 2022-08-24 22:31:28
Descripttion: 
'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from numpy.distutils.command.install import install
from setuptools import setup, find_packages
from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration
from os.path import join, dirname, realpath


setup(
    
    name='ncov_zit',
    version='0.0.2',
    author='WildboarG',
    author_email='mm62633482@gmail.com',
    url='https://github.com/WildboarG/ncov-zit',
    license="MIT",
    description='A cli tool  to obtain the health reporting and submission information of Zzhou Institute of science and technology.',
    long_description_content_type="text/markdown",
    long_description = "test  Module",
    install_requires=["requests","rich"],
    keywords=["zit", "ncov"],
    python_requires=">=3",

    package_data={
        '':['ncov_zit/info/*.py'],
               },

    exclude_package_data={
        'bandwidth_reporter':['*.txt']
               },
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "oh_my-zit = ncov_zit.main:main",
        ],
    }
)
