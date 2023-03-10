import unittest

import pytext



class testPyText(unittest.TestCase):

    def setUp(self):
        pass
    
    def testPyTextFormatting(self):

        txt = 'This is <BOLD>bold</BOLD>.  This is <FAIL>fail</FAIL>.  This is <BOLD><UNDERLINE><OKGREEN>bold & underline & green</OKGREEN></BOLD></UNDERLINE>'

        formatted = pytext.getConsoleText(txt)

        print(formatted)
        

    def testPyTextFormattingMultiline(self):

        txt = '\nThis is <BOLD>bold</BOLD>.  \nThis is <FAIL>fail</FAIL>.  \nThis is <BOLD><UNDERLINE><OKGREEN>bold & underline & green</OKGREEN></BOLD></UNDERLINE>'

        formatted = pytext.getConsoleText(txt)

        print(formatted)
        



        
