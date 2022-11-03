"""
Advanced password validation
"""

from django.core.exceptions import ValidationError
from django.utils.translation import ngettext as _
from django.utils.translation import gettext


class ContainsDigitsValidator:
    """
    Validates whether the password contains at least min_digits digits.
    """

    def __init__(self, min_digits=1):
        """Initializes the validator.

        Args:
            min_digits (int, optional): Minimum number of digits to validate password
                against. Defaults to 1.
        """
        self.min_digits = min_digits

    def validate(self, password, user=None):
        """
        Validates whether the password contains at least min_digits digits.

        Args:
            password (str): The password to validate.
            user (User): The user to validate the password for. (unused)

        Raises:
            ValidationError: Password must contain at least {self.min_digits} number(s).
        """
        if sum(c.isdigit() for c in password) < self.min_digits:
            raise ValidationError(
                _(
                    f"Password must contain at least {self.min_digits} number.",
                    f"Password must contain at least {self.min_digits} numbers.",
                    self.min_digits,
                ),
                code="password_too_weak",
                params={"min_digits": self.min_digits},
            )

    def get_help_text(self):
        """
        Get the help text for the validator.
        """
        return (
            _(
                f"Your password must contain at least {self.min_digits} number.",
                f"Your password must contain at least {self.min_digits} numbers.",
                self.min_digits,
            )
            % {"min_digits": self.min_digits}
        )


class ContainsUppercaseValidator:
    """
    Validates whether the password contains at least min_uppercase uppercase characters.
    """

    def __init__(self, min_uppercase=1):
        """Initializes the validator.

        Args:
            min_uppercase (int, optional): Minimum number of uppercase characters to
                validate password against. Defaults to 1.
        """
        self.min_uppercase = min_uppercase

    def validate(self, password, user=None):
        """
        Validates whether the password contains at least min_uppercase uppercase characters.

        Args:
            password (str): The password to validate.
            user (User): The user to validate the password for. (unused)

        Raises:
            ValidationError: Password must contain at least {self.min_uppercase} uppercase
                character(s).
        """
        if sum(c.isupper() for c in password) < self.min_uppercase:
            raise ValidationError(
                _(
                    f"Password must contain at least {self.min_uppercase} uppercase character.",
                    f"Password must contain at least {self.min_uppercase} uppercase characters.",
                    self.min_uppercase,
                ),
                code="password_too_weak",
                params={"min_uppercase": self.min_uppercase},
            )

    def get_help_text(self):
        """
        Get the help text for the validator.
        """
        return (
            _(
                f"Your password must contain at least {self.min_uppercase} uppercase character.",
                f"Your password must contain at least {self.min_uppercase} uppercase characters.",
                self.min_uppercase,
            )
            % {"min_uppercase": self.min_uppercase}
        )


class ContainsLowercaseValidator:
    """
    Validates whether the password contains at least min_lowercase lowercase characters.
    """

    def __init__(self, min_lowercase=1):
        """Initializes the validator.

        Args:
            min_lowercase (int, optional): Minimum number of lowercase characters to
                validate password against. Defaults to 1.
        """
        self.min_lowercase = min_lowercase

    def validate(self, password, user=None):
        """
        Validates whether the password contains at least min_lowercase lowercase characters.

        Args:
            password (str): The password to validate.
            user (User): The user to validate the password for. (unused)

        Raises:
            ValidationError: Password must contain at least {self.min_lowercase} lowercase
                character(s).
        """
        if sum(c.islower() for c in password) < self.min_lowercase:
            raise ValidationError(
                _(
                    f"Password must contain at least {self.min_lowercase} lowercase character.",
                    f"Password must contain at least {self.min_lowercase} lowercase characters.",
                    self.min_lowercase,
                ),
                code="password_too_weak",
                params={"min_lowercase": self.min_lowercase},
            )

    def get_help_text(self):
        """
        Get the help text for the validator.
        """
        return (
            _(
                f"Your password must contain at least {self.min_lowercase} lowercase character.",
                f"Your password must contain at least {self.min_lowercase} lowercase characters.",
                self.min_lowercase,
            )
            % {"min_lowercase": self.min_lowercase}
        )


class ContainsSpecialCharactersValidator:
    """
    Validates whether the password contains at least min_characters special characters.
    """

    def __init__(self, min_characters=1):
        """Initializes the validator.

        Args:
            min_characters (int, optional): Minimum number of special characters to
                validate password against. Defaults to 1.
        """
        self.min_characters = min_characters
        self.characters = set(" !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    def validate(self, password, user=None):
        """
        Validates whether the password contains at least min_characters special characters.

        Args:
            password (str): The password to validate.
            user (User): The user to validate the password for. (unused)

        Raises:
            ValidationError: Password must contain at least {self.min_characters} special
                character(s).
        """
        if sum(c in self.characters for c in password) < self.min_characters:
            raise ValidationError(
                _(
                    f"Password must contain at least {self.min_characters} special character.",
                    f"Password must contain at least {self.min_characters} special characters.",
                    self.min_characters,
                ),
                code="password_too_weak",
                params={"min_characters": self.min_characters},
            )

    def get_help_text(self):
        """
        Get the help text for the validator.
        """
        return (
            _(
                f"Your password must contain at least {self.min_characters} special character.",
                f"Your password must contain at least {self.min_characters} special characters.",
                self.min_characters,
            )
            % {"min_characters": self.min_characters}
        )


class MaximumLengthValidator:
    """
    OWASP recommends setting a maximum password length, typically 128 characters, to prevent
    'long password Denial of Service attacks'.
    """

    def __init__(self, max_length=128):
        """Initializes the validator.

        Args:
            max_length (int, optional): Maximum length of the password. Defaults to 128.
        """
        self.max_length = max_length

    def validate(self, password, user=None):
        """
        Validates whether the password contains at least min_characters special characters.

        Args:
            password (str): The password to validate.
            user (User): The user to validate the password for. (unused)

        Raises:
            ValidationError: Password must contain at least {self.min_characters} special
                character(s).
        """
        if len(password) > self.max_length:
            raise ValidationError(
                _(
                    f"Password must contain at maximum {self.max_length} character.",
                    f"Password must contain at maximum {self.max_length} characters.",
                    self.max_length,
                )
                % {"max_length": self.max_length}
            )

    def get_help_text(self):
        """
        Get the help text for the validator.
        """
        return (
            _(
                f"Password must contain at maximum {self.max_length} character.",
                f"Password must contain at maximum {self.max_length} characters.",
                self.max_length,
            )
            % {"max_length": self.max_length}
        )


class MaxConsecutiveCharactersValidator:
    """
    Validates whether the password contains more than max_consecutive consecutive characters.
    """

    def __init__(self, max_consecutive=3):
        """Initializes the validator.

        Args:
            max_consecutive (int, optional): Maximum number of consecutive characters to
                validate password against. Defaults to 3.
        """
        self.max_consecutive = max_consecutive

    def validate(self, password, user=None):
        """
        Validates whether the password contains more than max_consecutive consecutive characters.

        Args:
            password (str): The password to validate.
            user (User): The user to validate the password for. (unused)

        Raises:
            ValidationError: Password cannot contain consecutively repeating
                characters. e.g 'aaa' or '111'
        """
        for c in password:
            if password.count(c) >= self.max_consecutive:
                check = c * (self.max_consecutive + 1)
                if check in password:
                    raise ValidationError(
                        gettext(
                            "Password contains consecutively repeating characters. "
                            "e.g 'aaa' or '111'"
                        )
                    )

    def get_help_text(self):
        """
        Get the help text for the validator.
        """
        return gettext(
            "Password cannot contain consecutively repeating characters. e.g 'aaa' or '111'"
        )


class ConsecutivelyIncreasingDigitValidator:
    """
    Validates whether the password contains consecutively increasing digits.
    """

    def __init__(self, max_consecutive=3):
        """Initializes the validator.

        Args:
            max_consecutive (int, optional): Maximum number of consecutive digits to
                validate password against. Defaults to 3.
        """
        self.max_consecutive = max_consecutive

    def validate(self, password, user=None):
        """
        Validates whether the password contains consecutively increasing digits.

        Args:
            password (str): The password to validate.
            user (User): The user to validate the password for. (unused)

        Raises:
            ValidationError: Password contains consecutively increasing digits. e.g '12345'
        """
        for c in password:
            if c.isdigit():
                count = 0
                digit = int(c)
                index = password.index(c)

                try:
                    for i in range(1, self.max_consecutive + 1):
                        if password[index + i].isdigit():
                            if int(password[index + i]) == digit + 1:
                                count += 1
                                digit += 1

                                while count >= self.max_consecutive:
                                    raise ValidationError(
                                        gettext(
                                            "Password contains consecutively increasing digits. "
                                            "e.g '12345'"
                                        )
                                    )
                except IndexError:
                    pass

    def get_help_text(self):
        """
        Get the help text for the validator.
        """
        return gettext(
            "Password cannot contain consecutively increasing digits. e.g '12345'"
        )


class ConsecutivelyDecreasingDigitValidator:
    """
    Validates whether the password contains consecutively decreasing digits.
    """

    def __init__(self, max_consecutive=3):
        """Initializes the validator.

        Args:
            max_consecutive (int, optional): Maximum number of consecutive digits to
                validate password against. Defaults to 3.
        """
        self.max_consecutive = max_consecutive

    def validate(self, password, user=None):
        """
        Validates whether the password contains consecutively decreasing digits.

        Args:
            password (str): The password to validate.
            user (User): The user to validate the password for. (unused)

        Raises:
            ValidationError: Password contains consecutively decreasing digits. e.g '54321'
        """
        for c in password:
            if c.isdigit():
                count = 0
                digit = int(c)
                index = password.index(c)

                try:
                    for i in range(1, self.max_consecutive + 1):
                        if password[index + i].isdigit():
                            if int(password[index + i]) == digit - 1:
                                count += 1
                                digit -= 1

                                while count >= self.max_consecutive:
                                    raise ValidationError(
                                        gettext(
                                            "Password contains consecutively decreasing digits. "
                                            "e.g '54321'"
                                        )
                                    )
                except IndexError:
                    pass

    def get_help_text(self):
        """
        Get the help text for the validator.
        """
        return gettext(
            "Password cannot contain consecutively decreasing digits. e.g '54321'"
        )
