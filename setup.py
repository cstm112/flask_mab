"""
Flask-MAB
-------------

An implementation of the multi-armed bandit optimization pattern as a Flask extension
If you can pass it, we can test it
"""
from setuptools import setup

setup(
    name='Flask-MAB',
    version='2.0.10',
    url='https://github.com/cstm112/flask_mab.git',
    license='BSD',
    author='Mark Grey',
    author_email='mark.asperia@gmail.com',
    description='Multi-armed bandits for flask',
    long_description=__doc__,
    packages=['flask_mab'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=1.0.2',
        'flask-debugtoolbar==0.10.1',
        'future==0.17.1'
    ],
    setup_requires = [
        'future>=0.17.1',
        'coverage>=3.7.0',
        'mock>=1.0.0',
        'cryptography',
        'pytest-runner'
    ],
    tests_requires=[
        'pytest'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

