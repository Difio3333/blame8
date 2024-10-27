from setuptools import setup

setup(
    name="blame8",
    version="0.0.1",
    description="A example Python package",
    url="https://github.com/shuds13/pyexample",
    author="Fridolin Kerner, Christoph Ratay",
    author_email="fridolin.kerner@gmx.de, christophratay@gmail.com",
    license="BSD 2-clause",
    packages=["blame8"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "blame8 = blame8.client:main",
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",       
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
