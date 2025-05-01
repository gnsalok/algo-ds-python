import re

def remove_non_ascii(s):
    return "".join(c for c in s if ord(c) < 128)


def remove_special_characters(s):
    return re.sub(r'[^a-zA-Z0-9\s]', '', s)


s = "Héllo Wørld! @2025 😊"
print(remove_non_ascii(s))
# print(remove_special_characters(s))