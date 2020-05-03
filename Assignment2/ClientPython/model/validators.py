import regex
from PyInquirer import Validator, ValidationError


class EventNameValidator(Validator):
    def validate(self, document):
        trimmed_text = document.text.strip()

        if len(trimmed_text) == 0 or len(trimmed_text) > 100:
            raise ValidationError(message='Please enter a valid name (at most 100 characters)',
                                  cursor_position=len(document.text))


class EventDescriptionValidator(Validator):
    def validate(self, document):
        trimmed_text = document.text.strip()

        if len(trimmed_text) == 0 or len(trimmed_text) > 500:
            raise ValidationError(message='Please enter a valid description (at most 500 characters)',
                                  cursor_position=len(document.text))


class EventDateValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$', document.text)
        if not ok:
            raise ValidationError(message='Please enter a valid date (YYYY-MM-ZZ HH:MM:SS)',
                                  cursor_position=len(document.text))
