# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QPalette(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QPalette()
    QPalette(QColor)
    QPalette(Qt.GlobalColor)
    QPalette(QColor, QColor)
    QPalette(QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush)
    QPalette(QColor, QColor, QColor, QColor, QColor, QColor, QColor)
    QPalette(QPalette)
    QPalette(object)
    """
    def alternateBase(self): # real signature unknown; restored from __doc__
        """ QPalette.alternateBase() -> QBrush """
        return QBrush

    def background(self): # real signature unknown; restored from __doc__
        """ QPalette.background() -> QBrush """
        return QBrush

    def base(self): # real signature unknown; restored from __doc__
        """ QPalette.base() -> QBrush """
        return QBrush

    def brightText(self): # real signature unknown; restored from __doc__
        """ QPalette.brightText() -> QBrush """
        return QBrush

    def brush(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPalette.brush(QPalette.ColorGroup, QPalette.ColorRole) -> QBrush
        QPalette.brush(QPalette.ColorRole) -> QBrush
        """
        return QBrush

    def button(self): # real signature unknown; restored from __doc__
        """ QPalette.button() -> QBrush """
        return QBrush

    def buttonText(self): # real signature unknown; restored from __doc__
        """ QPalette.buttonText() -> QBrush """
        return QBrush

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ QPalette.cacheKey() -> int """
        return 0

    def color(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPalette.color(QPalette.ColorGroup, QPalette.ColorRole) -> QColor
        QPalette.color(QPalette.ColorRole) -> QColor
        """
        return QColor

    def currentColorGroup(self): # real signature unknown; restored from __doc__
        """ QPalette.currentColorGroup() -> QPalette.ColorGroup """
        pass

    def dark(self): # real signature unknown; restored from __doc__
        """ QPalette.dark() -> QBrush """
        return QBrush

    def foreground(self): # real signature unknown; restored from __doc__
        """ QPalette.foreground() -> QBrush """
        return QBrush

    def highlight(self): # real signature unknown; restored from __doc__
        """ QPalette.highlight() -> QBrush """
        return QBrush

    def highlightedText(self): # real signature unknown; restored from __doc__
        """ QPalette.highlightedText() -> QBrush """
        return QBrush

    def isBrushSet(self, QPalette_ColorGroup, QPalette_ColorRole): # real signature unknown; restored from __doc__
        """ QPalette.isBrushSet(QPalette.ColorGroup, QPalette.ColorRole) -> bool """
        return False

    def isCopyOf(self, QPalette): # real signature unknown; restored from __doc__
        """ QPalette.isCopyOf(QPalette) -> bool """
        return False

    def isEqual(self, QPalette_ColorGroup, QPalette_ColorGroup_1): # real signature unknown; restored from __doc__
        """ QPalette.isEqual(QPalette.ColorGroup, QPalette.ColorGroup) -> bool """
        return False

    def light(self): # real signature unknown; restored from __doc__
        """ QPalette.light() -> QBrush """
        return QBrush

    def link(self): # real signature unknown; restored from __doc__
        """ QPalette.link() -> QBrush """
        return QBrush

    def linkVisited(self): # real signature unknown; restored from __doc__
        """ QPalette.linkVisited() -> QBrush """
        return QBrush

    def mid(self): # real signature unknown; restored from __doc__
        """ QPalette.mid() -> QBrush """
        return QBrush

    def midlight(self): # real signature unknown; restored from __doc__
        """ QPalette.midlight() -> QBrush """
        return QBrush

    def resolve(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPalette.resolve(QPalette) -> QPalette
        QPalette.resolve() -> int
        QPalette.resolve(int)
        """
        return QPalette or 0

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ QPalette.serialNumber() -> int """
        return 0

    def setBrush(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPalette.setBrush(QPalette.ColorGroup, QPalette.ColorRole, QBrush)
        QPalette.setBrush(QPalette.ColorRole, QBrush)
        """
        pass

    def setColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPalette.setColor(QPalette.ColorGroup, QPalette.ColorRole, QColor)
        QPalette.setColor(QPalette.ColorRole, QColor)
        """
        pass

    def setColorGroup(self, QPalette_ColorGroup, QBrush, QBrush_1, QBrush_2, QBrush_3, QBrush_4, QBrush_5, QBrush_6, QBrush_7, QBrush_8): # real signature unknown; restored from __doc__
        """ QPalette.setColorGroup(QPalette.ColorGroup, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush, QBrush) """
        pass

    def setCurrentColorGroup(self, QPalette_ColorGroup): # real signature unknown; restored from __doc__
        """ QPalette.setCurrentColorGroup(QPalette.ColorGroup) """
        pass

    def shadow(self): # real signature unknown; restored from __doc__
        """ QPalette.shadow() -> QBrush """
        return QBrush

    def text(self): # real signature unknown; restored from __doc__
        """ QPalette.text() -> QBrush """
        return QBrush

    def toolTipBase(self): # real signature unknown; restored from __doc__
        """ QPalette.toolTipBase() -> QBrush """
        return QBrush

    def toolTipText(self): # real signature unknown; restored from __doc__
        """ QPalette.toolTipText() -> QBrush """
        return QBrush

    def window(self): # real signature unknown; restored from __doc__
        """ QPalette.window() -> QBrush """
        return QBrush

    def windowText(self): # real signature unknown; restored from __doc__
        """ QPalette.windowText() -> QBrush """
        return QBrush

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


    Active = 0
    All = 5
    AlternateBase = 16
    Background = 10
    Base = 9
    BrightText = 7
    Button = 1
    ButtonText = 8
    ColorGroup = None # (!) real value is ''
    ColorRole = None # (!) real value is ''
    Current = 4
    Dark = 4
    Disabled = 1
    Foreground = 0
    Highlight = 12
    HighlightedText = 13
    Inactive = 2
    Light = 2
    Link = 14
    LinkVisited = 15
    Mid = 5
    Midlight = 3
    NColorGroups = 3
    NColorRoles = 20
    Normal = 0
    NoRole = 17
    Shadow = 11
    Text = 6
    ToolTipBase = 18
    ToolTipText = 19
    Window = 10
    WindowText = 0
    __hash__ = None


