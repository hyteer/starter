# -*- coding: utf-8 -*-
"""
    YtEgg Tests
    ~~~~~~~~~~~~

    Tests the YtEgg application.

    :copyright: (c) 2017 by YT.
    :license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages

setup(
    name='ytegg',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
