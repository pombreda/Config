# encoding: utf-8
# module samba.dcerpc.srvsvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/srvsvc.so
# by generator 1.135
""" srvsvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class NetConnInfo1(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    conn_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    conn_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    conn_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_users = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    share = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



