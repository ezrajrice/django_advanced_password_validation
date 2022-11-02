"""
Tests for the advanced_password_validation module.
"""

import pytest
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from ..advanced_password_validation import (
    ConsecutivelyDecreasingDigitValidator,
    ConsecutivelyIncreasingDigitValidator,
    ContainsDigitsValidator,
    ContainsLowercaseValidator,
    ContainsSpecialCharactersValidator,
    ContainsUppercaseValidator,
    MaxConsecutiveCharactersValidator,
    MaximumLengthValidator,
)


def test_contains_digits_validator():
    validator = ContainsDigitsValidator()
    # None means that the password is valid. Otherwise it returns a ValidationError.
    assert validator.validate("1234567890") is None
    with pytest.raises(ValidationError) as exc:
        validator.validate("abcdefghij")
    assert exc.value.code == "password_too_weak"
    assert exc.value.message == "Password must contain at least 1 number."


def test_contains_uppercase_validator():
    validator = ContainsUppercaseValidator()
    assert validator.validate("ABCDEFGHIJ") is None
    with pytest.raises(ValidationError) as exc:
        validator.validate("abcdefghij")
    assert exc.value.code == "password_too_weak"
    assert exc.value.message == "Password must contain at least 1 uppercase character."


def test_contains_lowercase_validator():
    validator = ContainsLowercaseValidator()
    assert validator.validate("abcdefghij") is None
    with pytest.raises(ValidationError) as exc:
        validator.validate("ABCDEFGHIJ")
    assert exc.value.code == "password_too_weak"
    assert exc.value.message == "Password must contain at least 1 lowercase character."


def test_contains_special_characters_validator():
    validator = ContainsSpecialCharactersValidator()
    assert validator.validate("!@#$%^&*()") is None
    with pytest.raises(ValidationError) as exc:
        validator.validate("abcdefghij")
    assert exc.value.code == "password_too_weak"
    assert exc.value.message == "Password must contain at least 1 special character."


def test_maximum_length_validator():
    validator = MaximumLengthValidator(max_length=10)
    assert validator.validate("abcdefghij") is None
    with pytest.raises(ValidationError) as exc:
        validator.validate("abcdefghijk")
    assert exc.value.message == "Password must contain at maximum 10 characters."


def test_max_consecutive_characters_validator():
    validator = MaxConsecutiveCharactersValidator()
    assert validator.validate("abcdefghij") is None
    with pytest.raises(ValidationError) as exc:
        validator.validate("aaabbbccc")
    assert (
        exc.value.message
        == "Password contains consecutively repeating characters. e.g 'aaa' or '111'"
    )


def test_consecutively_increasing_digit_validator():
    validator = ConsecutivelyIncreasingDigitValidator()
    assert validator.validate("abcdefghij") is None
    with pytest.raises(ValidationError) as exc:
        validator.validate("1234567890")
    assert (
        exc.value.message
        == "Password contains consecutively increasing digits. e.g '12345'"
    )


def test_consecutively_decreasing_digit_validator():
    validator = ConsecutivelyDecreasingDigitValidator()
    assert validator.validate("abcdefghij") is None
    with pytest.raises(ValidationError) as exc:
        validator.validate("9876543210")
    assert (
        exc.value.message
        == "Password contains consecutively decreasing digits. e.g '54321'"
    )


def test_valid_password():
    assert validate_password("Abc$d1234!") is None


def test_invalid_password():
    with pytest.raises(ValidationError) as exc:
        validate_password("")
    assert exc.value.messages == [
        "This password is too short. It must contain at least 10 characters.",
        "Password must contain at least 1 number.",
        "Password must contain at least 1 uppercase character.",
        "Password must contain at least 1 lowercase character.",
        "Password must contain at least 1 special character.",
    ]
