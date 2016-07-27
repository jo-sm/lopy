from distutils.core import setup

setup(
    name='lopy',
    version='0.0.1',
    packages=[' lopy' ],
    author='Joshua Smock',
    url='https://github.com/jo-sm/lopy'
    license='MIT',
    long_description=open('README.md').read(),
    entry_points={
    	'console_scripts': [
    		'lopy=lopy.lopy:main'
    	]
    },
)