# flake8-super
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
