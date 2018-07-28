#/usr/bin/env python3
from distutils.core import setup

setup(
	name='HTTPrint',
	version='0.1dev',
	packages=['httprint',],
	license='GPL',
	long_description='HTTPrint',
	scripts=['scripts/httprint',],
	include_package_data=True
)
