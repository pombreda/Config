# encoding: utf-8
# module samba.dcerpc.dnsserver
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/dnsserver.so
# by generator 1.135
""" dnsserver DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class DNS_RPC_UTF8_STRING_LIST(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    dwCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pszStrings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



