
import abc

from blitmaster import recursivelayer


class SetLayer(recursivelayer.RecursiveLayer):

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, dims):
        recursivelayer.RecursiveLayer.__init__(self, name, dims)

    def reset(self):
        self.points = {}

    def reset_recursive(self):
        self.reset()
        for (_, _, layer) in list(self.layers.values()):
            layer.reset_recursive()

    ####################################
    # individual points
    def set(self, x, y, char, color=None, mode=1):
        if type(char) is not int:
            assert len(char) == 1
        self.points[(x, y)] = (
            char,
            color if color is not None else DEFAULT_COLOR,
            mode if mode is not None else DEFAULT_MODE,
        )

    def unset(self, x, y):
        try:
            del self.points[(x, y)]
        except KeyError:
            pass

    ####################################
    # setting ranges
    def setlines(self, x, y, lines, color=None, mode=1):
        """
        For convenience, to allow blocks of text to be pre-written and split.
        """
        for (i, line) in enumerate(lines):
            self.setrange(x, y + i, line, color=color, mode=mode)

    def setrange(self, x, y, it, color=None, mode=1):
        for (i, c) in enumerate(it, x):
            # if not allow_beyond:
            #     if self.out_of_bounds(i, y):
            #         break
            self.set(i, y, c, color=color, mode=mode)

    ####################################
    # pre-paired ranges
    def setrange_paired(self, x, y, it):
        for (i, (c, color, mode)) in enumerate(it, x):
            # if not allow_beyond:
            #     if self.out_of_bounds(i, y):
            #         break
            self.set(i, y, c, color=color, mode=mode)
