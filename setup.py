#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  rextract
#
#
#  Created by TVA on 3/13/18.
#  Copyright (c) 2018 rextract. All rights reserved.
from __future__ import unicode_literals
import os
import sys
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rextract/VERSION')) as f:
    __version__ = f.read()

if __name__ == '__main__':
    dirName = os.path.dirname(__file__)
    if dirName and os.getcwd() != dirName:
        os.chdir(dirName)

    summary = 'Powerful commandline tool to extract and manipulate strings using regular exressions'

    try:
        with open('README.rst', 'rt') as f:
            long_description = f.read()
    except Exception as e:
        sys.stderr.write('Exception when reading long description: %s\n' %(str(e),))
        long_description = summary

    setup(name='rextract',
            version=__version__,
            scripts=['bin/rextract'],
            author='V.Anh Tran',
            author_email='tranvietanh1991@gmail.com',
            maintainer='V.Anh Tran',
            url='https://github.com/tranvietanh1991/rextract',
            packages=find_packages(exclude=['*.tests', '*.tests.*']),
            include_package_data=True,
            maintainer_email='tranvietanh1991@gmail.com',
            description=summary,
            long_description=long_description,
            license='GPLv3',
            keywords=['rextract', 'regex', 'extract', 're', 'sed', 'grep', 'format', 'reformat', 'text', 'manipulate', 'strings', 'input', 'output', 'io', 'cli', 'commandline'],
            classifiers=['Development Status :: 5 - Production/Stable',
                         'Environment :: Console',
                         'Topic :: Text Processing',
                         'Topic :: Text Processing :: General',
                         'Topic :: Text Processing :: Filters',
                         'Topic :: Utilities',
                         'Programming Language :: Python',
                         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                         'Programming Language :: Python :: 2',
                         'Programming Language :: Python :: 2',
                         'Programming Language :: Python :: 2.7',
                         'Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 3.4',
                         'Programming Language :: Python :: 3.5',
            ]
    )

