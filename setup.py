# coding=utf-8
from setuptools import setup

setup(
    name="pefim_sp",
    version="0.1",
    description='SAML SP for the pefim profile.',
    author="Mathias Hedström",
    author_email="mathias.hedstrom@umu.se",
    license="Apache 2.0",
    packages=["pefim_sp"],
    package_dir={"": "src"},
    classifiers=["Development Status :: 0.1 - Beta",
                 "License :: OSI Approved :: Apache Software License",
                 "Topic :: Software Development :: Libraries :: Python Modules"],
    install_requires=["cherrypy==3.2.4"], #, "pysaml2"
    entry_points={
        'console_scripts': ['pefim_sp=pefim_sp.sp:main'],
    },

    zip_safe=False
)
