# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.135
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class QuerySitesByCostRequest1(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_req = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_from = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



