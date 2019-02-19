"""
Copyright © 2016 Riccardo Cagnasso <riccardo@phascode.org>

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://www.wtfpl.net/ for more details.
"""

from setuptools import setup, find_packages

setup(
    name="nsmclient",
    version="0.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    author="CHANGE HERE",
    author_email="CHANGE HERE",
    license="LGPLv3",
    keywords="jack non-session-manager nsm",
    scripts=[
    ],
    install_requires=[]
)
