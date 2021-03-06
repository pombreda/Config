# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QGesture import QGesture

class QSwipeGesture(QGesture):
    """ QSwipeGesture(QObject parent=None) """
    def horizontalDirection(self): # real signature unknown; restored from __doc__
        """ QSwipeGesture.horizontalDirection() -> QSwipeGesture.SwipeDirection """
        pass

    def setSwipeAngle(self, p_float): # real signature unknown; restored from __doc__
        """ QSwipeGesture.setSwipeAngle(float) """
        pass

    def swipeAngle(self): # real signature unknown; restored from __doc__
        """ QSwipeGesture.swipeAngle() -> float """
        return 0.0

    def verticalDirection(self): # real signature unknown; restored from __doc__
        """ QSwipeGesture.verticalDirection() -> QSwipeGesture.SwipeDirection """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Down = 4
    Left = 1
    NoDirection = 0
    Right = 2
    SwipeDirection = None # (!) real value is ''
    Up = 3


