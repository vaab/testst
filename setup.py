#!/usr/bin/env python


from distutils.core import setup
setup(
    name='tests',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=['testst'],
    install_requires=['kids.cache', ],
    )


