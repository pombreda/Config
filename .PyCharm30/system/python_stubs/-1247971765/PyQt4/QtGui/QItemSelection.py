# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QItemSelection(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QItemSelection()
    QItemSelection(QModelIndex, QModelIndex)
    QItemSelection(QItemSelection)
    """
    def append(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ QItemSelection.append(QItemSelectionRange) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QItemSelection.clear() """
        pass

    def contains(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QItemSelection.contains(QModelIndex) -> bool """
        return False

    def count(self, QItemSelectionRange=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QItemSelection.count(QItemSelectionRange) -> int
        QItemSelection.count() -> int
        """
        return 0

    def first(self): # real signature unknown; restored from __doc__
        """ QItemSelection.first() -> QItemSelectionRange """
        return QItemSelectionRange

    def indexes(self): # real signature unknown; restored from __doc__
        """ QItemSelection.indexes() -> list-of-QModelIndex """
        pass

    def indexOf(self, QItemSelectionRange, int_from=0): # real signature unknown; restored from __doc__
        """ QItemSelection.indexOf(QItemSelectionRange, int from=0) -> int """
        return 0

    def insert(self, p_int, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ QItemSelection.insert(int, QItemSelectionRange) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QItemSelection.isEmpty() -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ QItemSelection.last() -> QItemSelectionRange """
        return QItemSelectionRange

    def lastIndexOf(self, QItemSelectionRange, int_from=-1): # real signature unknown; restored from __doc__
        """ QItemSelection.lastIndexOf(QItemSelectionRange, int from=-1) -> int """
        return 0

    def merge(self, QItemSelection, QItemSelectionModel_SelectionFlags): # real signature unknown; restored from __doc__
        """ QItemSelection.merge(QItemSelection, QItemSelectionModel.SelectionFlags) """
        pass

    def move(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QItemSelection.move(int, int) """
        pass

    def prepend(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ QItemSelection.prepend(QItemSelectionRange) """
        pass

    def removeAll(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ QItemSelection.removeAll(QItemSelectionRange) -> int """
        return 0

    def removeAt(self, p_int): # real signature unknown; restored from __doc__
        """ QItemSelection.removeAt(int) """
        pass

    def replace(self, p_int, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ QItemSelection.replace(int, QItemSelectionRange) """
        pass

    def select(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ QItemSelection.select(QModelIndex, QModelIndex) """
        pass

    def split(self, QItemSelectionRange, QItemSelectionRange_1, QItemSelection): # real signature unknown; restored from __doc__
        """ QItemSelection.split(QItemSelectionRange, QItemSelectionRange, QItemSelection) """
        pass

    def swap(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QItemSelection.swap(int, int) """
        pass

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ QItemSelection.takeAt(int) -> QItemSelectionRange """
        return QItemSelectionRange

    def takeFirst(self): # real signature unknown; restored from __doc__
        """ QItemSelection.takeFirst() -> QItemSelectionRange """
        return QItemSelectionRange

    def takeLast(self): # real signature unknown; restored from __doc__
        """ QItemSelection.takeLast() -> QItemSelectionRange """
        return QItemSelectionRange

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


