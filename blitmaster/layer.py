
from blitmaster import recursivelayer
from blitmaster import registeredlayer
from blitmaster import renderlayer
from blitmaster import resizelayer


class Layer(recursivelayer.RecursiveLayer,
            registeredlayer.RegisteredLayer,
            renderlayer.RenderLayer,
            resizelayer.ResizeLayer):

    def __init__(self, name, dims, sublayers=None):

        recursivelayer.RecursiveLayer.__init__(self, name, dims, sublayers=sublayers)
        registeredlayer.RegisteredLayer.__init__(self, name, dims)
        renderlayer.RenderLayer.__init__(self, name, dims)
        resizelayer.ResizeLayer.__init__(self, name, dims)
