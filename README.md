# flake8-super
[![Downloads](https://pepy.tech/badge/flake8-super/month)](https://pepy.tech/project/flake8-super)
![PyPI](https://img.shields.io/pypi/v/flake8-super)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-super)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/flake8-super)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/flake8-super)

Python 3 super() check for flake8

# Installation

```bash
pip install flake8-super
```

# Configuration

No configuration required


# Example

```python3
#  Error
class SomeClass:
    def __init__(self):
        super(SomeClass, self).__init__()  # SPR100 Use `super()` instead of `super(__class__, self)`


# Good
class SomeClass:
    def __init__(self):
        super().__init__()

```


# Error codes

|code|description|
|---|---|
|SPR100|Use `super()` instead of `super(__class__, self)`|


# Links

https://github.com/meanmail/flake8-super

https://meanmail.dev/
