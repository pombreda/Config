# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkCookie(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QNetworkCookie(QByteArray name=QByteArray(), QByteArray value=QByteArray())
    QNetworkCookie(QNetworkCookie)
    """
    def domain(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.domain() -> str """
        return ""

    def expirationDate(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.expirationDate() -> QDateTime """
        pass

    def isHttpOnly(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.isHttpOnly() -> bool """
        return False

    def isSecure(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.isSecure() -> bool """
        return False

    def isSessionCookie(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.isSessionCookie() -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.name() -> QByteArray """
        pass

    def parseCookies(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkCookie.parseCookies(QByteArray) -> list-of-QNetworkCookie """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.path() -> str """
        return ""

    def setDomain(self, p_str): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setDomain(str) """
        pass

    def setExpirationDate(self, QDateTime): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setExpirationDate(QDateTime) """
        pass

    def setHttpOnly(self, bool): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setHttpOnly(bool) """
        pass

    def setName(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setName(QByteArray) """
        pass

    def setPath(self, p_str): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setPath(str) """
        pass

    def setSecure(self, bool): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setSecure(bool) """
        pass

    def setValue(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkCookie.setValue(QByteArray) """
        pass

    def toRawForm(self, QNetworkCookie_RawForm_form=None): # real signature unknown; restored from __doc__
        """ QNetworkCookie.toRawForm(QNetworkCookie.RawForm form=QNetworkCookie.Full) -> QByteArray """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ QNetworkCookie.value() -> QByteArray """
        pass

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


    Full = 1
    NameAndValueOnly = 0
    RawForm = None # (!) real value is ''
    __hash__ = None


