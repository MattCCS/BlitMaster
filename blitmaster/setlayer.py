
import abc

from . import baselayer


class SetLayer(baselayer.BaseLayer):

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, dims):
        baselayer.BaseLayer.__init__(self, name, dims)
        self.points = {}

    def reset(self):
        self.points = {}

    ####################################
    # individual points
    def set(self, x, y, char, meta=None):
        if type(char) is not int:
            assert len(char) == 1
        self.points[(x, y)] = (char, meta)

    def unset(self, x, y):
        try:
            del self.points[(x, y)]
        except KeyError:
            pass

    ####################################
    # setting ranges
    def setlines(self, x, y, lines, meta=None):
        """
        For convenience, to allow blocks of text to be pre-written and split.
        """
        for (i, line) in enumerate(lines):
            self.setrange(x, y + i, line, meta=meta)

    def setrange(self, x, y, it, meta=None):
        for (i, c) in enumerate(it, x):
            # if not allow_beyond:
            #     if self.out_of_bounds(i, y):
            #         break
            self.set(i, y, c, meta=meta)

    def setrange_paired(self, x, y, it):
        for (i, (c, meta)) in enumerate(it, x):
            # if not allow_beyond:
            #     if self.out_of_bounds(i, y):
            #         break
            self.set(i, y, c, meta=meta)

    def fill(self, c, x=0, y=0, w=0, h=0, meta=None):
        if not w:
            w = self.w
        if not h:
            h = self.h

        lines = (c * w for _ in xrange(h))

        self.setlines(x, y, lines, meta=meta)
