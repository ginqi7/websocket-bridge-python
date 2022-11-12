#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='websocket_bridge_python',
    version='0.0.1',
    author='qiqi jin',
    author_email='ginqi7@gmail.com',
    url='https://github.com/ginqi7/websocket-bridge-python',
    description=u'websocket-bridge Used for communication between Emacs and python',
    packages=['websocket_bridge_python'],
    install_requires=['websockets']
)
