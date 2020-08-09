import setuptools

requires = [
    "flake8 > 3.0.0",
    "flake8-plugin-utils == 1.3.1",
]

flake8_entry_point = 'flake8.extension'

setuptools.setup(
    name="flake8_example",
    license="Apache",
    version="2.0",
    description="Python 3 super() check for flake8",
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
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)