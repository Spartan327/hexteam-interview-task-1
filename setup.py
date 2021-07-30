#!/usr/bin/env python3

import setuptools
from convertor import __version__

setuptools.setup(
    name='leet-tools',
    version=__version__,
    description='This is a test leet task',
    zip_safe=False,
    include_package_data=True,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            # TODO: need to implement this functionality [6]
        ]
    },
)
