from pathlib import Path

import setuptools

requires = [
    "flake8 > 3.0.0",
    "flake8-plugin-utils == 1.3.1",
]

flake8_entry_point = 'flake8.extension'

this_directory = Path(__file__).parent.resolve()
long_description = (this_directory / 'README.md').read_text()

setuptools.setup(
    name="flake8_super",
    license="MIT",
    version="0.1.2",
    description="Python 3 super() check for flake8",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="meanmail",
    author_email="example@example.com",
    url="https://github.com/meanmail/flake8-super",
    packages=[
        "flake8_super",
    ],
    install_requires=requires,
    entry_points={
        flake8_entry_point: [
            'SPR = flake8_super:SuperPlugin',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
