# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QUndoGroup(__PyQt4_QtCore.QObject):
    """ QUndoGroup(QObject parent=None) """
    def activeStack(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.activeStack() -> QUndoStack """
        return QUndoStack

    def activeStackChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.activeStackChanged[QUndoStack] [signal] """
        pass

    def addStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ QUndoGroup.addStack(QUndoStack) """
        pass

    def canRedo(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.canRedo() -> bool """
        return False

    def canRedoChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.canRedoChanged[bool] [signal] """
        pass

    def canUndo(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.canUndo() -> bool """
        return False

    def canUndoChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.canUndoChanged[bool] [signal] """
        pass

    def cleanChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.cleanChanged[bool] [signal] """
        pass

    def createRedoAction(self, QObject, str_prefix=''): # real signature unknown; restored from __doc__
        """ QUndoGroup.createRedoAction(QObject, str prefix='') -> QAction """
        return QAction

    def createUndoAction(self, QObject, str_prefix=''): # real signature unknown; restored from __doc__
        """ QUndoGroup.createUndoAction(QObject, str prefix='') -> QAction """
        return QAction

    def indexChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.indexChanged[int] [signal] """
        pass

    def isClean(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.isClean() -> bool """
        return False

    def redo(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.redo() """
        pass

    def redoText(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.redoText() -> str """
        return ""

    def redoTextChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.redoTextChanged[str] [signal] """
        pass

    def removeStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ QUndoGroup.removeStack(QUndoStack) """
        pass

    def setActiveStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ QUndoGroup.setActiveStack(QUndoStack) """
        pass

    def stacks(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.stacks() -> list-of-QUndoStack """
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.undo() """
        pass

    def undoText(self): # real signature unknown; restored from __doc__
        """ QUndoGroup.undoText() -> str """
        return ""

    def undoTextChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoGroup.undoTextChanged[str] [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


