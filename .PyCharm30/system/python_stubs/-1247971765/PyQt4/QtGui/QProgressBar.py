# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QWidget import QWidget

class QProgressBar(QWidget):
    """ QProgressBar(QWidget parent=None) """
    def alignment(self): # real signature unknown; restored from __doc__
        """ QProgressBar.alignment() -> Qt.Alignment """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QProgressBar.event(QEvent) -> bool """
        return False

    def format(self): # real signature unknown; restored from __doc__
        """ QProgressBar.format() -> str """
        return ""

    def initStyleOption(self, QStyleOptionProgressBar): # real signature unknown; restored from __doc__
        """ QProgressBar.initStyleOption(QStyleOptionProgressBar) """
        pass

    def invertedAppearance(self): # real signature unknown; restored from __doc__
        """ QProgressBar.invertedAppearance() -> bool """
        return False

    def isTextVisible(self): # real signature unknown; restored from __doc__
        """ QProgressBar.isTextVisible() -> bool """
        return False

    def maximum(self): # real signature unknown; restored from __doc__
        """ QProgressBar.maximum() -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ QProgressBar.minimum() -> int """
        return 0

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QProgressBar.minimumSizeHint() -> QSize """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ QProgressBar.orientation() -> Qt.Orientation """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QProgressBar.paintEvent(QPaintEvent) """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QProgressBar.reset() """
        pass

    def setAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QProgressBar.setAlignment(Qt.Alignment) """
        pass

    def setFormat(self, p_str): # real signature unknown; restored from __doc__
        """ QProgressBar.setFormat(str) """
        pass

    def setInvertedAppearance(self, bool): # real signature unknown; restored from __doc__
        """ QProgressBar.setInvertedAppearance(bool) """
        pass

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressBar.setMaximum(int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressBar.setMinimum(int) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QProgressBar.setOrientation(Qt.Orientation) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QProgressBar.setRange(int, int) """
        pass

    def setTextDirection(self, QProgressBar_Direction): # real signature unknown; restored from __doc__
        """ QProgressBar.setTextDirection(QProgressBar.Direction) """
        pass

    def setTextVisible(self, bool): # real signature unknown; restored from __doc__
        """ QProgressBar.setTextVisible(bool) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ QProgressBar.setValue(int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QProgressBar.sizeHint() -> QSize """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QProgressBar.text() -> str """
        return ""

    def textDirection(self): # real signature unknown; restored from __doc__
        """ QProgressBar.textDirection() -> QProgressBar.Direction """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ QProgressBar.value() -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """ QProgressBar.valueChanged[int] [signal] """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass

    BottomToTop = 1
    Direction = None # (!) real value is ''
    TopToBottom = 0

