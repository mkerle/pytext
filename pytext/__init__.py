import re

from pytext.consoleColours import ConsoleColours

_consoleColours = ConsoleColours
_tagMapping = {}

def _setupTagMapping():
    for property, value in vars(_consoleColours).items():
        
        starttag = '<' + property + '>'
        endtag = '</' + property + '>'
        
        _tagMapping[starttag] = value
        _tagMapping[endtag] = _consoleColours.ENDC


_setupTagMapping()

def _getFormatTags(s):

    tags = []
    for line in s.split('\n'):

        foundTag = True
        while (foundTag):

            match = re.match(r'.*(<\/?.*>)', line)

            if (match is not None):
                tags.append(match.group(1))
                line = line.replace(match.group(1), '')

            else:
                foundTag = False

    return tags

def getConsoleText(s):

    for tag in _getFormatTags(s):

        if (tag in _tagMapping):
            s = s.replace(tag, _tagMapping[tag])

        else:
            raise Exception('Tag [%s] not found in pytext mapping!' % (tag))

    return s
