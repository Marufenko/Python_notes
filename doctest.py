def shorten(text, length=25, indicator="..."):
    """Function returns text or its truncated copy with indicator in the end

    text - any string;
    length - max length of return string (including indicator);
    indicator - string which is added in the end to reflect truncate

    >>> shorten("The Road")
    'The Road'
    >>> shorten("No Country for Old Men", 20)
    'No Country for Ol...'
    >>> shorten("Cities of the Plain", 15, "*")
    'Cities of the *'
    """

    if len(text) > length:
        text = text[:length - len(indicator)] + indicator
    return text

if __name__ == "__main__":
    import doctest
    doctest.testmod()