import string

UNTRUSTED_PREFIXES = tuple(["/", "\\"] + [c + ":" for c in string.ascii_letters])

print(UNTRUSTED_PREFIXES)