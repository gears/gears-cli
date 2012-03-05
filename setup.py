import os
import sys
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


requirements = ['Gears']
if sys.version_info < (2, 7):
    requirements.append('argparse')


setup(
    name='gears-cli',
    version='0.1.dev',
    license='ISC',
    description='Command-line tools for Gears.',
    long_description=read('README.rst'),
    url='https://github.com/trilan/gears-cli',
    author='Mike Yumatov',
    author_email='mike@yumatov.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points = {
        'console_scripts': [
            'gears = gears_cli.__main__:run',
        ]
    }
)
