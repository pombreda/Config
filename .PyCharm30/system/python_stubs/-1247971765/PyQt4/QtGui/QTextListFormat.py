# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QTextFormat import QTextFormat

class QTextListFormat(QTextFormat):
    """
    QTextListFormat()
    QTextListFormat(QTextListFormat)
    """
    def indent(self): # real signature unknown; restored from __doc__
        """ QTextListFormat.indent() -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ QTextListFormat.isValid() -> bool """
        return False

    def numberPrefix(self): # real signature unknown; restored from __doc__
        """ QTextListFormat.numberPrefix() -> str """
        return ""

    def numberSuffix(self): # real signature unknown; restored from __doc__
        """ QTextListFormat.numberSuffix() -> str """
        return ""

    def setIndent(self, p_int): # real signature unknown; restored from __doc__
        """ QTextListFormat.setIndent(int) """
        pass

    def setNumberPrefix(self, p_str): # real signature unknown; restored from __doc__
        """ QTextListFormat.setNumberPrefix(str) """
        pass

    def setNumberSuffix(self, p_str): # real signature unknown; restored from __doc__
        """ QTextListFormat.setNumberSuffix(str) """
        pass

    def setStyle(self, QTextListFormat_Style): # real signature unknown; restored from __doc__
        """ QTextListFormat.setStyle(QTextListFormat.Style) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ QTextListFormat.style() -> QTextListFormat.Style """
        pass

    def __init__(self, QTextListFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ListCircle = -2
    ListDecimal = -4
    ListDisc = -1
    ListLowerAlpha = -5
    ListLowerRoman = -7
    ListSquare = -3
    ListUpperAlpha = -6
    ListUpperRoman = -8
    Style = None # (!) real value is ''


