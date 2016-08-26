
from blitmaster import registeredlayer
from blitmaster import renderlayer
from blitmaster import resizelayer


class Layer(registeredlayer.RegisteredLayer,
            renderlayer.RenderLayer,
            resizelayer.ResizeLayer):

    def __init__(self, name, dims, sublayers=None):

        registeredlayer.RegisteredLayer.__init__(self, name, dims)
        renderlayer.RenderLayer.__init__(self, name, dims, sublayers=sublayers)
        resizelayer.ResizeLayer.__init__(self, name, dims)
