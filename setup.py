from setuptools import setup

setup(
    name='lopy',
    version='0.0.6',
    packages=[ 'lopy' ],
    author='Joshua Smock',
    description="Local Python package manager",
    url='https://github.com/jo-sm/lopy',
    license='MIT',
    entry_points={
    	'console_scripts': [
    		'lopy=lopy.lopy:main'
    	]
    },
    install_requires=[
      'colorama',
    ],
)
