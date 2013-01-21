#!/usr/bin/env python
"""
Proofread
=========

Test your web app without writing tests!

Compatible with Django. Flask coming soon.

:copyright: (c) 2013 by Matt Robenolt
:license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages

tests_require = map(lambda x: x.strip(), open('requirements.txt').readlines())

setup(
    name='proofread',
    version='0.1.1',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/proofread',
    description='Test your web app without writing tests!',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    tests_require=tests_require,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
