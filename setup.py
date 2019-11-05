#!/usr/bin/env python
# coding: utf-8

from setuptools import find_packages, setup

import awesome

install_requires = ["wheel"]

extras_require = {
    "np": ["numpy"]
}


def install():
    setup(
        name="awesome",
        version=awesome.__version__,
        description="awesome package",
        author="Some awesome team",
        packages=find_packages(where=".", exclude=["ghost"]),
        install_requires=install_requires,
        extras_require=extras_require,
        package_data={"awesome": ["data/data.txt"]},
        entry_points={
            "console_scripts": ["awesome = awesome.__main__:main"]
        },
    )


install()
