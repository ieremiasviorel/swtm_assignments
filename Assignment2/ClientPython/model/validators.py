import regex
from PyInquirer import Validator, ValidationError


class EventNameValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[a-zA-Z0-9-_ ]+$', document.text)
        if not ok:
            raise ValidationError(message='Please enter a valid name (no special characters)',
                                  cursor_position=len(document.text))


class EventDateValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$', document.text)
        if not ok:
            raise ValidationError(message='Please enter a valid date (YYYY-MM-ZZ HH:MM:SS)',
                                  cursor_position=len(document.text))
