
from . import recursivelayer
from . import registeredlayer
from . import renderlayer
from . import resizelayer


class Layer(registeredlayer.RegisteredLayer,
            renderlayer.RenderLayer,
            resizelayer.ResizeLayer):

    def __init__(self, name, dims, sublayers=None):

        registeredlayer.RegisteredLayer.__init__(self, name, dims)
        renderlayer.RenderLayer.__init__(self, name, dims, sublayers=sublayers)
        resizelayer.ResizeLayer.__init__(self, name, dims)
