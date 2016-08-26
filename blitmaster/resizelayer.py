
import abc

from . import baselayer


class ResizeLayer(baselayer.BaseLayer):

    # TODO: might have to respect "restrict" effects?

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, dims):
        baselayer.BaseLayer.__init__(self, name, dims)

    def resize_diff(self, dw=0, dh=0):
        (w, h) = self.size()
        w += dw
        h += dh
        self.resize(w, h)

    def resize(self, w=0, h=0):
        (ow, oh) = self.size()

        self.w = w if w > 0 else ow
        self.h = h if h > 0 else oh

        self.on_resize()

    def on_resize(self):
        """Called on resize event.  Use for things like drawing borders."""
        pass
