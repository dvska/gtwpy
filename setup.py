#!/usr/bin/env python
from distutils.core import setup

VERSION='1.2.0'

setup(
    name='gtwpy',
    version=VERSION,
    description='Python GoToWebinar (GTW) REST API Wrapper',
    author='Michael Prior',
    author_email='prior@cracklabs.com',
    url='https://github.com/prior/pygtw',
    download_url='https://github.com/prior/gtwpy/tarball/v%s'%VERSION,
    packages=['gtw'],
    install_requires=[ 'nose==1.1.2' ]
)
