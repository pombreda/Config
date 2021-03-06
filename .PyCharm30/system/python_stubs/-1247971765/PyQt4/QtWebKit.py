# encoding: utf-8
# module PyQt4.QtWebKit
# from /usr/lib/python3/dist-packages/PyQt4/QtWebKit.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# functions

def qWebKitMajorVersion(): # real signature unknown; restored from __doc__
    """ qWebKitMajorVersion() -> int """
    return 0

def qWebKitMinorVersion(): # real signature unknown; restored from __doc__
    """ qWebKitMinorVersion() -> int """
    return 0

def qWebKitVersion(): # real signature unknown; restored from __doc__
    """ qWebKitVersion() -> str """
    return ""

# classes

class QGraphicsWebView(__PyQt4_QtGui.QGraphicsWidget):
    """ QGraphicsWebView(QGraphicsItem parent=None) """
    def back(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.back() """
        pass

    def contextMenuEvent(self, QGraphicsSceneContextMenuEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.contextMenuEvent(QGraphicsSceneContextMenuEvent) """
        pass

    def dragEnterEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.dragEnterEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dragLeaveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.dragLeaveEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dragMoveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.dragMoveEvent(QGraphicsSceneDragDropEvent) """
        pass

    def dropEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.dropEvent(QGraphicsSceneDragDropEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.event(QEvent) -> bool """
        return False

    def findText(self, p_str, QWebPage_FindFlags_options=0): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.findText(str, QWebPage.FindFlags options=0) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.focusInEvent(QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.focusOutEvent(QFocusEvent) """
        pass

    def forward(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.forward() """
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.history() -> QWebHistory """
        return QWebHistory

    def hoverLeaveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.hoverLeaveEvent(QGraphicsSceneHoverEvent) """
        pass

    def hoverMoveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.hoverMoveEvent(QGraphicsSceneHoverEvent) """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.icon() -> QIcon """
        pass

    def iconChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsWebView.iconChanged [signal] """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.inputMethodQuery(Qt.InputMethodQuery) -> object """
        return object()

    def isModified(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.isModified() -> bool """
        return False

    def isTiledBackingStoreFrozen(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.isTiledBackingStoreFrozen() -> bool """
        return False

    def itemChange(self, QGraphicsItem_GraphicsItemChange, p_object): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.itemChange(QGraphicsItem.GraphicsItemChange, object) -> object """
        return object()

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.keyReleaseEvent(QKeyEvent) """
        pass

    def linkClicked(self, *args, **kwargs): # real signature unknown
        """ QGraphicsWebView.linkClicked[QUrl] [signal] """
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGraphicsWebView.load(QUrl)
        QGraphicsWebView.load(QNetworkRequest, QNetworkAccessManager.Operation operation=QNetworkAccessManager.GetOperation, QByteArray body=QByteArray())
        """
        pass

    def loadFinished(self, *args, **kwargs): # real signature unknown
        """ QGraphicsWebView.loadFinished[bool] [signal] """
        pass

    def loadProgress(self, *args, **kwargs): # real signature unknown
        """ QGraphicsWebView.loadProgress[int] [signal] """
        pass

    def loadStarted(self, *args, **kwargs): # real signature unknown
        """ QGraphicsWebView.loadStarted [signal] """
        pass

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.mouseDoubleClickEvent(QGraphicsSceneMouseEvent) """
        pass

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.mouseMoveEvent(QGraphicsSceneMouseEvent) """
        pass

    def mousePressEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.mousePressEvent(QGraphicsSceneMouseEvent) """
        pass

    def mouseReleaseEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.mouseReleaseEvent(QGraphicsSceneMouseEvent) """
        pass

    def page(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.page() -> QWebPage """
        return QWebPage

    def pageAction(self, QWebPage_WebAction): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.pageAction(QWebPage.WebAction) -> QAction """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.paint(QPainter, QStyleOptionGraphicsItem, QWidget widget=None) """
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.reload() """
        pass

    def renderHints(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.renderHints() -> QPainter.RenderHints """
        pass

    def resizesToContents(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.resizesToContents() -> bool """
        return False

    def sceneEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.sceneEvent(QEvent) -> bool """
        return False

    def setContent(self, QByteArray, str_mimeType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsWebView.setContent(QByteArray, str mimeType=QString(), QUrl baseUrl=QUrl()) """
        pass

    def setGeometry(self, QRectF): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.setGeometry(QRectF) """
        pass

    def setHtml(self, p_str, QUrl_baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QGraphicsWebView.setHtml(str, QUrl baseUrl=QUrl()) """
        pass

    def setPage(self, QWebPage): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.setPage(QWebPage) """
        pass

    def setRenderHint(self, QPainter_RenderHint, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.setRenderHint(QPainter.RenderHint, bool enabled=True) """
        pass

    def setRenderHints(self, QPainter_RenderHints): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.setRenderHints(QPainter.RenderHints) """
        pass

    def setResizesToContents(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.setResizesToContents(bool) """
        pass

    def setTiledBackingStoreFrozen(self, bool): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.setTiledBackingStoreFrozen(bool) """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.settings() -> QWebSettings """
        return QWebSettings

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.setUrl(QUrl) """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.setZoomFactor(float) """
        pass

    def sizeHint(self, Qt_SizeHint, QSizeF): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.sizeHint(Qt.SizeHint, QSizeF) -> QSizeF """
        pass

    def statusBarMessage(self, *args, **kwargs): # real signature unknown
        """ QGraphicsWebView.statusBarMessage[str] [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.stop() """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.title() -> str """
        return ""

    def titleChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsWebView.titleChanged[str] [signal] """
        pass

    def triggerPageAction(self, QWebPage_WebAction, bool_checked=False): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.triggerPageAction(QWebPage.WebAction, bool checked=False) """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.updateGeometry() """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.url() -> QUrl """
        pass

    def urlChanged(self, *args, **kwargs): # real signature unknown
        """ QGraphicsWebView.urlChanged[QUrl] [signal] """
        pass

    def wheelEvent(self, QGraphicsSceneWheelEvent): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.wheelEvent(QGraphicsSceneWheelEvent) """
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ QGraphicsWebView.zoomFactor() -> float """
        return 0.0

    def __init__(self, QGraphicsItem_parent=None): # real signature unknown; restored from __doc__
        pass


class QWebDatabase(): # skipped bases: <class 'sip.simplewrapper'>
    """ QWebDatabase(QWebDatabase) """
    def displayName(self): # real signature unknown; restored from __doc__
        """ QWebDatabase.displayName() -> str """
        return ""

    def expectedSize(self): # real signature unknown; restored from __doc__
        """ QWebDatabase.expectedSize() -> int """
        return 0

    def fileName(self): # real signature unknown; restored from __doc__
        """ QWebDatabase.fileName() -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ QWebDatabase.name() -> str """
        return ""

    def origin(self): # real signature unknown; restored from __doc__
        """ QWebDatabase.origin() -> QWebSecurityOrigin """
        return QWebSecurityOrigin

    def removeAllDatabases(self): # real signature unknown; restored from __doc__
        """ QWebDatabase.removeAllDatabases() """
        pass

    def removeDatabase(self, QWebDatabase): # real signature unknown; restored from __doc__
        """ QWebDatabase.removeDatabase(QWebDatabase) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QWebDatabase.size() -> int """
        return 0

    def __init__(self, QWebDatabase): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebElement(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QWebElement()
    QWebElement(QWebElement)
    """
    def addClass(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.addClass(str) """
        pass

    def appendInside(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebElement.appendInside(str)
        QWebElement.appendInside(QWebElement)
        """
        pass

    def appendOutside(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebElement.appendOutside(str)
        QWebElement.appendOutside(QWebElement)
        """
        pass

    def attribute(self, p_str, str_defaultValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QWebElement.attribute(str, str defaultValue=QString()) -> str """
        pass

    def attributeNames(self, str_namespaceUri=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QWebElement.attributeNames(str namespaceUri=QString()) -> list-of-str """
        pass

    def attributeNS(self, p_str, p_str_1, str_defaultValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QWebElement.attributeNS(str, str, str defaultValue=QString()) -> str """
        pass

    def classes(self): # real signature unknown; restored from __doc__
        """ QWebElement.classes() -> list-of-str """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ QWebElement.clone() -> QWebElement """
        return QWebElement

    def document(self): # real signature unknown; restored from __doc__
        """ QWebElement.document() -> QWebElement """
        return QWebElement

    def encloseContentsWith(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebElement.encloseContentsWith(QWebElement)
        QWebElement.encloseContentsWith(str)
        """
        pass

    def encloseWith(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebElement.encloseWith(str)
        QWebElement.encloseWith(QWebElement)
        """
        pass

    def evaluateJavaScript(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.evaluateJavaScript(str) -> object """
        return object()

    def findAll(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.findAll(str) -> QWebElementCollection """
        return QWebElementCollection

    def findFirst(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.findFirst(str) -> QWebElement """
        return QWebElement

    def firstChild(self): # real signature unknown; restored from __doc__
        """ QWebElement.firstChild() -> QWebElement """
        return QWebElement

    def geometry(self): # real signature unknown; restored from __doc__
        """ QWebElement.geometry() -> QRect """
        pass

    def hasAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.hasAttribute(str) -> bool """
        return False

    def hasAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QWebElement.hasAttributeNS(str, str) -> bool """
        return False

    def hasAttributes(self): # real signature unknown; restored from __doc__
        """ QWebElement.hasAttributes() -> bool """
        return False

    def hasClass(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.hasClass(str) -> bool """
        return False

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ QWebElement.hasFocus() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QWebElement.isNull() -> bool """
        return False

    def lastChild(self): # real signature unknown; restored from __doc__
        """ QWebElement.lastChild() -> QWebElement """
        return QWebElement

    def localName(self): # real signature unknown; restored from __doc__
        """ QWebElement.localName() -> str """
        return ""

    def namespaceUri(self): # real signature unknown; restored from __doc__
        """ QWebElement.namespaceUri() -> str """
        return ""

    def nextSibling(self): # real signature unknown; restored from __doc__
        """ QWebElement.nextSibling() -> QWebElement """
        return QWebElement

    def parent(self): # real signature unknown; restored from __doc__
        """ QWebElement.parent() -> QWebElement """
        return QWebElement

    def prefix(self): # real signature unknown; restored from __doc__
        """ QWebElement.prefix() -> str """
        return ""

    def prependInside(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebElement.prependInside(str)
        QWebElement.prependInside(QWebElement)
        """
        pass

    def prependOutside(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebElement.prependOutside(str)
        QWebElement.prependOutside(QWebElement)
        """
        pass

    def previousSibling(self): # real signature unknown; restored from __doc__
        """ QWebElement.previousSibling() -> QWebElement """
        return QWebElement

    def removeAllChildren(self): # real signature unknown; restored from __doc__
        """ QWebElement.removeAllChildren() """
        pass

    def removeAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.removeAttribute(str) """
        pass

    def removeAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QWebElement.removeAttributeNS(str, str) """
        pass

    def removeClass(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.removeClass(str) """
        pass

    def removeFromDocument(self): # real signature unknown; restored from __doc__
        """ QWebElement.removeFromDocument() """
        pass

    def render(self, QPainter, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebElement.render(QPainter)
        QWebElement.render(QPainter, QRect)
        """
        pass

    def replace(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebElement.replace(str)
        QWebElement.replace(QWebElement)
        """
        pass

    def setAttribute(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QWebElement.setAttribute(str, str) """
        pass

    def setAttributeNS(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ QWebElement.setAttributeNS(str, str, str) """
        pass

    def setFocus(self): # real signature unknown; restored from __doc__
        """ QWebElement.setFocus() """
        pass

    def setInnerXml(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.setInnerXml(str) """
        pass

    def setOuterXml(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.setOuterXml(str) """
        pass

    def setPlainText(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.setPlainText(str) """
        pass

    def setStyleProperty(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QWebElement.setStyleProperty(str, str) """
        pass

    def styleProperty(self, p_str, QWebElement_StyleResolveStrategy): # real signature unknown; restored from __doc__
        """ QWebElement.styleProperty(str, QWebElement.StyleResolveStrategy) -> str """
        return ""

    def tagName(self): # real signature unknown; restored from __doc__
        """ QWebElement.tagName() -> str """
        return ""

    def takeFromDocument(self): # real signature unknown; restored from __doc__
        """ QWebElement.takeFromDocument() -> QWebElement """
        return QWebElement

    def toggleClass(self, p_str): # real signature unknown; restored from __doc__
        """ QWebElement.toggleClass(str) """
        pass

    def toInnerXml(self): # real signature unknown; restored from __doc__
        """ QWebElement.toInnerXml() -> str """
        return ""

    def toOuterXml(self): # real signature unknown; restored from __doc__
        """ QWebElement.toOuterXml() -> str """
        return ""

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ QWebElement.toPlainText() -> str """
        return ""

    def webFrame(self): # real signature unknown; restored from __doc__
        """ QWebElement.webFrame() -> QWebFrame """
        return QWebFrame

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QWebElement=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    CascadedStyle = 1
    ComputedStyle = 2
    InlineStyle = 0
    StyleResolveStrategy = None # (!) real value is ''
    __hash__ = None


class QWebElementCollection(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QWebElementCollection()
    QWebElementCollection(QWebElement, str)
    QWebElementCollection(QWebElementCollection)
    """
    def append(self, QWebElementCollection): # real signature unknown; restored from __doc__
        """ QWebElementCollection.append(QWebElementCollection) """
        pass

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ QWebElementCollection.at(int) -> QWebElement """
        return QWebElement

    def count(self): # real signature unknown; restored from __doc__
        """ QWebElementCollection.count() -> int """
        return 0

    def first(self): # real signature unknown; restored from __doc__
        """ QWebElementCollection.first() -> QWebElement """
        return QWebElement

    def last(self): # real signature unknown; restored from __doc__
        """ QWebElementCollection.last() -> QWebElement """
        return QWebElement

    def toList(self): # real signature unknown; restored from __doc__
        """ QWebElementCollection.toList() -> list-of-QWebElement """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebFrame(__PyQt4_QtCore.QObject):
    # no doc
    def addToJavaScriptWindowObject(self, p_str, QObject): # real signature unknown; restored from __doc__
        """ QWebFrame.addToJavaScriptWindowObject(str, QObject) """
        pass

    def baseUrl(self): # real signature unknown; restored from __doc__
        """ QWebFrame.baseUrl() -> QUrl """
        pass

    def childFrames(self): # real signature unknown; restored from __doc__
        """ QWebFrame.childFrames() -> list-of-QWebFrame """
        pass

    def contentsSize(self): # real signature unknown; restored from __doc__
        """ QWebFrame.contentsSize() -> QSize """
        pass

    def contentsSizeChanged(self, *args, **kwargs): # real signature unknown
        """ QWebFrame.contentsSizeChanged[QSize] [signal] """
        pass

    def documentElement(self): # real signature unknown; restored from __doc__
        """ QWebFrame.documentElement() -> QWebElement """
        return QWebElement

    def evaluateJavaScript(self, p_str): # real signature unknown; restored from __doc__
        """ QWebFrame.evaluateJavaScript(str) -> object """
        return object()

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QWebFrame.event(QEvent) -> bool """
        return False

    def findAllElements(self, p_str): # real signature unknown; restored from __doc__
        """ QWebFrame.findAllElements(str) -> QWebElementCollection """
        return QWebElementCollection

    def findFirstElement(self, p_str): # real signature unknown; restored from __doc__
        """ QWebFrame.findFirstElement(str) -> QWebElement """
        return QWebElement

    def frameName(self): # real signature unknown; restored from __doc__
        """ QWebFrame.frameName() -> str """
        return ""

    def geometry(self): # real signature unknown; restored from __doc__
        """ QWebFrame.geometry() -> QRect """
        pass

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ QWebFrame.hasFocus() -> bool """
        return False

    def hitTestContent(self, QPoint): # real signature unknown; restored from __doc__
        """ QWebFrame.hitTestContent(QPoint) -> QWebHitTestResult """
        return QWebHitTestResult

    def icon(self): # real signature unknown; restored from __doc__
        """ QWebFrame.icon() -> QIcon """
        pass

    def iconChanged(self, *args, **kwargs): # real signature unknown
        """ QWebFrame.iconChanged [signal] """
        pass

    def initialLayoutCompleted(self, *args, **kwargs): # real signature unknown
        """ QWebFrame.initialLayoutCompleted [signal] """
        pass

    def javaScriptWindowObjectCleared(self, *args, **kwargs): # real signature unknown
        """ QWebFrame.javaScriptWindowObjectCleared [signal] """
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebFrame.load(QUrl)
        QWebFrame.load(QNetworkRequest, QNetworkAccessManager.Operation operation=QNetworkAccessManager.GetOperation, QByteArray body=QByteArray())
        """
        pass

    def loadFinished(self, *args, **kwargs): # real signature unknown
        """ QWebFrame.loadFinished[bool] [signal] """
        pass

    def loadStarted(self, *args, **kwargs): # real signature unknown
        """ QWebFrame.loadStarted [signal] """
        pass

    def metaData(self): # real signature unknown; restored from __doc__
        """ QWebFrame.metaData() -> dict-of-QString-list-of-QString """
        pass

    def page(self): # real signature unknown; restored from __doc__
        """ QWebFrame.page() -> QWebPage """
        return QWebPage

    def pageChanged(self, *args, **kwargs): # real signature unknown
        """ QWebFrame.pageChanged [signal] """
        pass

    def parentFrame(self): # real signature unknown; restored from __doc__
        """ QWebFrame.parentFrame() -> QWebFrame """
        return QWebFrame

    def pos(self): # real signature unknown; restored from __doc__
        """ QWebFrame.pos() -> QPoint """
        pass

    def print(self, QPrinter): # real signature unknown; restored from __doc__
        """ QWebFrame.print(QPrinter) """
        pass

    def print_(self, QPrinter): # real signature unknown; restored from __doc__
        """ QWebFrame.print_(QPrinter) """
        pass

    def render(self, QPainter, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebFrame.render(QPainter, QRegion)
        QWebFrame.render(QPainter)
        QWebFrame.render(QPainter, QWebFrame.RenderLayer, QRegion clip=QRegion())
        """
        pass

    def renderTreeDump(self): # real signature unknown; restored from __doc__
        """ QWebFrame.renderTreeDump() -> str """
        return ""

    def requestedUrl(self): # real signature unknown; restored from __doc__
        """ QWebFrame.requestedUrl() -> QUrl """
        pass

    def scroll(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QWebFrame.scroll(int, int) """
        pass

    def scrollBarGeometry(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QWebFrame.scrollBarGeometry(Qt.Orientation) -> QRect """
        pass

    def scrollBarMaximum(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QWebFrame.scrollBarMaximum(Qt.Orientation) -> int """
        return 0

    def scrollBarMinimum(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QWebFrame.scrollBarMinimum(Qt.Orientation) -> int """
        return 0

    def scrollBarPolicy(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QWebFrame.scrollBarPolicy(Qt.Orientation) -> Qt.ScrollBarPolicy """
        pass

    def scrollBarValue(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ QWebFrame.scrollBarValue(Qt.Orientation) -> int """
        return 0

    def scrollPosition(self): # real signature unknown; restored from __doc__
        """ QWebFrame.scrollPosition() -> QPoint """
        pass

    def scrollToAnchor(self, p_str): # real signature unknown; restored from __doc__
        """ QWebFrame.scrollToAnchor(str) """
        pass

    def securityOrigin(self): # real signature unknown; restored from __doc__
        """ QWebFrame.securityOrigin() -> QWebSecurityOrigin """
        return QWebSecurityOrigin

    def setContent(self, QByteArray, str_mimeType='', QUrl_baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QWebFrame.setContent(QByteArray, str mimeType='', QUrl baseUrl=QUrl()) """
        pass

    def setFocus(self): # real signature unknown; restored from __doc__
        """ QWebFrame.setFocus() """
        pass

    def setHtml(self, p_str, QUrl_baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QWebFrame.setHtml(str, QUrl baseUrl=QUrl()) """
        pass

    def setScrollBarPolicy(self, Qt_Orientation, Qt_ScrollBarPolicy): # real signature unknown; restored from __doc__
        """ QWebFrame.setScrollBarPolicy(Qt.Orientation, Qt.ScrollBarPolicy) """
        pass

    def setScrollBarValue(self, Qt_Orientation, p_int): # real signature unknown; restored from __doc__
        """ QWebFrame.setScrollBarValue(Qt.Orientation, int) """
        pass

    def setScrollPosition(self, QPoint): # real signature unknown; restored from __doc__
        """ QWebFrame.setScrollPosition(QPoint) """
        pass

    def setTextSizeMultiplier(self, p_float): # real signature unknown; restored from __doc__
        """ QWebFrame.setTextSizeMultiplier(float) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QWebFrame.setUrl(QUrl) """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ QWebFrame.setZoomFactor(float) """
        pass

    def textSizeMultiplier(self): # real signature unknown; restored from __doc__
        """ QWebFrame.textSizeMultiplier() -> float """
        return 0.0

    def title(self): # real signature unknown; restored from __doc__
        """ QWebFrame.title() -> str """
        return ""

    def titleChanged(self, *args, **kwargs): # real signature unknown
        """ QWebFrame.titleChanged[str] [signal] """
        pass

    def toHtml(self): # real signature unknown; restored from __doc__
        """ QWebFrame.toHtml() -> str """
        return ""

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ QWebFrame.toPlainText() -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ QWebFrame.url() -> QUrl """
        pass

    def urlChanged(self, *args, **kwargs): # real signature unknown
        """ QWebFrame.urlChanged[QUrl] [signal] """
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ QWebFrame.zoomFactor() -> float """
        return 0.0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AllLayers = 255
    ContentsLayer = 16
    PanIconLayer = 64
    RenderLayer = None # (!) real value is ''
    ScrollBarLayer = 32


class QWebHistory(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def back(self): # real signature unknown; restored from __doc__
        """ QWebHistory.back() """
        pass

    def backItem(self): # real signature unknown; restored from __doc__
        """ QWebHistory.backItem() -> QWebHistoryItem """
        return QWebHistoryItem

    def backItems(self, p_int): # real signature unknown; restored from __doc__
        """ QWebHistory.backItems(int) -> list-of-QWebHistoryItem """
        pass

    def canGoBack(self): # real signature unknown; restored from __doc__
        """ QWebHistory.canGoBack() -> bool """
        return False

    def canGoForward(self): # real signature unknown; restored from __doc__
        """ QWebHistory.canGoForward() -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ QWebHistory.clear() """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QWebHistory.count() -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ QWebHistory.currentItem() -> QWebHistoryItem """
        return QWebHistoryItem

    def currentItemIndex(self): # real signature unknown; restored from __doc__
        """ QWebHistory.currentItemIndex() -> int """
        return 0

    def forward(self): # real signature unknown; restored from __doc__
        """ QWebHistory.forward() """
        pass

    def forwardItem(self): # real signature unknown; restored from __doc__
        """ QWebHistory.forwardItem() -> QWebHistoryItem """
        return QWebHistoryItem

    def forwardItems(self, p_int): # real signature unknown; restored from __doc__
        """ QWebHistory.forwardItems(int) -> list-of-QWebHistoryItem """
        pass

    def goToItem(self, QWebHistoryItem): # real signature unknown; restored from __doc__
        """ QWebHistory.goToItem(QWebHistoryItem) """
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ QWebHistory.itemAt(int) -> QWebHistoryItem """
        return QWebHistoryItem

    def items(self): # real signature unknown; restored from __doc__
        """ QWebHistory.items() -> list-of-QWebHistoryItem """
        pass

    def maximumItemCount(self): # real signature unknown; restored from __doc__
        """ QWebHistory.maximumItemCount() -> int """
        return 0

    def setMaximumItemCount(self, p_int): # real signature unknown; restored from __doc__
        """ QWebHistory.setMaximumItemCount(int) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebHistoryInterface(__PyQt4_QtCore.QObject):
    """ QWebHistoryInterface(QObject parent=None) """
    def addHistoryEntry(self, p_str): # real signature unknown; restored from __doc__
        """ QWebHistoryInterface.addHistoryEntry(str) """
        pass

    def defaultInterface(self): # real signature unknown; restored from __doc__
        """ QWebHistoryInterface.defaultInterface() -> QWebHistoryInterface """
        return QWebHistoryInterface

    def historyContains(self, p_str): # real signature unknown; restored from __doc__
        """ QWebHistoryInterface.historyContains(str) -> bool """
        return False

    def setDefaultInterface(self, QWebHistoryInterface): # real signature unknown; restored from __doc__
        """ QWebHistoryInterface.setDefaultInterface(QWebHistoryInterface) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QWebHistoryItem(): # skipped bases: <class 'sip.simplewrapper'>
    """ QWebHistoryItem(QWebHistoryItem) """
    def icon(self): # real signature unknown; restored from __doc__
        """ QWebHistoryItem.icon() -> QIcon """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QWebHistoryItem.isValid() -> bool """
        return False

    def lastVisited(self): # real signature unknown; restored from __doc__
        """ QWebHistoryItem.lastVisited() -> QDateTime """
        pass

    def originalUrl(self): # real signature unknown; restored from __doc__
        """ QWebHistoryItem.originalUrl() -> QUrl """
        pass

    def setUserData(self, p_object): # real signature unknown; restored from __doc__
        """ QWebHistoryItem.setUserData(object) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ QWebHistoryItem.title() -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ QWebHistoryItem.url() -> QUrl """
        pass

    def userData(self): # real signature unknown; restored from __doc__
        """ QWebHistoryItem.userData() -> object """
        return object()

    def __init__(self, QWebHistoryItem): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebHitTestResult(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QWebHitTestResult()
    QWebHitTestResult(QWebHitTestResult)
    """
    def alternateText(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.alternateText() -> str """
        return ""

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.boundingRect() -> QRect """
        pass

    def element(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.element() -> QWebElement """
        return QWebElement

    def enclosingBlockElement(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.enclosingBlockElement() -> QWebElement """
        return QWebElement

    def frame(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.frame() -> QWebFrame """
        return QWebFrame

    def imageUrl(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.imageUrl() -> QUrl """
        pass

    def isContentEditable(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.isContentEditable() -> bool """
        return False

    def isContentSelected(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.isContentSelected() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.isNull() -> bool """
        return False

    def linkElement(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.linkElement() -> QWebElement """
        return QWebElement

    def linkTargetFrame(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.linkTargetFrame() -> QWebFrame """
        return QWebFrame

    def linkText(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.linkText() -> str """
        return ""

    def linkTitle(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.linkTitle() -> QUrl """
        pass

    def linkUrl(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.linkUrl() -> QUrl """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.pixmap() -> QPixmap """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.pos() -> QPoint """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ QWebHitTestResult.title() -> str """
        return ""

    def __init__(self, QWebHitTestResult=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebInspector(__PyQt4_QtGui.QWidget):
    """ QWebInspector(QWidget parent=None) """
    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QWebInspector.closeEvent(QCloseEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QWebInspector.event(QEvent) -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ QWebInspector.hideEvent(QHideEvent) """
        pass

    def page(self): # real signature unknown; restored from __doc__
        """ QWebInspector.page() -> QWebPage """
        return QWebPage

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QWebInspector.resizeEvent(QResizeEvent) """
        pass

    def setPage(self, QWebPage): # real signature unknown; restored from __doc__
        """ QWebInspector.setPage(QWebPage) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QWebInspector.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QWebInspector.sizeHint() -> QSize """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


class QWebPage(__PyQt4_QtCore.QObject):
    """ QWebPage(QObject parent=None) """
    def acceptNavigationRequest(self, QWebFrame, QNetworkRequest, QWebPage_NavigationType): # real signature unknown; restored from __doc__
        """ QWebPage.acceptNavigationRequest(QWebFrame, QNetworkRequest, QWebPage.NavigationType) -> bool """
        return False

    def action(self, QWebPage_WebAction): # real signature unknown; restored from __doc__
        """ QWebPage.action(QWebPage.WebAction) -> QAction """
        pass

    def applicationCacheQuotaExceeded(self, *args, **kwargs): # real signature unknown
        """ QWebPage.applicationCacheQuotaExceeded[QWebSecurityOrigin, int] [signal] """
        pass

    def bytesReceived(self): # real signature unknown; restored from __doc__
        """ QWebPage.bytesReceived() -> int """
        return 0

    def chooseFile(self, QWebFrame, p_str): # real signature unknown; restored from __doc__
        """ QWebPage.chooseFile(QWebFrame, str) -> str """
        return ""

    def contentsChanged(self, *args, **kwargs): # real signature unknown
        """ QWebPage.contentsChanged [signal] """
        pass

    def createPlugin(self, p_str, QUrl, list_of_str, list_of_str_1): # real signature unknown; restored from __doc__
        """ QWebPage.createPlugin(str, QUrl, list-of-str, list-of-str) -> QObject """
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ QWebPage.createStandardContextMenu() -> QMenu """
        pass

    def createWindow(self, QWebPage_WebWindowType): # real signature unknown; restored from __doc__
        """ QWebPage.createWindow(QWebPage.WebWindowType) -> QWebPage """
        return QWebPage

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ QWebPage.currentFrame() -> QWebFrame """
        return QWebFrame

    def databaseQuotaExceeded(self, *args, **kwargs): # real signature unknown
        """ QWebPage.databaseQuotaExceeded[QWebFrame, str] [signal] """
        pass

    def downloadRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.downloadRequested[QNetworkRequest] [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QWebPage.event(QEvent) -> bool """
        return False

    def extension(self, QWebPage_Extension, QWebPage_ExtensionOption_option=None, QWebPage_ExtensionReturn_output=None): # real signature unknown; restored from __doc__
        """ QWebPage.extension(QWebPage.Extension, QWebPage.ExtensionOption option=None, QWebPage.ExtensionReturn output=None) -> bool """
        return False

    def featurePermissionRequestCanceled(self, *args, **kwargs): # real signature unknown
        """ QWebPage.featurePermissionRequestCanceled[QWebFrame, QWebPage.Feature] [signal] """
        pass

    def featurePermissionRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.featurePermissionRequested[QWebFrame, QWebPage.Feature] [signal] """
        pass

    def findText(self, p_str, QWebPage_FindFlags_options=0): # real signature unknown; restored from __doc__
        """ QWebPage.findText(str, QWebPage.FindFlags options=0) -> bool """
        return False

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QWebPage.focusNextPrevChild(bool) -> bool """
        return False

    def forwardUnsupportedContent(self): # real signature unknown; restored from __doc__
        """ QWebPage.forwardUnsupportedContent() -> bool """
        return False

    def frameAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QWebPage.frameAt(QPoint) -> QWebFrame """
        return QWebFrame

    def frameCreated(self, *args, **kwargs): # real signature unknown
        """ QWebPage.frameCreated[QWebFrame] [signal] """
        pass

    def geometryChangeRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.geometryChangeRequested[QRect] [signal] """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ QWebPage.hasSelection() -> bool """
        return False

    def history(self): # real signature unknown; restored from __doc__
        """ QWebPage.history() -> QWebHistory """
        return QWebHistory

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QWebPage.inputMethodQuery(Qt.InputMethodQuery) -> object """
        return object()

    def isContentEditable(self): # real signature unknown; restored from __doc__
        """ QWebPage.isContentEditable() -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ QWebPage.isModified() -> bool """
        return False

    def javaScriptAlert(self, QWebFrame, p_str): # real signature unknown; restored from __doc__
        """ QWebPage.javaScriptAlert(QWebFrame, str) """
        pass

    def javaScriptConfirm(self, QWebFrame, p_str): # real signature unknown; restored from __doc__
        """ QWebPage.javaScriptConfirm(QWebFrame, str) -> bool """
        return False

    def javaScriptConsoleMessage(self, p_str, p_int, p_str_1): # real signature unknown; restored from __doc__
        """ QWebPage.javaScriptConsoleMessage(str, int, str) """
        pass

    def javaScriptPrompt(self, QWebFrame, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QWebPage.javaScriptPrompt(QWebFrame, str, str) -> (bool, str) """
        pass

    def linkClicked(self, *args, **kwargs): # real signature unknown
        """ QWebPage.linkClicked[QUrl] [signal] """
        pass

    def linkDelegationPolicy(self): # real signature unknown; restored from __doc__
        """ QWebPage.linkDelegationPolicy() -> QWebPage.LinkDelegationPolicy """
        pass

    def linkHovered(self, *args, **kwargs): # real signature unknown
        """ QWebPage.linkHovered[str, str, str] [signal] """
        pass

    def loadFinished(self, *args, **kwargs): # real signature unknown
        """ QWebPage.loadFinished[bool] [signal] """
        pass

    def loadProgress(self, *args, **kwargs): # real signature unknown
        """ QWebPage.loadProgress[int] [signal] """
        pass

    def loadStarted(self, *args, **kwargs): # real signature unknown
        """ QWebPage.loadStarted [signal] """
        pass

    def mainFrame(self): # real signature unknown; restored from __doc__
        """ QWebPage.mainFrame() -> QWebFrame """
        return QWebFrame

    def menuBarVisibilityChangeRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.menuBarVisibilityChangeRequested[bool] [signal] """
        pass

    def microFocusChanged(self, *args, **kwargs): # real signature unknown
        """ QWebPage.microFocusChanged [signal] """
        pass

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ QWebPage.networkAccessManager() -> QNetworkAccessManager """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ QWebPage.palette() -> QPalette """
        pass

    def pluginFactory(self): # real signature unknown; restored from __doc__
        """ QWebPage.pluginFactory() -> QWebPluginFactory """
        return QWebPluginFactory

    def preferredContentsSize(self): # real signature unknown; restored from __doc__
        """ QWebPage.preferredContentsSize() -> QSize """
        pass

    def printRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.printRequested[QWebFrame] [signal] """
        pass

    def repaintRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.repaintRequested[QRect] [signal] """
        pass

    def restoreFrameStateRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.restoreFrameStateRequested[QWebFrame] [signal] """
        pass

    def saveFrameStateRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.saveFrameStateRequested[QWebFrame, QWebHistoryItem] [signal] """
        pass

    def scrollRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.scrollRequested[int, int, QRect] [signal] """
        pass

    def selectedHtml(self): # real signature unknown; restored from __doc__
        """ QWebPage.selectedHtml() -> str """
        return ""

    def selectedText(self): # real signature unknown; restored from __doc__
        """ QWebPage.selectedText() -> str """
        return ""

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QWebPage.selectionChanged [signal] """
        pass

    def setActualVisibleContentRect(self, QRect): # real signature unknown; restored from __doc__
        """ QWebPage.setActualVisibleContentRect(QRect) """
        pass

    def setContentEditable(self, bool): # real signature unknown; restored from __doc__
        """ QWebPage.setContentEditable(bool) """
        pass

    def setFeaturePermission(self, QWebFrame, QWebPage_Feature, QWebPage_PermissionPolicy): # real signature unknown; restored from __doc__
        """ QWebPage.setFeaturePermission(QWebFrame, QWebPage.Feature, QWebPage.PermissionPolicy) """
        pass

    def setForwardUnsupportedContent(self, bool): # real signature unknown; restored from __doc__
        """ QWebPage.setForwardUnsupportedContent(bool) """
        pass

    def setLinkDelegationPolicy(self, QWebPage_LinkDelegationPolicy): # real signature unknown; restored from __doc__
        """ QWebPage.setLinkDelegationPolicy(QWebPage.LinkDelegationPolicy) """
        pass

    def setNetworkAccessManager(self, QNetworkAccessManager): # real signature unknown; restored from __doc__
        """ QWebPage.setNetworkAccessManager(QNetworkAccessManager) """
        pass

    def setPalette(self, QPalette): # real signature unknown; restored from __doc__
        """ QWebPage.setPalette(QPalette) """
        pass

    def setPluginFactory(self, QWebPluginFactory): # real signature unknown; restored from __doc__
        """ QWebPage.setPluginFactory(QWebPluginFactory) """
        pass

    def setPreferredContentsSize(self, QSize): # real signature unknown; restored from __doc__
        """ QWebPage.setPreferredContentsSize(QSize) """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ QWebPage.settings() -> QWebSettings """
        return QWebSettings

    def setView(self, QWidget): # real signature unknown; restored from __doc__
        """ QWebPage.setView(QWidget) """
        pass

    def setViewportSize(self, QSize): # real signature unknown; restored from __doc__
        """ QWebPage.setViewportSize(QSize) """
        pass

    def shouldInterruptJavaScript(self): # real signature unknown; restored from __doc__
        """ QWebPage.shouldInterruptJavaScript() -> bool """
        return False

    def statusBarMessage(self, *args, **kwargs): # real signature unknown
        """ QWebPage.statusBarMessage[str] [signal] """
        pass

    def statusBarVisibilityChangeRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.statusBarVisibilityChangeRequested[bool] [signal] """
        pass

    def supportedContentTypes(self): # real signature unknown; restored from __doc__
        """ QWebPage.supportedContentTypes() -> list-of-str """
        pass

    def supportsContentType(self, p_str): # real signature unknown; restored from __doc__
        """ QWebPage.supportsContentType(str) -> bool """
        return False

    def supportsExtension(self, QWebPage_Extension): # real signature unknown; restored from __doc__
        """ QWebPage.supportsExtension(QWebPage.Extension) -> bool """
        return False

    def swallowContextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QWebPage.swallowContextMenuEvent(QContextMenuEvent) -> bool """
        return False

    def toolBarVisibilityChangeRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.toolBarVisibilityChangeRequested[bool] [signal] """
        pass

    def totalBytes(self): # real signature unknown; restored from __doc__
        """ QWebPage.totalBytes() -> int """
        return 0

    def triggerAction(self, QWebPage_WebAction, bool_checked=False): # real signature unknown; restored from __doc__
        """ QWebPage.triggerAction(QWebPage.WebAction, bool checked=False) """
        pass

    def undoStack(self): # real signature unknown; restored from __doc__
        """ QWebPage.undoStack() -> QUndoStack """
        pass

    def unsupportedContent(self, *args, **kwargs): # real signature unknown
        """ QWebPage.unsupportedContent[QNetworkReply] [signal] """
        pass

    def updatePositionDependentActions(self, QPoint): # real signature unknown; restored from __doc__
        """ QWebPage.updatePositionDependentActions(QPoint) """
        pass

    def userAgentForUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QWebPage.userAgentForUrl(QUrl) -> str """
        return ""

    def view(self): # real signature unknown; restored from __doc__
        """ QWebPage.view() -> QWidget """
        pass

    def viewportAttributesForSize(self, QSize): # real signature unknown; restored from __doc__
        """ QWebPage.viewportAttributesForSize(QSize) -> QWebPage.ViewportAttributes """
        pass

    def viewportChangeRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.viewportChangeRequested [signal] """
        pass

    def viewportSize(self): # real signature unknown; restored from __doc__
        """ QWebPage.viewportSize() -> QSize """
        pass

    def windowCloseRequested(self, *args, **kwargs): # real signature unknown
        """ QWebPage.windowCloseRequested [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    AlignCenter = 63
    AlignJustified = 64
    AlignLeft = 65
    AlignRight = 66
    Back = 8
    ChooseMultipleFilesExtension = 0
    ChooseMultipleFilesExtensionOption = None # (!) real value is ''
    ChooseMultipleFilesExtensionReturn = None # (!) real value is ''
    Copy = 13
    CopyImageToClipboard = 7
    CopyImageUrlToClipboard = 68
    CopyLinkToClipboard = 4
    Cut = 12
    DelegateAllLinks = 2
    DelegateExternalLinks = 1
    DeleteEndOfWord = 42
    DeleteStartOfWord = 41
    DontDelegateLinks = 0
    DownloadImageToDisk = 6
    DownloadLinkToDisk = 3
    ErrorDomain = None # (!) real value is ''
    ErrorPageExtension = 1
    ErrorPageExtensionOption = None # (!) real value is ''
    ErrorPageExtensionReturn = None # (!) real value is ''
    Extension = None # (!) real value is ''
    ExtensionOption = None # (!) real value is ''
    ExtensionReturn = None # (!) real value is ''
    Feature = None # (!) real value is ''
    FindBackward = 1
    FindCaseSensitively = 2
    FindFlag = None # (!) real value is ''
    FindFlags = None # (!) real value is ''
    FindWrapsAroundDocument = 4
    Forward = 9
    Geolocation = 1
    HighlightAllOccurrences = 8
    Http = 1
    Indent = 61
    InsertLineSeparator = 51
    InsertOrderedList = 60
    InsertParagraphSeparator = 50
    InsertUnorderedList = 59
    InspectElement = 49
    LinkDelegationPolicy = None # (!) real value is ''
    MoveToEndOfBlock = 26
    MoveToEndOfDocument = 28
    MoveToEndOfLine = 24
    MoveToNextChar = 17
    MoveToNextLine = 21
    MoveToNextWord = 19
    MoveToPreviousChar = 18
    MoveToPreviousLine = 22
    MoveToPreviousWord = 20
    MoveToStartOfBlock = 25
    MoveToStartOfDocument = 27
    MoveToStartOfLine = 23
    NavigationType = None # (!) real value is ''
    NavigationTypeBackOrForward = 2
    NavigationTypeFormResubmitted = 4
    NavigationTypeFormSubmitted = 1
    NavigationTypeLinkClicked = 0
    NavigationTypeOther = 5
    NavigationTypeReload = 3
    Notifications = 0
    NoWebAction = -1
    OpenFrameInNewWindow = 2
    OpenImageInNewWindow = 5
    OpenLink = 0
    OpenLinkInNewWindow = 1
    Outdent = 62
    Paste = 14
    PasteAndMatchStyle = 54
    PermissionDeniedByUser = 2
    PermissionGrantedByUser = 1
    PermissionPolicy = None # (!) real value is ''
    PermissionUnknown = 0
    QtNetwork = 0
    Redo = 16
    Reload = 11
    ReloadAndBypassCache = 53
    RemoveFormat = 55
    SelectAll = 52
    SelectEndOfBlock = 38
    SelectEndOfDocument = 40
    SelectEndOfLine = 36
    SelectNextChar = 29
    SelectNextLine = 33
    SelectNextWord = 31
    SelectPreviousChar = 30
    SelectPreviousLine = 34
    SelectPreviousWord = 32
    SelectStartOfBlock = 37
    SelectStartOfDocument = 39
    SelectStartOfLine = 35
    SetTextDirectionDefault = 43
    SetTextDirectionLeftToRight = 44
    SetTextDirectionRightToLeft = 45
    Stop = 10
    StopScheduledPageRefresh = 67
    ToggleBold = 46
    ToggleItalic = 47
    ToggleStrikethrough = 56
    ToggleSubscript = 57
    ToggleSuperscript = 58
    ToggleUnderline = 48
    Undo = 15
    ViewportAttributes = None # (!) real value is ''
    WebAction = None # (!) real value is ''
    WebBrowserWindow = 0
    WebKit = 2
    WebModalDialog = 1
    WebWindowType = None # (!) real value is ''


class QWebPluginFactory(__PyQt4_QtCore.QObject):
    """ QWebPluginFactory(QObject parent=None) """
    def create(self, p_str, QUrl, list_of_str, list_of_str_1): # real signature unknown; restored from __doc__
        """ QWebPluginFactory.create(str, QUrl, list-of-str, list-of-str) -> QObject """
        pass

    def extension(self, QWebPluginFactory_Extension, QWebPluginFactory_ExtensionOption_option=None, QWebPluginFactory_ExtensionReturn_output=None): # real signature unknown; restored from __doc__
        """ QWebPluginFactory.extension(QWebPluginFactory.Extension, QWebPluginFactory.ExtensionOption option=None, QWebPluginFactory.ExtensionReturn output=None) -> bool """
        return False

    def plugins(self): # real signature unknown; restored from __doc__
        """ QWebPluginFactory.plugins() -> list-of-QWebPluginFactory.Plugin """
        pass

    def refreshPlugins(self): # real signature unknown; restored from __doc__
        """ QWebPluginFactory.refreshPlugins() """
        pass

    def supportsExtension(self, QWebPluginFactory_Extension): # real signature unknown; restored from __doc__
        """ QWebPluginFactory.supportsExtension(QWebPluginFactory.Extension) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Extension = None # (!) real value is ''
    ExtensionOption = None # (!) real value is ''
    ExtensionReturn = None # (!) real value is ''
    MimeType = None # (!) real value is ''
    Plugin = None # (!) real value is ''


class QWebSecurityOrigin(): # skipped bases: <class 'sip.simplewrapper'>
    """ QWebSecurityOrigin(QWebSecurityOrigin) """
    def addLocalScheme(self, p_str): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.addLocalScheme(str) """
        pass

    def allOrigins(self): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.allOrigins() -> list-of-QWebSecurityOrigin """
        pass

    def databaseQuota(self): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.databaseQuota() -> int """
        return 0

    def databases(self): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.databases() -> list-of-QWebDatabase """
        pass

    def databaseUsage(self): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.databaseUsage() -> int """
        return 0

    def host(self): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.host() -> str """
        return ""

    def localSchemes(self): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.localSchemes() -> list-of-str """
        pass

    def port(self): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.port() -> int """
        return 0

    def removeLocalScheme(self, p_str): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.removeLocalScheme(str) """
        pass

    def scheme(self): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.scheme() -> str """
        return ""

    def setApplicationCacheQuota(self, p_int): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.setApplicationCacheQuota(int) """
        pass

    def setDatabaseQuota(self, p_int): # real signature unknown; restored from __doc__
        """ QWebSecurityOrigin.setDatabaseQuota(int) """
        pass

    def __init__(self, QWebSecurityOrigin): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebSettings(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def clearIconDatabase(self): # real signature unknown; restored from __doc__
        """ QWebSettings.clearIconDatabase() """
        pass

    def clearMemoryCaches(self): # real signature unknown; restored from __doc__
        """ QWebSettings.clearMemoryCaches() """
        pass

    def defaultTextEncoding(self): # real signature unknown; restored from __doc__
        """ QWebSettings.defaultTextEncoding() -> str """
        return ""

    def enablePersistentStorage(self, str_path=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QWebSettings.enablePersistentStorage(str path=QString()) """
        pass

    def fontFamily(self, QWebSettings_FontFamily): # real signature unknown; restored from __doc__
        """ QWebSettings.fontFamily(QWebSettings.FontFamily) -> str """
        return ""

    def fontSize(self, QWebSettings_FontSize): # real signature unknown; restored from __doc__
        """ QWebSettings.fontSize(QWebSettings.FontSize) -> int """
        return 0

    def globalSettings(self): # real signature unknown; restored from __doc__
        """ QWebSettings.globalSettings() -> QWebSettings """
        return QWebSettings

    def iconDatabasePath(self): # real signature unknown; restored from __doc__
        """ QWebSettings.iconDatabasePath() -> str """
        return ""

    def iconForUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QWebSettings.iconForUrl(QUrl) -> QIcon """
        pass

    def localStoragePath(self): # real signature unknown; restored from __doc__
        """ QWebSettings.localStoragePath() -> str """
        return ""

    def maximumPagesInCache(self): # real signature unknown; restored from __doc__
        """ QWebSettings.maximumPagesInCache() -> int """
        return 0

    def offlineStorageDefaultQuota(self): # real signature unknown; restored from __doc__
        """ QWebSettings.offlineStorageDefaultQuota() -> int """
        return 0

    def offlineStoragePath(self): # real signature unknown; restored from __doc__
        """ QWebSettings.offlineStoragePath() -> str """
        return ""

    def offlineWebApplicationCachePath(self): # real signature unknown; restored from __doc__
        """ QWebSettings.offlineWebApplicationCachePath() -> str """
        return ""

    def offlineWebApplicationCacheQuota(self): # real signature unknown; restored from __doc__
        """ QWebSettings.offlineWebApplicationCacheQuota() -> int """
        return 0

    def resetAttribute(self, QWebSettings_WebAttribute): # real signature unknown; restored from __doc__
        """ QWebSettings.resetAttribute(QWebSettings.WebAttribute) """
        pass

    def resetFontFamily(self, QWebSettings_FontFamily): # real signature unknown; restored from __doc__
        """ QWebSettings.resetFontFamily(QWebSettings.FontFamily) """
        pass

    def resetFontSize(self, QWebSettings_FontSize): # real signature unknown; restored from __doc__
        """ QWebSettings.resetFontSize(QWebSettings.FontSize) """
        pass

    def setAttribute(self, QWebSettings_WebAttribute, bool): # real signature unknown; restored from __doc__
        """ QWebSettings.setAttribute(QWebSettings.WebAttribute, bool) """
        pass

    def setDefaultTextEncoding(self, p_str): # real signature unknown; restored from __doc__
        """ QWebSettings.setDefaultTextEncoding(str) """
        pass

    def setFontFamily(self, QWebSettings_FontFamily, p_str): # real signature unknown; restored from __doc__
        """ QWebSettings.setFontFamily(QWebSettings.FontFamily, str) """
        pass

    def setFontSize(self, QWebSettings_FontSize, p_int): # real signature unknown; restored from __doc__
        """ QWebSettings.setFontSize(QWebSettings.FontSize, int) """
        pass

    def setIconDatabasePath(self, p_str): # real signature unknown; restored from __doc__
        """ QWebSettings.setIconDatabasePath(str) """
        pass

    def setLocalStoragePath(self, p_str): # real signature unknown; restored from __doc__
        """ QWebSettings.setLocalStoragePath(str) """
        pass

    def setMaximumPagesInCache(self, p_int): # real signature unknown; restored from __doc__
        """ QWebSettings.setMaximumPagesInCache(int) """
        pass

    def setObjectCacheCapacities(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ QWebSettings.setObjectCacheCapacities(int, int, int) """
        pass

    def setOfflineStorageDefaultQuota(self, p_int): # real signature unknown; restored from __doc__
        """ QWebSettings.setOfflineStorageDefaultQuota(int) """
        pass

    def setOfflineStoragePath(self, p_str): # real signature unknown; restored from __doc__
        """ QWebSettings.setOfflineStoragePath(str) """
        pass

    def setOfflineWebApplicationCachePath(self, p_str): # real signature unknown; restored from __doc__
        """ QWebSettings.setOfflineWebApplicationCachePath(str) """
        pass

    def setOfflineWebApplicationCacheQuota(self, p_int): # real signature unknown; restored from __doc__
        """ QWebSettings.setOfflineWebApplicationCacheQuota(int) """
        pass

    def setUserStyleSheetUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QWebSettings.setUserStyleSheetUrl(QUrl) """
        pass

    def setWebGraphic(self, QWebSettings_WebGraphic, QPixmap): # real signature unknown; restored from __doc__
        """ QWebSettings.setWebGraphic(QWebSettings.WebGraphic, QPixmap) """
        pass

    def testAttribute(self, QWebSettings_WebAttribute): # real signature unknown; restored from __doc__
        """ QWebSettings.testAttribute(QWebSettings.WebAttribute) -> bool """
        return False

    def userStyleSheetUrl(self): # real signature unknown; restored from __doc__
        """ QWebSettings.userStyleSheetUrl() -> QUrl """
        pass

    def webGraphic(self, QWebSettings_WebGraphic): # real signature unknown; restored from __doc__
        """ QWebSettings.webGraphic(QWebSettings.WebGraphic) -> QPixmap """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AcceleratedCompositingEnabled = 17
    AutoLoadImages = 0
    CursiveFont = 4
    DefaultFixedFontSize = 3
    DefaultFontSize = 2
    DefaultFrameIconGraphic = 2
    DeveloperExtrasEnabled = 7
    DnsPrefetchEnabled = 15
    FantasyFont = 5
    FixedFont = 1
    FontFamily = None # (!) real value is ''
    FontSize = None # (!) real value is ''
    FrameFlatteningEnabled = 21
    HyperlinkAuditingEnabled = 25
    InputSpeechButtonGraphic = 5
    JavaEnabled = 2
    JavascriptCanAccessClipboard = 6
    JavascriptCanCloseWindows = 23
    JavascriptCanOpenWindows = 5
    JavascriptEnabled = 1
    LinksIncludedInFocusChain = 8
    LocalContentCanAccessFileUrls = 19
    LocalContentCanAccessRemoteUrls = 14
    LocalStorageDatabaseEnabled = 13
    LocalStorageEnabled = 13
    MinimumFontSize = 0
    MinimumLogicalFontSize = 1
    MissingImageGraphic = 0
    MissingPluginGraphic = 1
    OfflineStorageDatabaseEnabled = 11
    OfflineWebApplicationCacheEnabled = 12
    PluginsEnabled = 3
    PrintElementBackgrounds = 10
    PrivateBrowsingEnabled = 4
    SansSerifFont = 3
    SearchCancelButtonGraphic = 6
    SearchCancelButtonPressedGraphic = 7
    SerifFont = 2
    SiteSpecificQuirksEnabled = 22
    SpatialNavigationEnabled = 18
    StandardFont = 0
    TextAreaSizeGripCornerGraphic = 3
    TiledBackingStoreEnabled = 20
    WebAttribute = None # (!) real value is ''
    WebGLEnabled = 24
    WebGraphic = None # (!) real value is ''
    XSSAuditingEnabled = 16
    ZoomTextOnly = 9


class QWebView(__PyQt4_QtGui.QWidget):
    """ QWebView(QWidget parent=None) """
    def back(self): # real signature unknown; restored from __doc__
        """ QWebView.back() """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QWebView.changeEvent(QEvent) """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ QWebView.contextMenuEvent(QContextMenuEvent) """
        pass

    def createWindow(self, QWebPage_WebWindowType): # real signature unknown; restored from __doc__
        """ QWebView.createWindow(QWebPage.WebWindowType) -> QWebView """
        return QWebView

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ QWebView.dragEnterEvent(QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ QWebView.dragLeaveEvent(QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ QWebView.dragMoveEvent(QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ QWebView.dropEvent(QDropEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QWebView.event(QEvent) -> bool """
        return False

    def findText(self, p_str, QWebPage_FindFlags_options=0): # real signature unknown; restored from __doc__
        """ QWebView.findText(str, QWebPage.FindFlags options=0) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QWebView.focusInEvent(QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ QWebView.focusNextPrevChild(bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ QWebView.focusOutEvent(QFocusEvent) """
        pass

    def forward(self): # real signature unknown; restored from __doc__
        """ QWebView.forward() """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ QWebView.hasSelection() -> bool """
        return False

    def history(self): # real signature unknown; restored from __doc__
        """ QWebView.history() -> QWebHistory """
        return QWebHistory

    def icon(self): # real signature unknown; restored from __doc__
        """ QWebView.icon() -> QIcon """
        pass

    def iconChanged(self, *args, **kwargs): # real signature unknown
        """ QWebView.iconChanged [signal] """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QWebView.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QWebView.inputMethodQuery(Qt.InputMethodQuery) -> object """
        return object()

    def isModified(self): # real signature unknown; restored from __doc__
        """ QWebView.isModified() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QWebView.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QWebView.keyReleaseEvent(QKeyEvent) """
        pass

    def linkClicked(self, *args, **kwargs): # real signature unknown
        """ QWebView.linkClicked[QUrl] [signal] """
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWebView.load(QUrl)
        QWebView.load(QNetworkRequest, QNetworkAccessManager.Operation operation=QNetworkAccessManager.GetOperation, QByteArray body=QByteArray())
        """
        pass

    def loadFinished(self, *args, **kwargs): # real signature unknown
        """ QWebView.loadFinished[bool] [signal] """
        pass

    def loadProgress(self, *args, **kwargs): # real signature unknown
        """ QWebView.loadProgress[int] [signal] """
        pass

    def loadStarted(self, *args, **kwargs): # real signature unknown
        """ QWebView.loadStarted [signal] """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QWebView.mouseDoubleClickEvent(QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QWebView.mouseMoveEvent(QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QWebView.mousePressEvent(QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ QWebView.mouseReleaseEvent(QMouseEvent) """
        pass

    def page(self): # real signature unknown; restored from __doc__
        """ QWebView.page() -> QWebPage """
        return QWebPage

    def pageAction(self, QWebPage_WebAction): # real signature unknown; restored from __doc__
        """ QWebView.pageAction(QWebPage.WebAction) -> QAction """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QWebView.paintEvent(QPaintEvent) """
        pass

    def print(self, QPrinter): # real signature unknown; restored from __doc__
        """ QWebView.print(QPrinter) """
        pass

    def print_(self, QPrinter): # real signature unknown; restored from __doc__
        """ QWebView.print_(QPrinter) """
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ QWebView.reload() """
        pass

    def renderHints(self): # real signature unknown; restored from __doc__
        """ QWebView.renderHints() -> QPainter.RenderHints """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QWebView.resizeEvent(QResizeEvent) """
        pass

    def selectedHtml(self): # real signature unknown; restored from __doc__
        """ QWebView.selectedHtml() -> str """
        return ""

    def selectedText(self): # real signature unknown; restored from __doc__
        """ QWebView.selectedText() -> str """
        return ""

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ QWebView.selectionChanged [signal] """
        pass

    def setContent(self, QByteArray, str_mimeType='', QUrl_baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QWebView.setContent(QByteArray, str mimeType='', QUrl baseUrl=QUrl()) """
        pass

    def setHtml(self, p_str, QUrl_baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QWebView.setHtml(str, QUrl baseUrl=QUrl()) """
        pass

    def setPage(self, QWebPage): # real signature unknown; restored from __doc__
        """ QWebView.setPage(QWebPage) """
        pass

    def setRenderHint(self, QPainter_RenderHint, bool_enabled=True): # real signature unknown; restored from __doc__
        """ QWebView.setRenderHint(QPainter.RenderHint, bool enabled=True) """
        pass

    def setRenderHints(self, QPainter_RenderHints): # real signature unknown; restored from __doc__
        """ QWebView.setRenderHints(QPainter.RenderHints) """
        pass

    def setTextSizeMultiplier(self, p_float): # real signature unknown; restored from __doc__
        """ QWebView.setTextSizeMultiplier(float) """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ QWebView.settings() -> QWebSettings """
        return QWebSettings

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QWebView.setUrl(QUrl) """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ QWebView.setZoomFactor(float) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QWebView.sizeHint() -> QSize """
        pass

    def statusBarMessage(self, *args, **kwargs): # real signature unknown
        """ QWebView.statusBarMessage[str] [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QWebView.stop() """
        pass

    def textSizeMultiplier(self): # real signature unknown; restored from __doc__
        """ QWebView.textSizeMultiplier() -> float """
        return 0.0

    def title(self): # real signature unknown; restored from __doc__
        """ QWebView.title() -> str """
        return ""

    def titleChanged(self, *args, **kwargs): # real signature unknown
        """ QWebView.titleChanged[str] [signal] """
        pass

    def triggerPageAction(self, QWebPage_WebAction, bool_checked=False): # real signature unknown; restored from __doc__
        """ QWebView.triggerPageAction(QWebPage.WebAction, bool checked=False) """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ QWebView.url() -> QUrl """
        pass

    def urlChanged(self, *args, **kwargs): # real signature unknown
        """ QWebView.urlChanged[QUrl] [signal] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ QWebView.wheelEvent(QWheelEvent) """
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ QWebView.zoomFactor() -> float """
        return 0.0

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

