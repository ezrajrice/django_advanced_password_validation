from django.core.exceptions import ValidationError
from django.utils.translation import ngettext


class ContainsDigitsValidator:
    def __init__(self, min_digits=1):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if sum(c.isdigit() for c in password) < self.min_digits:
            raise ValidationError(
                ngettext("Password must contain at least %(min_digits)d number.",
                         "Password must contain at least %(min_digits)d numbers.",
                         self.min_digits),
                code='password_too_weak',
                params={'min_digits': self.min_digits},
            )

    def get_help_text(self):
        return ngettext(
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
                ngettext("Password must contain at least %(min_uppercase)d uppercase character.",
                         "Password must contain at least %(min_uppercase)d uppercase characters.",
                         self.min_uppercase),
                code='password_too_weak',
                params={'min_uppercase': self.min_uppercase},
            )

    def get_help_text(self):
        return ngettext(
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
                ngettext("Password must contain at least %(min_lowercase)d lowercase character.",
                         "Password must contain at least %(min_lowercase)d lowercase characters.",
                         self.min_lowercase),
                code='password_too_weak',
                params={'min_lowercase': self.min_lowercase},
            )

    def get_help_text(self):
        return ngettext(
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
                ngettext("Password must contain at least %(min_characters)d special character.",
                         "Password must contain at least %(min_characters)d special characters.",
                         self.min_characters),
                code='password_too_weak',
                params={'min_characters': self.min_characters},
            )

    def get_help_text(self):
        return ngettext(
            "Your password must contain at least %(min_characters)d special character.",
            "Your password must contain at least %(min_characters)d special characters.",
            self.min_characters
        ) % {'min_characters': self.min_characters}