#!/usr/bin/env python

from setuptools import setup

setup(
    name='apns2',
    version='0.0.1',
    packages=['apns2'],
    install_requires=[
        'hyper>=0.7',
        'PyJWT>=1.4.0',
        'cryptography>=1.7.2',
    ],
    extras_require={
        "tests": [
            'freezegun',
            'pytest',
            'mock',
        ],
    },
    url='https://github.com/VinayGValsaraj/PyAPNs2',
    license='MIT',
    author='Vinay Valsaraj',
    author_email='vinaygvalsaraj@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
    description='A python library for interacting with the Apple Push Notification Service via HTTP/2 protocol'
)
