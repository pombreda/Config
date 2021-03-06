# encoding: utf-8
# module _symtable
# from (built-in)
# by generator 1.135
# no doc
# no imports

# Variables with simple values

CELL = 5

DEF_BOUND = 134
DEF_FREE = 32

DEF_FREE_CLASS = 64

DEF_GLOBAL = 1
DEF_IMPORT = 128
DEF_LOCAL = 2
DEF_PARAM = 4

FREE = 4

GLOBAL_EXPLICIT = 2
GLOBAL_IMPLICIT = 3

LOCAL = 1

OPT_IMPORT_STAR = 1

OPT_TOPLEVEL = 2

SCOPE_MASK = 15
SCOPE_OFF = 11

TYPE_CLASS = 1
TYPE_FUNCTION = 0
TYPE_MODULE = 2

USE = 16

# functions

def symtable(*args, **kwargs): # real signature unknown
    """ Return symbol and scope dictionaries used internally by compiler. """
    pass

# classes

from .object import object

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """ Load a built-in module. """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

__spec__ = None # (!) real value is ''

