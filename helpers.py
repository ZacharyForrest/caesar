# input validation functions
# https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet
# - removes potentially hazardous characters
def sanitise_text_input(s):
    import re, html
    allowed_characters = "a-zA-Z0-9\_\,\s\.\-\!\?"
    s = re.sub(r'[^{}]+'.format(allowed_characters), '', s)
    return html.escape(s)
# - removes any non-numeric numbers and converts the string to an int
def sanitise_number_input(n):
    import re
    allowed_characters = "0-9"
    n = re.sub(r'[^{}]+'.format(allowed_characters), '', str(n))
    try:
        return int(n)
    except ValueError:
        return 0