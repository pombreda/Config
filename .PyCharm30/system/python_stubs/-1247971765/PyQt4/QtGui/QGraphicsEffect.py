# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QGraphicsEffect(__PyQt4_QtCore.QObject):
    """ QGraphicsEffect(QObject parent=None) """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.boundingRect() -> QRectF """
        pass

    def boundingRectFor(self, QRectF): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.boundingRectFor(QRectF) -> QRectF """
        pass

    def draw(self, QPainter): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.draw(QPainter) """
        pass

    def drawSource(self, QPainter): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.drawSource(QPainter) """
        pass

    def enabledChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsEffect.enabledChanged[bool] [signal] """
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.isEnabled() -> bool """
        return False

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.setEnabled(bool) """
        pass

    def sourceBoundingRect(self, Qt_CoordinateSystem_system=None): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.sourceBoundingRect(Qt.CoordinateSystem system=Qt.LogicalCoordinates) -> QRectF """
        pass

    def sourceChanged(self, QGraphicsEffect_ChangeFlags): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.sourceChanged(QGraphicsEffect.ChangeFlags) """
        pass

    def sourceIsPixmap(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.sourceIsPixmap() -> bool """
        return False

    def sourcePixmap(self, Qt_CoordinateSystem_system=None, QGraphicsEffect_PixmapPadMode_mode=None): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.sourcePixmap(Qt.CoordinateSystem system=Qt.LogicalCoordinates, QGraphicsEffect.PixmapPadMode mode=QGraphicsEffect.PadToEffectiveBoundingRect) -> (QPixmap, QPoint) """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.update() """
        pass

    def updateBoundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsEffect.updateBoundingRect() """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    ChangeFlag = None # (!) real value is ''
    ChangeFlags = None # (!) real value is ''
    NoPad = 0
    PadToEffectiveBoundingRect = 2
    PadToTransparentBorder = 1
    PixmapPadMode = None # (!) real value is ''
    SourceAttached = 1
    SourceBoundingRectChanged = 4
    SourceDetached = 2
    SourceInvalidated = 8


