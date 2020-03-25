# django-advanced_password_validation

Extends Django password validation options to include minimum uppercase, minimum lowercase, minimum numerical, and minimum special characters. This was created in an attempt to keep up with industry standards for strong user passwords.

This package works for both python 3.x and 2.x versions.

> **_NOTE:_** As of January 01, 2020 python 2.x has been deprecated and will no longer receive continued support. See [Python 2.x EOL](https://www.python.org/doc/sunset-python-2/) for more details.

### Prerequisites

Requires Django 1.11 or later.
You can install the latest version of Django via pip:

```
$ pip install django
```

Alternatively, you can install a specific version of Django via pip:

```
$ pip install django=2.2
```

> **_NOTE:_**  See the [django-project](https://docs.djangoproject.com) documentation for information on non-deprecated Django versions.

### Installation

#### Normal installation

Install django-advanced_password_validation via pip:

```
$ pip install django-advanced_password_validation
```

#### Development installation

```
$ git clone https://github.com/ezrajrice/django-advanced_password_validation.git
$ cd django-advanced_password_validation
$ pip install --editable .
```

### Usage

The four optional validators must be configured in the settings.py file of your django project.

#### /my-cool-project/settings.py

```python
INSTALLED_APPS = [
    ...
    'django-advanced_password_validation',
    ...
]

AUTH_PASSWORD_VALIDATORS = [
    ...
    {
        'NAME': 'django-advanced_password_validation.advanced_password_validation.ContainsDigitsValidator',
        'OPTIONS': {
            'min_digits': 1
        }
    },
    {
        'NAME': 'django-advanced_password_validation.advanced_password_validation.ContainsUppercaseValidator',
        'OPTIONS': {
            'min_uppercase': 1
        }
    },
    {
        'NAME': 'django-advanced_password_validation.advanced_password_validation.ContainsLowercaseValidator',
        'OPTIONS': {
            'min_lowercase': 1
        }
    },
    {
        'NAME': 'django-advanced_password_validation.advanced_password_validation.ContainsSpecialCharactersValidator',
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

## Authors

* **Ezra Rice** - *Initial work* - [ezrajrice](https://github.com/ezrajrice)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* **Victor Semionov** - *Contributor* - [vsemionov](https://github.com/vsemionov)
