import re


def removeComments(string):
    string = re.sub(
        re.compile("/\*.*?\*/", re.DOTALL), "", string
    )  # remove all occurance streamed comments (/*COMMENT */) from string
    string = re.sub(
        re.compile("//.*?\n"), "", string
    )  # remove all occurance singleline comments (//COMMENT\n ) from string
    return string
