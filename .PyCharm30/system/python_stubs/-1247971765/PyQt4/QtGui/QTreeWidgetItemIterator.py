# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTreeWidgetItemIterator(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QTreeWidgetItemIterator(QTreeWidgetItemIterator)
    QTreeWidgetItemIterator(QTreeWidget, QTreeWidgetItemIterator.IteratorFlags flags=QTreeWidgetItemIterator.All)
    QTreeWidgetItemIterator(QTreeWidgetItem, QTreeWidgetItemIterator.IteratorFlags flags=QTreeWidgetItemIterator.All)
    """
    def value(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItemIterator.value() -> QTreeWidgetItem """
        return QTreeWidgetItem

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    All = 0
    Checked = 4096
    Disabled = 32768
    DragDisabled = 128
    DragEnabled = 64
    DropDisabled = 512
    DropEnabled = 256
    Editable = 65536
    Enabled = 16384
    HasChildren = 1024
    Hidden = 1
    IteratorFlag = None # (!) real value is ''
    IteratorFlags = None # (!) real value is ''
    NoChildren = 2048
    NotChecked = 8192
    NotEditable = 131072
    NotHidden = 2
    NotSelectable = 32
    Selectable = 16
    Selected = 4
    Unselected = 8
    UserFlag = 16777216


