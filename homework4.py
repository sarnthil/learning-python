import re

'''12/15 points. 2.0'''

def match_email(string):
    '''Returns True if and only if the string seems to be a valid email
    address.

    Note: Doing this absolutely correctly to spec isn't the goal here. You
    should have the goal of matching 99% of the email addresses in the wild,
    and may refuse obscure things. So don't worry about RFCs etc.

    3/4 points
    +@+.oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    '''
    pattern = r'[a-z.0-9_+-]+@[a-z0-9.-]+\.[a-z]+'
    something = re.fullmatch(pattern, string, re.IGNORECASE)
    if something:
        return True
    else:
        return False
def match_link(string):
    '''Returns True if and only if the given string is a seemingly valid HTTP(S)
    link.

    Note: see note for match_email.

    1/3 points
    https://./////////
    '''
    pattern = r'https?://[a-z.0-9-]+[/a-z0-9#-]'
    something = re.fullmatch(pattern, string, re.IGNORECASE)
    if something:
        return True
    else:
        return False

def grep(filename, string):
    '''Returns all lines that match a given string. Interpret the string as a
    regular expression, so e.g. if the string is "foo[bp]ar" it should return
    all those lines that contain the words foobar and/or foopar.

    It shouldn't return the lines altogether in a list, but rather one by one
    using yield.

    5/5 points
    '''
    with open(filename) as f:
        for line in f:
            if re.find(string, line):
                yield line
def matching_one(regexes, string):
    '''Returns True if and only if one of the given regexes (a list) matches the
    string. For example, if regexes is ['abc','foo'] and the string is 'blabcar',
    it should return True, but not if regexes is ['lalala','foo'] and the string
    is 'blabcar'.

    3/3 points
    '''
    for item in regexes:
        if re.find(item, string):
            return True
    return False
    #also works, but the above is more beautiful:
    #return any(re.find(item,string) for item in regexes)
