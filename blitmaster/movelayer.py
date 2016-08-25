
import abc

from blitmaster import recursivelayer


class MoveLayer(recursivelayer.RecursiveLayer):

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, dims):
        recursivelayer.RecursiveLayer.__init__(self, name, dims)
