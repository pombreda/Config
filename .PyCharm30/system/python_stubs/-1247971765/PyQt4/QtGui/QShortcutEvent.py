# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QShortcutEvent(__PyQt4_QtCore.QEvent):
    """
    QShortcutEvent(QKeySequence, int, bool ambiguous=False)
    QShortcutEvent(QShortcutEvent)
    """
    def isAmbiguous(self): # real signature unknown; restored from __doc__
        """ QShortcutEvent.isAmbiguous() -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ QShortcutEvent.key() -> QKeySequence """
        return QKeySequence

    def shortcutId(self): # real signature unknown; restored from __doc__
        """ QShortcutEvent.shortcutId() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


