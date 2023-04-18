import re


def validate_pin(pin):
    bool(re.fullmatch("\d{4}|\d{6}", pin))