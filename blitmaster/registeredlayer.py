
import abc

from . import baselayer


class RegisteredLayer(baselayer.BaseLayer):

    __metaclass__ = abc.ABCMeta

    registry = {}

    def __init__(self, dims, name=None):
        baselayer.BaseLayer.__init__(self, dims)
        
        if name is not None:
            if name in RegisteredLayer.registry:
                raise RuntimeError("Layer name {} already exists!".format(repr(name)))
            RegisteredLayer.registry[name] = self

    @staticmethod
    def get(name):
        return RegisteredLayer.registry[name]

    @staticmethod
    def delete(name):
        del RegisteredLayer.registry[name]
