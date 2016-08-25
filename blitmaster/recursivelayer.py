
import abc
from collections import OrderedDict

from blitmaster import registeredlayer


class RecursiveLayer(registeredlayer.RegisteredLayer):

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, dims, sublayers=None):
        self.layers = OrderedDict()  # string -> (x, y, layer) (ORDER MATTERS!)

        if sublayers is None:
            sublayers = []

        for (x, y, each) in sublayers:
            self.add_layer(x, y, each)

        registeredlayer.RegisteredLayer.__init__(self, name, dims)

    def get_layer(self, name):
        return self.layers[name]

    def add_layer(self, x, y, layer):
        self.layers[layer.name] = (x, y, layer)

    def delete_layer(self, name):
        del self.layers[name]

    def move_layer(self, x, y, name):
        (_, _, layer) = self.get_layer(name)
        if self.restrict:
            if self.layer_out_of_bounds(x, y, layer):
                return False
        self.delete_layer(name)
        self.add_layer(x, y, layer)
        return True

    def move_layer_inc(self, x, y, name):
        (sx, sy, layer) = self.get_layer(name)
        x = sx + x
        y = sy + y
        return self.move_layer(x, y, name)
