# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsblobs.so
# by generator 1.135
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class supplementalCredentialsSubBlob(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    num_packages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    packages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


