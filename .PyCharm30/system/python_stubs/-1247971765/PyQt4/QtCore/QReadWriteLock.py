# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QReadWriteLock(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QReadWriteLock()
    QReadWriteLock(QReadWriteLock.RecursionMode)
    """
    def lockForRead(self): # real signature unknown; restored from __doc__
        """ QReadWriteLock.lockForRead() """
        pass

    def lockForWrite(self): # real signature unknown; restored from __doc__
        """ QReadWriteLock.lockForWrite() """
        pass

    def tryLockForRead(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QReadWriteLock.tryLockForRead() -> bool
        QReadWriteLock.tryLockForRead(int) -> bool
        """
        return False

    def tryLockForWrite(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QReadWriteLock.tryLockForWrite() -> bool
        QReadWriteLock.tryLockForWrite(int) -> bool
        """
        return False

    def unlock(self): # real signature unknown; restored from __doc__
        """ QReadWriteLock.unlock() """
        pass

    def __init__(self, QReadWriteLock_RecursionMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NonRecursive = 0
    RecursionMode = None # (!) real value is ''
    Recursive = 1


