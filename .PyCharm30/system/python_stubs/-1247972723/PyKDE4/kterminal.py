# encoding: utf-8
# module PyKDE4.kterminal
# from /usr/lib/python2.7/dist-packages/PyKDE4/kterminal.so
# by generator 1.135
# no doc
# no imports

# no functions
# classes

class KTerminal(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def terminalInterface(self, *args, **kwargs): # real signature unknown
        pass

    def terminalInterfaceV2(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class TerminalInterface(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def sendInput(self, *args, **kwargs): # real signature unknown
        pass

    def showShellInDir(self, *args, **kwargs): # real signature unknown
        pass

    def startProgram(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



from TerminalInterface import TerminalInterface

class TerminalInterfaceV2(TerminalInterface):
    # no doc
    def foregroundProcessId(self, *args, **kwargs): # real signature unknown
        pass

    def foregroundProcessName(self, *args, **kwargs): # real signature unknown
        pass

    def terminalProcessId(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


