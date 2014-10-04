# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QIODevice import QIODevice

class QProcess(QIODevice):
    """ QProcess(QObject parent=None) """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ QProcess.atEnd() -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ QProcess.bytesAvailable() -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ QProcess.bytesToWrite() -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ QProcess.canReadLine() -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ QProcess.close() """
        pass

    def closeReadChannel(self, QProcess_ProcessChannel): # real signature unknown; restored from __doc__
        """ QProcess.closeReadChannel(QProcess.ProcessChannel) """
        pass

    def closeWriteChannel(self): # real signature unknown; restored from __doc__
        """ QProcess.closeWriteChannel() """
        pass

    def environment(self): # real signature unknown; restored from __doc__
        """ QProcess.environment() -> list-of-str """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """
        QProcess.error() -> QProcess.ProcessError
        QProcess.error[QProcess.ProcessError] [signal]
        """
        pass

    def execute(self, p_str, list_of_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QProcess.execute(str, list-of-str) -> int
        QProcess.execute(str) -> int
        """
        return 0

    def exitCode(self): # real signature unknown; restored from __doc__
        """ QProcess.exitCode() -> int """
        return 0

    def exitStatus(self): # real signature unknown; restored from __doc__
        """ QProcess.exitStatus() -> QProcess.ExitStatus """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """
        QProcess.finished[int, QProcess.ExitStatus] [signal]
        QProcess.finished[int] [signal]
        """
        pass

    def isSequential(self): # real signature unknown; restored from __doc__
        """ QProcess.isSequential() -> bool """
        return False

    def kill(self): # real signature unknown; restored from __doc__
        """ QProcess.kill() """
        pass

    def pid(self): # real signature unknown; restored from __doc__
        """ QProcess.pid() -> int """
        return 0

    def processChannelMode(self): # real signature unknown; restored from __doc__
        """ QProcess.processChannelMode() -> QProcess.ProcessChannelMode """
        pass

    def processEnvironment(self): # real signature unknown; restored from __doc__
        """ QProcess.processEnvironment() -> QProcessEnvironment """
        return QProcessEnvironment

    def readAllStandardError(self): # real signature unknown; restored from __doc__
        """ QProcess.readAllStandardError() -> QByteArray """
        return QByteArray

    def readAllStandardOutput(self): # real signature unknown; restored from __doc__
        """ QProcess.readAllStandardOutput() -> QByteArray """
        return QByteArray

    def readChannel(self): # real signature unknown; restored from __doc__
        """ QProcess.readChannel() -> QProcess.ProcessChannel """
        pass

    def readChannelMode(self): # real signature unknown; restored from __doc__
        """ QProcess.readChannelMode() -> QProcess.ProcessChannelMode """
        pass

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ QProcess.readData(int) -> bytes """
        return b""

    def readyReadStandardError(self, *args, **kwargs): # real signature unknown
        """ QProcess.readyReadStandardError [signal] """
        pass

    def readyReadStandardOutput(self, *args, **kwargs): # real signature unknown
        """ QProcess.readyReadStandardOutput [signal] """
        pass

    def setEnvironment(self, list_of_str): # real signature unknown; restored from __doc__
        """ QProcess.setEnvironment(list-of-str) """
        pass

    def setProcessChannelMode(self, QProcess_ProcessChannelMode): # real signature unknown; restored from __doc__
        """ QProcess.setProcessChannelMode(QProcess.ProcessChannelMode) """
        pass

    def setProcessEnvironment(self, QProcessEnvironment): # real signature unknown; restored from __doc__
        """ QProcess.setProcessEnvironment(QProcessEnvironment) """
        pass

    def setProcessState(self, QProcess_ProcessState): # real signature unknown; restored from __doc__
        """ QProcess.setProcessState(QProcess.ProcessState) """
        pass

    def setReadChannel(self, QProcess_ProcessChannel): # real signature unknown; restored from __doc__
        """ QProcess.setReadChannel(QProcess.ProcessChannel) """
        pass

    def setReadChannelMode(self, QProcess_ProcessChannelMode): # real signature unknown; restored from __doc__
        """ QProcess.setReadChannelMode(QProcess.ProcessChannelMode) """
        pass

    def setStandardErrorFile(self, p_str, QIODevice_OpenMode_mode=None): # real signature unknown; restored from __doc__
        """ QProcess.setStandardErrorFile(str, QIODevice.OpenMode mode=QIODevice.Truncate) """
        pass

    def setStandardInputFile(self, p_str): # real signature unknown; restored from __doc__
        """ QProcess.setStandardInputFile(str) """
        pass

    def setStandardOutputFile(self, p_str, QIODevice_OpenMode_mode=None): # real signature unknown; restored from __doc__
        """ QProcess.setStandardOutputFile(str, QIODevice.OpenMode mode=QIODevice.Truncate) """
        pass

    def setStandardOutputProcess(self, QProcess): # real signature unknown; restored from __doc__
        """ QProcess.setStandardOutputProcess(QProcess) """
        pass

    def setupChildProcess(self): # real signature unknown; restored from __doc__
        """ QProcess.setupChildProcess() """
        pass

    def setWorkingDirectory(self, p_str): # real signature unknown; restored from __doc__
        """ QProcess.setWorkingDirectory(str) """
        pass

    def start(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QProcess.start(str, list-of-str, QIODevice.OpenMode mode=QIODevice.ReadWrite)
        QProcess.start(str, QIODevice.OpenMode mode=QIODevice.ReadWrite)
        """
        pass

    def startDetached(self, p_str, list_of_str=None, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QProcess.startDetached(str, list-of-str, str) -> (bool, int)
        QProcess.startDetached(str, list-of-str) -> bool
        QProcess.startDetached(str) -> bool
        """
        return False

    def started(self, *args, **kwargs): # real signature unknown
        """ QProcess.started [signal] """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QProcess.state() -> QProcess.ProcessState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QProcess.stateChanged[QProcess.ProcessState] [signal] """
        pass

    def systemEnvironment(self): # real signature unknown; restored from __doc__
        """ QProcess.systemEnvironment() -> list-of-str """
        pass

    def terminate(self): # real signature unknown; restored from __doc__
        """ QProcess.terminate() """
        pass

    def waitForBytesWritten(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QProcess.waitForBytesWritten(int msecs=30000) -> bool """
        return False

    def waitForFinished(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QProcess.waitForFinished(int msecs=30000) -> bool """
        return False

    def waitForReadyRead(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QProcess.waitForReadyRead(int msecs=30000) -> bool """
        return False

    def waitForStarted(self, int_msecs=30000): # real signature unknown; restored from __doc__
        """ QProcess.waitForStarted(int msecs=30000) -> bool """
        return False

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ QProcess.workingDirectory() -> str """
        return ""

    def writeData(self, p_str): # real signature unknown; restored from __doc__
        """ QProcess.writeData(str) -> int """
        return 0

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Crashed = 1
    CrashExit = 1
    ExitStatus = None # (!) real value is ''
    FailedToStart = 0
    ForwardedChannels = 2
    MergedChannels = 1
    NormalExit = 0
    NotRunning = 0
    ProcessChannel = None # (!) real value is ''
    ProcessChannelMode = None # (!) real value is ''
    ProcessError = None # (!) real value is ''
    ProcessState = None # (!) real value is ''
    ReadError = 3
    Running = 2
    SeparateChannels = 0
    StandardError = 1
    StandardOutput = 0
    Starting = 1
    Timedout = 2
    UnknownError = 5
    WriteError = 4


