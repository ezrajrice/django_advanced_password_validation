# django_advanced_password_validation

[![test](https://github.com/ezrajrice/django_advanced_password_validation/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/ezrajrice/django_advanced_password_validation/actions/workflows/test.yaml)
[![Coverage Status](https://coveralls.io/repos/github/ezrajrice/django_advanced_password_validation/badge.svg?branch=main)](https://coveralls.io/github/ezrajrice/django_advanced_password_validation?branch=main)

Extends Django password validation options to include minimum uppercase, minimum lowercase, minimum numerical, and minimum special characters. This was created in an attempt to keep up with industry standards for strong user passwords.

This package works for python 3.6+.

## Prerequisites

Requires Django 2.2 or later.
You can install the latest version of Django via pip:

```bash
pip install django
```

Alternatively, you can install a specific version of Django via pip:

```bash
pip install django=3.2
```

> **_NOTE:_**  See the [django-project](https://docs.djangoproject.com) documentation for information on non-deprecated Django versions.

## Installation

### Normal installation

Install django-advanced_password_validation via pip:

```bash
pip install django-advanced_password_validation
```

### Development installation

```bash
git clone https://github.com/ezrajrice/django-advanced_password_validation.git
cd django-advanced_password_validation
pip install --editable .
```

### Usage

The optional validators must be configured in the settings.py file of your django project to be actively used in your project.

#### /my-cool-project/settings.py

```python
INSTALLED_APPS = [
    ...
    'django_advanced_password_validation',
    ...
]

AUTH_PASSWORD_VALIDATORS = [
    ...
    {
        'NAME': 'django_advanced_password_validation.advanced_password_validation.ContainsDigitsValidator',
        'OPTIONS': {
            'min_digits': 1
        }
    },
    {
        'NAME': 'django_advanced_password_validation.advanced_password_validation.ContainsUppercaseValidator',
        'OPTIONS': {
            'min_uppercase': 1
        }
    },
    {
        'NAME': 'django_advanced_password_validation.advanced_password_validation.ContainsLowercaseValidator',
        'OPTIONS': {
            'min_lowercase': 1
        }
    },
    {
        'NAME': 'django_advanced_password_validation.advanced_password_validation.ContainsSpecialCharactersValidator',
        'OPTIONS': {
            'min_characters': 1
        }
    },
    ...
]
```

### Options

Here is a list of the available options with their default values.

| Validator | Option | Default |
| --- |:---:| ---:|
| ContainsDigitsValidator | min_digits | 1 |
| ContainsUppercaseValidator | min_uppercase | 1 |
| ContainsLowercaseValidator | min_lowercase | 1 |
| ContainsSpecialCharactersValidator | min_characters | 1 |
| MaximumLengthValidator | max_length | 128 |
| MaxConsecutiveCharactersValidator | max_consecutive | 3 |
| ConsecutivelyIncreasingDigitValidator | max_consecutive | 3 |
| ConsecutivelyDecreasingDigitValidator | max_consecutive | 3 |

## Authors

* **Ezra Rice** - _Initial work_ - [ezrajrice](https://github.com/ezrajrice)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* **Victor Semionov** - _Contributor_ - [vsemionov](https://github.com/vsemionov)
* **Mostafa Moradian** - _Contributor_ - [mostafa](https://github.com/mostafa)
