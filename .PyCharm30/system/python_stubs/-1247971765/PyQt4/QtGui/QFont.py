# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QFont(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QFont()
    QFont(str, int pointSize=-1, int weight=-1, bool italic=False)
    QFont(QFont, QPaintDevice)
    QFont(QFont)
    QFont(object)
    """
    def bold(self): # real signature unknown; restored from __doc__
        """ QFont.bold() -> bool """
        return False

    def cacheStatistics(self): # real signature unknown; restored from __doc__
        """ QFont.cacheStatistics() """
        pass

    def capitalization(self): # real signature unknown; restored from __doc__
        """ QFont.capitalization() -> QFont.Capitalization """
        pass

    def cleanup(self): # real signature unknown; restored from __doc__
        """ QFont.cleanup() """
        pass

    def defaultFamily(self): # real signature unknown; restored from __doc__
        """ QFont.defaultFamily() -> str """
        return ""

    def exactMatch(self): # real signature unknown; restored from __doc__
        """ QFont.exactMatch() -> bool """
        return False

    def family(self): # real signature unknown; restored from __doc__
        """ QFont.family() -> str """
        return ""

    def fixedPitch(self): # real signature unknown; restored from __doc__
        """ QFont.fixedPitch() -> bool """
        return False

    def fromString(self, p_str): # real signature unknown; restored from __doc__
        """ QFont.fromString(str) -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ QFont.handle() -> int """
        return 0

    def hintingPreference(self): # real signature unknown; restored from __doc__
        """ QFont.hintingPreference() -> QFont.HintingPreference """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ QFont.initialize() """
        pass

    def insertSubstitution(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QFont.insertSubstitution(str, str) """
        pass

    def insertSubstitutions(self, p_str, list_of_str): # real signature unknown; restored from __doc__
        """ QFont.insertSubstitutions(str, list-of-str) """
        pass

    def isCopyOf(self, QFont): # real signature unknown; restored from __doc__
        """ QFont.isCopyOf(QFont) -> bool """
        return False

    def italic(self): # real signature unknown; restored from __doc__
        """ QFont.italic() -> bool """
        return False

    def kerning(self): # real signature unknown; restored from __doc__
        """ QFont.kerning() -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ QFont.key() -> str """
        return ""

    def lastResortFamily(self): # real signature unknown; restored from __doc__
        """ QFont.lastResortFamily() -> str """
        return ""

    def lastResortFont(self): # real signature unknown; restored from __doc__
        """ QFont.lastResortFont() -> str """
        return ""

    def letterSpacing(self): # real signature unknown; restored from __doc__
        """ QFont.letterSpacing() -> float """
        return 0.0

    def letterSpacingType(self): # real signature unknown; restored from __doc__
        """ QFont.letterSpacingType() -> QFont.SpacingType """
        pass

    def overline(self): # real signature unknown; restored from __doc__
        """ QFont.overline() -> bool """
        return False

    def pixelSize(self): # real signature unknown; restored from __doc__
        """ QFont.pixelSize() -> int """
        return 0

    def pointSize(self): # real signature unknown; restored from __doc__
        """ QFont.pointSize() -> int """
        return 0

    def pointSizeF(self): # real signature unknown; restored from __doc__
        """ QFont.pointSizeF() -> float """
        return 0.0

    def rawMode(self): # real signature unknown; restored from __doc__
        """ QFont.rawMode() -> bool """
        return False

    def rawName(self): # real signature unknown; restored from __doc__
        """ QFont.rawName() -> str """
        return ""

    def removeSubstitution(self, p_str): # real signature unknown; restored from __doc__
        """ QFont.removeSubstitution(str) """
        pass

    def resolve(self, QFont): # real signature unknown; restored from __doc__
        """ QFont.resolve(QFont) -> QFont """
        return QFont

    def setBold(self, bool): # real signature unknown; restored from __doc__
        """ QFont.setBold(bool) """
        pass

    def setCapitalization(self, QFont_Capitalization): # real signature unknown; restored from __doc__
        """ QFont.setCapitalization(QFont.Capitalization) """
        pass

    def setFamily(self, p_str): # real signature unknown; restored from __doc__
        """ QFont.setFamily(str) """
        pass

    def setFixedPitch(self, bool): # real signature unknown; restored from __doc__
        """ QFont.setFixedPitch(bool) """
        pass

    def setHintingPreference(self, QFont_HintingPreference): # real signature unknown; restored from __doc__
        """ QFont.setHintingPreference(QFont.HintingPreference) """
        pass

    def setItalic(self, bool): # real signature unknown; restored from __doc__
        """ QFont.setItalic(bool) """
        pass

    def setKerning(self, bool): # real signature unknown; restored from __doc__
        """ QFont.setKerning(bool) """
        pass

    def setLetterSpacing(self, QFont_SpacingType, p_float): # real signature unknown; restored from __doc__
        """ QFont.setLetterSpacing(QFont.SpacingType, float) """
        pass

    def setOverline(self, bool): # real signature unknown; restored from __doc__
        """ QFont.setOverline(bool) """
        pass

    def setPixelSize(self, p_int): # real signature unknown; restored from __doc__
        """ QFont.setPixelSize(int) """
        pass

    def setPointSize(self, p_int): # real signature unknown; restored from __doc__
        """ QFont.setPointSize(int) """
        pass

    def setPointSizeF(self, p_float): # real signature unknown; restored from __doc__
        """ QFont.setPointSizeF(float) """
        pass

    def setRawMode(self, bool): # real signature unknown; restored from __doc__
        """ QFont.setRawMode(bool) """
        pass

    def setRawName(self, p_str): # real signature unknown; restored from __doc__
        """ QFont.setRawName(str) """
        pass

    def setStretch(self, p_int): # real signature unknown; restored from __doc__
        """ QFont.setStretch(int) """
        pass

    def setStrikeOut(self, bool): # real signature unknown; restored from __doc__
        """ QFont.setStrikeOut(bool) """
        pass

    def setStyle(self, QFont_Style): # real signature unknown; restored from __doc__
        """ QFont.setStyle(QFont.Style) """
        pass

    def setStyleHint(self, QFont_StyleHint, QFont_StyleStrategy_strategy=None): # real signature unknown; restored from __doc__
        """ QFont.setStyleHint(QFont.StyleHint, QFont.StyleStrategy strategy=QFont.PreferDefault) """
        pass

    def setStyleName(self, p_str): # real signature unknown; restored from __doc__
        """ QFont.setStyleName(str) """
        pass

    def setStyleStrategy(self, QFont_StyleStrategy): # real signature unknown; restored from __doc__
        """ QFont.setStyleStrategy(QFont.StyleStrategy) """
        pass

    def setUnderline(self, bool): # real signature unknown; restored from __doc__
        """ QFont.setUnderline(bool) """
        pass

    def setWeight(self, p_int): # real signature unknown; restored from __doc__
        """ QFont.setWeight(int) """
        pass

    def setWordSpacing(self, p_float): # real signature unknown; restored from __doc__
        """ QFont.setWordSpacing(float) """
        pass

    def stretch(self): # real signature unknown; restored from __doc__
        """ QFont.stretch() -> int """
        return 0

    def strikeOut(self): # real signature unknown; restored from __doc__
        """ QFont.strikeOut() -> bool """
        return False

    def style(self): # real signature unknown; restored from __doc__
        """ QFont.style() -> QFont.Style """
        pass

    def styleHint(self): # real signature unknown; restored from __doc__
        """ QFont.styleHint() -> QFont.StyleHint """
        pass

    def styleName(self): # real signature unknown; restored from __doc__
        """ QFont.styleName() -> str """
        return ""

    def styleStrategy(self): # real signature unknown; restored from __doc__
        """ QFont.styleStrategy() -> QFont.StyleStrategy """
        pass

    def substitute(self, p_str): # real signature unknown; restored from __doc__
        """ QFont.substitute(str) -> str """
        return ""

    def substitutes(self, p_str): # real signature unknown; restored from __doc__
        """ QFont.substitutes(str) -> list-of-str """
        pass

    def substitutions(self): # real signature unknown; restored from __doc__
        """ QFont.substitutions() -> list-of-str """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ QFont.toString() -> str """
        return ""

    def underline(self): # real signature unknown; restored from __doc__
        """ QFont.underline() -> bool """
        return False

    def weight(self): # real signature unknown; restored from __doc__
        """ QFont.weight() -> int """
        return 0

    def wordSpacing(self): # real signature unknown; restored from __doc__
        """ QFont.wordSpacing() -> float """
        return 0.0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AbsoluteSpacing = 1
    AllLowercase = 2
    AllUppercase = 1
    AnyStyle = 5
    Black = 87
    Bold = 75
    Capitalization = None # (!) real value is ''
    Capitalize = 4
    Condensed = 75
    Courier = 2
    Cursive = 6
    Decorative = 3
    DemiBold = 63
    Expanded = 125
    ExtraCondensed = 62
    ExtraExpanded = 150
    Fantasy = 8
    ForceIntegerMetrics = 1024
    ForceOutline = 16
    Helvetica = 0
    HintingPreference = None # (!) real value is ''
    Light = 25
    MixedCase = 0
    Monospace = 7
    NoAntialias = 256
    NoFontMerging = 32768
    Normal = 50
    OldEnglish = 3
    OpenGLCompatible = 512
    PercentageSpacing = 0
    PreferAntialias = 128
    PreferBitmap = 2
    PreferDefault = 1
    PreferDefaultHinting = 0
    PreferDevice = 4
    PreferFullHinting = 3
    PreferMatch = 32
    PreferNoHinting = 1
    PreferOutline = 8
    PreferQuality = 64
    PreferVerticalHinting = 2
    SansSerif = 0
    SemiCondensed = 87
    SemiExpanded = 112
    Serif = 1
    SmallCaps = 3
    SpacingType = None # (!) real value is ''
    Stretch = None # (!) real value is ''
    Style = None # (!) real value is ''
    StyleHint = None # (!) real value is ''
    StyleItalic = 1
    StyleNormal = 0
    StyleOblique = 2
    StyleStrategy = None # (!) real value is ''
    System = 4
    Times = 1
    TypeWriter = 2
    UltraCondensed = 50
    UltraExpanded = 200
    Unstretched = 100
    Weight = None # (!) real value is ''
    __hash__ = None


