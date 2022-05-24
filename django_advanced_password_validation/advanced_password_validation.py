from django.core.exceptions import ValidationError
from django.utils.translation import ngettext as _


class ContainsDigitsValidator:
    def __init__(self, min_digits=1):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if sum(c.isdigit() for c in password) < self.min_digits:
            raise ValidationError(
                _("Password must contain at least %(min_digits)d number.",
                         "Password must contain at least %(min_digits)d numbers.",
                         self.min_digits),
                code='password_too_weak',
                params={'min_digits': self.min_digits},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_digits)d number.",
            "Your password must contain at least %(min_digits)d numbers.",
            self.min_digits
        ) % {'min_digits': self.min_digits}


class ContainsUppercaseValidator:
    def __init__(self, min_uppercase=1):
        self.min_uppercase = min_uppercase

    def validate(self, password, user=None):
        if sum(c.isupper() for c in password) < self.min_uppercase:
            raise ValidationError(
                _("Password must contain at least %(min_uppercase)d uppercase character.",
                         "Password must contain at least %(min_uppercase)d uppercase characters.",
                         self.min_uppercase),
                code='password_too_weak',
                params={'min_uppercase': self.min_uppercase},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_uppercase)d uppercase character.",
            "Your password must contain at least %(min_uppercase)d uppercase characters.",
            self.min_uppercase
        ) % {'min_uppercase': self.min_uppercase}


class ContainsLowercaseValidator:
    def __init__(self, min_lowercase=1):
        self.min_lowercase = min_lowercase

    def validate(self, password, user=None):
        if sum(c.islower() for c in password) < self.min_lowercase:
            raise ValidationError(
                _("Password must contain at least %(min_lowercase)d lowercase character.",
                         "Password must contain at least %(min_lowercase)d lowercase characters.",
                         self.min_lowercase),
                code='password_too_weak',
                params={'min_lowercase': self.min_lowercase},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_lowercase)d lowercase character.",
            "Your password must contain at least %(min_lowercase)d lowercase characters.",
            self.min_lowercase
        ) % {'min_lowercase': self.min_lowercase}


class ContainsSpecialCharactersValidator:
    def __init__(self, min_characters=1):
        self.min_characters = min_characters
        self.characters = set(" !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    def validate(self, password, user=None):
        if sum(c in self.characters for c in password) < self.min_characters:
            raise ValidationError(
                _("Password must contain at least %(min_characters)d special character.",
                         "Password must contain at least %(min_characters)d special characters.",
                         self.min_characters),
                code='password_too_weak',
                params={'min_characters': self.min_characters},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_characters)d special character.",
            "Your password must contain at least %(min_characters)d special characters.",
            self.min_characters
        ) % {'min_characters': self.min_characters}


class MaximumLengthValidator:
    """
    OWASP recommends setting a maximum password length, typically 128 characters, to prevent
    'long password Denial of Service attacks'.
    """
    def __init__(self, max_length=128):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _(
                    "Password must contain at maximum %(max_length)d character.",
                    "Password must contain at maximum %(max_length)d characters.",
                    self.max_length
                ) % {'max_length': self.max_length}
            )

    def get_help_text(self):
        return _(
            "Password must contain at maximum %(max_length)d character.",
            "Password must contain at maximum %(max_length)d characters.",
            self.max_length
        ) % {'max_length': self.max_length}


class MaxConsecutiveCharactersValidator:
    def __init__(self, max_consecutive=3):
        self.max_consecutive = max_consecutive

    def validate(self, password, user=None):
        for c in password:
            if password.count(c) >= self.max_consecutive:
                check = c * self.max_consecutive
                if check in password:
                    raise ValidationError(
                        _("Password contains consecutively repeating characters. e.g 'aaa' or '111'")
                    )

    def get_help_text(self):
        return _("Password cannot contain consecutively repeating characters. e.g 'aaa' or '111'")


class ConsecutivelyIncreasingDigitValidator:
    def __init__(self, max_consecutive=3):
        self.max_consecutive = max_consecutive

    def validate(self, password, user=None):
        for c in password:
            if c.isdigit():
                count = 0
                digit = int(c)
                index = password.index(c)

                try:
                    for i in range(1, self.max_consecutive+1):
                        if password[index+i].isdigit():
                            if int(password[index+i]) == digit + 1:
                                count += 1
                                digit += 1

                                while count >= self.max_consecutive:
                                    raise ValidationError(
                                        _("Password contains consecutively increasing digits. e.g '12345'")
                                    )
                except IndexError:
                    pass

    def get_help_text(self):
        return _("Password cannot contain consecutively increasing digits. e.g '12345'")


class ConsecutivelyDecreasingDigitValidator:
    def __init__(self, max_consecutive=3):
        self.max_consecutive = max_consecutive

    def validate(self, password, user=None):
        for c in password:
            if c.isdigit():
                count = 0
                digit = int(c)
                index = password.index(c)

                try:
                    for i in range(1, self.max_consecutive+1):
                        if password[index+i].isdigit():
                            if int(password[index+i]) == digit - 1:
                                count += 1
                                digit -= 1

                                while count >= self.max_consecutive:
                                    raise ValidationError(
                                        _("Password contains consecutively decreasing digits. e.g '54321'")
                                    )
                except IndexError:
                    pass

    def get_help_text(self):
        return _("Password cannot contain consecutively decreasing digits. e.g '54321'")
