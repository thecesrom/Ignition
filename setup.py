#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md', 'r') as fin:
    readme = fin.read()

with open('requirements.txt', 'r') as fin:
    requirements = [e.strip() for e in fin.readlines()]

common_args = {
    'long_description': readme,
    'author': 'SD Team at Plenty Unlimited, Inc.',
    'author_email': 'software-data@plenty.ag',
    'url': 'https://github.com/PlentyAg/ignition_mock',
    'include_package_data': True,
    'install_requires': requirements,
    'zip_safe': False,
    'keywords': [],
    'classifiers': [],
    'test_suite': '',
    'tests_require': [],
    'setup_requires': [],
    'dependency_links': []
}

setup(
    name='system',
    version='0.1',
    description='The Igntition system mock library.',
    packages=['system'],
    **common_args)
setup(
    name='java',
    version='0.1',
    description='The Igntition java mock library.',
    packages=['java'],
    **common_args)
setup(
    name='javax',
    version='0.1',
    description='The Igntition javax mock library.',
    packages=['javax'],
    **common_args)
