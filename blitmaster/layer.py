
from blitmaster.setlayer import SetLayer
from blitmaster.resizelayer import ResizeLayer
from blitmaster.renderlayer import RenderLayer


class Layer(SetLayer, ResizeLayer, RenderLayer):

    def __init__(self, name, dims):

        SetLayer.__init__(self, name, dims)
        ResizeLayer.__init__(self, name, dims)
        RenderLayer.__init__(self, name, dims)
        pass

L = Layer("L", (3, 5))
print L.relative_1d_coord(2, 2)
print L.registry
print Layer.get("L")
