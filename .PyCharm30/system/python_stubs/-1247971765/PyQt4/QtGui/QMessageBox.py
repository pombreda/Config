# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QDialog import QDialog

class QMessageBox(QDialog):
    """
    QMessageBox(QWidget parent=None)
    QMessageBox(QMessageBox.Icon, str, str, QMessageBox.StandardButtons buttons=QMessageBox.NoButton, QWidget parent=None, Qt.WindowFlags flags=Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint)
    QMessageBox(str, str, QMessageBox.Icon, int, int, int, QWidget parent=None, Qt.WindowFlags flags=Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint)
    """
    def about(self, QWidget, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QMessageBox.about(QWidget, str, str) """
        pass

    def aboutQt(self, QWidget, str_title=''): # real signature unknown; restored from __doc__
        """ QMessageBox.aboutQt(QWidget, str title='') """
        pass

    def addButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.addButton(QAbstractButton, QMessageBox.ButtonRole)
        QMessageBox.addButton(str, QMessageBox.ButtonRole) -> QPushButton
        QMessageBox.addButton(QMessageBox.StandardButton) -> QPushButton
        """
        return QPushButton

    def button(self, QMessageBox_StandardButton): # real signature unknown; restored from __doc__
        """ QMessageBox.button(QMessageBox.StandardButton) -> QAbstractButton """
        return QAbstractButton

    def buttonClicked(self, *args, **kwargs): # real signature unknown
        """ QMessageBox.buttonClicked[QAbstractButton] [signal] """
        pass

    def buttonRole(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QMessageBox.buttonRole(QAbstractButton) -> QMessageBox.ButtonRole """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ QMessageBox.buttons() -> list-of-QAbstractButton """
        pass

    def buttonText(self, p_int): # real signature unknown; restored from __doc__
        """ QMessageBox.buttonText(int) -> str """
        return ""

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.changeEvent(QEvent) """
        pass

    def clickedButton(self): # real signature unknown; restored from __doc__
        """ QMessageBox.clickedButton() -> QAbstractButton """
        return QAbstractButton

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.closeEvent(QCloseEvent) """
        pass

    def critical(self, QWidget, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.critical(QWidget, str, str, QMessageBox.StandardButtons buttons=QMessageBox.Ok, QMessageBox.StandardButton defaultButton=QMessageBox.NoButton) -> QMessageBox.StandardButton
        QMessageBox.critical(QWidget, str, str, int, int, int button2=0) -> int
        QMessageBox.critical(QWidget, str, str, str, str button1Text='', str button2Text='', int defaultButtonNumber=0, int escapeButtonNumber=-1) -> int
        """
        return 0

    def defaultButton(self): # real signature unknown; restored from __doc__
        """ QMessageBox.defaultButton() -> QPushButton """
        return QPushButton

    def detailedText(self): # real signature unknown; restored from __doc__
        """ QMessageBox.detailedText() -> str """
        return ""

    def escapeButton(self): # real signature unknown; restored from __doc__
        """ QMessageBox.escapeButton() -> QAbstractButton """
        return QAbstractButton

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.event(QEvent) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ QMessageBox.icon() -> QMessageBox.Icon """
        pass

    def iconPixmap(self): # real signature unknown; restored from __doc__
        """ QMessageBox.iconPixmap() -> QPixmap """
        return QPixmap

    def information(self, QWidget, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.information(QWidget, str, str, QMessageBox.StandardButtons buttons=QMessageBox.Ok, QMessageBox.StandardButton defaultButton=QMessageBox.NoButton) -> QMessageBox.StandardButton
        QMessageBox.information(QWidget, str, str, int, int button1=0, int button2=0) -> int
        QMessageBox.information(QWidget, str, str, str, str button1Text='', str button2Text='', int defaultButtonNumber=0, int escapeButtonNumber=-1) -> int
        """
        return 0

    def informativeText(self): # real signature unknown; restored from __doc__
        """ QMessageBox.informativeText() -> str """
        return ""

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.keyPressEvent(QKeyEvent) """
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.open()
        QMessageBox.open(QObject, SLOT())
        QMessageBox.open(callable)
        """
        pass

    def question(self, QWidget, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.question(QWidget, str, str, QMessageBox.StandardButtons buttons=QMessageBox.Ok, QMessageBox.StandardButton defaultButton=QMessageBox.NoButton) -> QMessageBox.StandardButton
        QMessageBox.question(QWidget, str, str, int, int button1=0, int button2=0) -> int
        QMessageBox.question(QWidget, str, str, str, str button1Text='', str button2Text='', int defaultButtonNumber=0, int escapeButtonNumber=-1) -> int
        """
        return 0

    def removeButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QMessageBox.removeButton(QAbstractButton) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.resizeEvent(QResizeEvent) """
        pass

    def setButtonText(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ QMessageBox.setButtonText(int, str) """
        pass

    def setDefaultButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.setDefaultButton(QPushButton)
        QMessageBox.setDefaultButton(QMessageBox.StandardButton)
        """
        pass

    def setDetailedText(self, p_str): # real signature unknown; restored from __doc__
        """ QMessageBox.setDetailedText(str) """
        pass

    def setEscapeButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.setEscapeButton(QAbstractButton)
        QMessageBox.setEscapeButton(QMessageBox.StandardButton)
        """
        pass

    def setIcon(self, QMessageBox_Icon): # real signature unknown; restored from __doc__
        """ QMessageBox.setIcon(QMessageBox.Icon) """
        pass

    def setIconPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ QMessageBox.setIconPixmap(QPixmap) """
        pass

    def setInformativeText(self, p_str): # real signature unknown; restored from __doc__
        """ QMessageBox.setInformativeText(str) """
        pass

    def setStandardButtons(self, QMessageBox_StandardButtons): # real signature unknown; restored from __doc__
        """ QMessageBox.setStandardButtons(QMessageBox.StandardButtons) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ QMessageBox.setText(str) """
        pass

    def setTextFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ QMessageBox.setTextFormat(Qt.TextFormat) """
        pass

    def setWindowModality(self, Qt_WindowModality): # real signature unknown; restored from __doc__
        """ QMessageBox.setWindowModality(Qt.WindowModality) """
        pass

    def setWindowTitle(self, p_str): # real signature unknown; restored from __doc__
        """ QMessageBox.setWindowTitle(str) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QMessageBox.sizeHint() -> QSize """
        pass

    def standardButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QMessageBox.standardButton(QAbstractButton) -> QMessageBox.StandardButton """
        pass

    def standardButtons(self): # real signature unknown; restored from __doc__
        """ QMessageBox.standardButtons() -> QMessageBox.StandardButtons """
        pass

    def standardIcon(self, QMessageBox_Icon): # real signature unknown; restored from __doc__
        """ QMessageBox.standardIcon(QMessageBox.Icon) -> QPixmap """
        return QPixmap

    def text(self): # real signature unknown; restored from __doc__
        """ QMessageBox.text() -> str """
        return ""

    def textFormat(self): # real signature unknown; restored from __doc__
        """ QMessageBox.textFormat() -> Qt.TextFormat """
        pass

    def warning(self, QWidget, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.warning(QWidget, str, str, QMessageBox.StandardButtons buttons=QMessageBox.Ok, QMessageBox.StandardButton defaultButton=QMessageBox.NoButton) -> QMessageBox.StandardButton
        QMessageBox.warning(QWidget, str, str, int, int, int button2=0) -> int
        QMessageBox.warning(QWidget, str, str, str, str button1Text='', str button2Text='', int defaultButtonNumber=0, int escapeButtonNumber=-1) -> int
        """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Abort = 262144
    AcceptRole = 0
    ActionRole = 3
    Apply = 33554432
    ApplyRole = 8
    ButtonMask = -769
    ButtonRole = None # (!) real value is ''
    Cancel = 4194304
    Close = 2097152
    Critical = 3
    Default = 256
    DestructiveRole = 2
    Discard = 8388608
    Escape = 512
    FirstButton = 1024
    FlagMask = 768
    Help = 16777216
    HelpRole = 4
    Icon = None # (!) real value is ''
    Ignore = 1048576
    Information = 1
    InvalidRole = -1
    LastButton = 134217728
    No = 65536
    NoAll = 131072
    NoButton = 0
    NoIcon = 0
    NoRole = 6
    NoToAll = 131072
    Ok = 1024
    Open = 8192
    Question = 4
    RejectRole = 1
    Reset = 67108864
    ResetRole = 7
    RestoreDefaults = 134217728
    Retry = 524288
    Save = 2048
    SaveAll = 4096
    StandardButton = None # (!) real value is ''
    StandardButtons = None # (!) real value is ''
    Warning = 2
    Yes = 16384
    YesAll = 32768
    YesRole = 5
    YesToAll = 32768


