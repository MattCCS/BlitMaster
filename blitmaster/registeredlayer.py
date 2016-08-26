
import abc

from blitmaster import baselayer


class RegisteredLayer(baselayer.BaseLayer):

    __metaclass__ = abc.ABCMeta

    registry = {}

    def __init__(self, name, dims):
        if name in RegisteredLayer.registry:
            raise RuntimeError("Layer name {} already exists!".format(repr(name)))

        baselayer.BaseLayer.__init__(self, name, dims)

        RegisteredLayer.registry[name] = self

    @staticmethod
    def get(name):
        return RegisteredLayer.registry[name]

    @staticmethod
    def delete(name):
        del RegisteredLayer.registry[name]
