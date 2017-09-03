import string

UNTRUSTED_PREFIXES = tuple(["/", "\\"] + [c + ":" for c in string.ascii_letters])

print(UNTRUSTED_PREFIXES)

# let's try to add something by autocommit...
# let's try commit using ssh key