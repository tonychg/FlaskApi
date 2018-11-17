#!/usr/bin/env python3
# coding: utf-8
# =============================================================================
# Name     : setup.py
# Function :
# Usage    :
# Version  : 1.0.0
# vi       : set expandtab shiftwidth=4 softtabstop=4
# =============================================================================
# When        Who      What
# 11/17/18    tonychg
# =============================================================================

from setuptools import setup, find_packages

long_description = """Basic Template to distribute FlaskAPI"""

setup(
    name='FlaskAPI',
    version='1.0',
    description='Basic Template to distribute FlaskAPI',
    author='TonyChG',
    author_email='tonychg@dotfile.eu',
    url='https://github.com/TonyChG/flaskapi',
    packages=find_packages(),
    install_requires=[
        'certifi',
        'chardet',
        'click',
        'Flask',
        'idna',
        'itsdangerous',
        'Jinja2',
        'MarkupSafe',
        'requests',
        'urllib3',
        'Werkzeug',
    ],
    long_description=long_description,
    python_requires='>=3.4',
    classifiers=[
      "Development Status :: 5 - Production/Stable",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "License :: Other/Proprietary License",
      "Programming Language :: Python :: 3",
    ],
)
