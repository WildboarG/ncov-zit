#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import setuptools

setuptools.setup(
    name='ncovzit',
    version='0.0.1',
    author='WildboarG',
    author_email='mm62633482@gmail.com',
    url='https://github.com/WildboarG/zit-Cov',
    license="MIT",
    description='A small function to obtain the health reporting and submission information of Zhengzhou Institute of science and technology.',
    long_description_content_type="text/markdown",
    long_description = "test Module",
    packages=["zitncov"],
    install_requires=["requests","fuckzk","argparse","rich"],
    keywords=["zit", "ncov"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "zitncov = zitncov.main:main",
        ],
    },
)
