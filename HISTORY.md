# VERSION HISTORY

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