
import abc


class BaseLayer(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, dims):
        self.w, self.h = dims

        # self.restrict = restrict
        # self.wrap = wrap

    def size(self):
        return (self.w, self.h)

    def relative_1d_coord(self, x, y):
        return self.w * y + x

    def relative_2d_coord(self, i):
        (y, x) = divmod(i, self.w)
        return (x, y)

    def out_of_bounds(self, x, y):
        return not (0 <= x < self.w) or not (0 <= y < self.h)
