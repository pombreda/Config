# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QFileIconProvider(): # skipped bases: <class 'sip.simplewrapper'>
    """ QFileIconProvider() """
    def icon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileIconProvider.icon(QFileIconProvider.IconType) -> QIcon
        QFileIconProvider.icon(QFileInfo) -> QIcon
        """
        return QIcon

    def type(self, QFileInfo): # real signature unknown; restored from __doc__
        """ QFileIconProvider.type(QFileInfo) -> str """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Computer = 0
    Desktop = 1
    Drive = 4
    File = 6
    Folder = 5
    IconType = None # (!) real value is ''
    Network = 3
    Trashcan = 2


