# encoding: utf-8
# module samba.dcerpc.samr
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/samr.so
# by generator 1.135
""" samr DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class ValidatePasswordReq3(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    account = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clear_lockout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwd_must_change_at_next_logon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



