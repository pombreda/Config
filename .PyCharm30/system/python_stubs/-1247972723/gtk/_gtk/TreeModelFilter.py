# encoding: utf-8
# module gtk._gtk
# from /usr/lib/python2.7/dist-packages/gtk-2.0/gtk/_gtk.so
# by generator 1.135
# no doc

# imports
import atk as __atk
import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject


from TreeModel import TreeModel

from TreeDragSource import TreeDragSource

class TreeModelFilter(__gobject__gobject.GObject, TreeModel, TreeDragSource):
    """
    Object GtkTreeModelFilter
    
    Properties from GtkTreeModelFilter:
      child-model -> GtkTreeModel: The child model
        The model for the filtermodel to filter
      virtual-root -> GtkTreePath: The virtual root
        The virtual root (relative to the child model) for this filtermodel
    
    Signals from GtkTreeModel:
      row-changed (GtkTreePath, GtkTreeIter)
      row-inserted (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)
    
    Signals from GObject:
      notify (GParam)
    """
    def clear_cache(self, *args, **kwargs): # real signature unknown
        pass

    def convert_child_iter_to_iter(self, *args, **kwargs): # real signature unknown
        pass

    def convert_child_path_to_path(self, *args, **kwargs): # real signature unknown
        pass

    def convert_iter_to_child_iter(self, *args, **kwargs): # real signature unknown
        pass

    def convert_path_to_child_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_model(self, *args, **kwargs): # real signature unknown
        pass

    def refilter(self, *args, **kwargs): # real signature unknown
        pass

    def set_modify_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible_column(self, *args, **kwargs): # real signature unknown
        pass

    def set_visible_func(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    __gtype__ = None # (!) real value is ''


