#!/usr/bin/python3
def to_uppercase(text):
    result = ""
    for char in text:
        code = ord(char)
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += char
    return result
print(to_uppercase("Best"))
print(to_uppercase("Best school 98 battery street"))
