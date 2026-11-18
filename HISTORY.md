# VERSION HISTORY

### VERSION 1.3.0 - 2026-11-17

**Added**

- Support/Testing for Django 5.2
- Support/Testing for Django 6.0
- Support/Testing for Django 6.1
- Support/Testing for Python 3.11-3.15 in accordance with each Django version's supported Python distribution

**Removed**

- Django 3 no longer supported as it has been deprecated by the Django Project
- Django 4 no longer supported as it has been deprecated by the Django Project
- Support/Testing for Python versions older than 3.11
  - Older versions of Python should still work, but are considered deprecated to be consistent with supported Python version of current Django versions

**Edited**

- Improved MaxConsecutiveCharactersValidator efficiency

**Bug Fix**

- N/A

### VERSION 1.2.0 - 2023-11-17

**Added**

- N/A

**Removed**

- Django 2.2 no longer supported as it has been deprecated by the Django Project

**Edited**

- N/A

**Bug Fix**

- Fixed improper use of alias "_" for plural messages with ngettext
- Changed gettext usage to lazy translations

### VERSION 1.1.0 - 2022-05-23

**Added**

- MaximumLengthValidator
- MaxConsecutiveCharactersValidator
- ConsecutivelyIncreasingDigitValidator
- ConsecutivelyDecreasingDigitValidator

**Removed**

- N/A

**Edited**

- Updated the Options list to show inputs and default values for the new methods.

**Bug Fix**

- package has been renamed from "django-advanced_password_validation" to "django_advanced_password_validation" to fix the *django.core.exceptions.improperlyconfigured: the app label 'django-advanced_password_validation' is not a valid python identifier* error

### VERSION 1.0.4 - 2020-03-25

**Added**

- N/A

**Removed**

- Unused import gettext has been removed.

**Edited**

- *ContainsNumeralsValidator* has been modified to *ContainsDigitsValidator* to be a more intuitive naming convention (i.e. 15 is one numeral, but two digits)
  - Option *min_numerals* has been changed to *min_digits*

**Bug Fix**

- ContainsSpecialValidator was only checking for one (1) special character instead of the minimum parameter.

### VERSION 1.0.3 - 2020-03-20

**Added**

- ContainsNumeralsValidator
- ContainsUppercaseValidator
- ContainsLowercaseValidator
- ContainsSpecialCharactersValidator
