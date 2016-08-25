
import abc


class BaseLayer(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, dims):

        self.name = name
        self.w, self.h = dims

        # self.restrict = restrict
        # self.wrap = wrap
        self.points = {}

    def size(self):
        return (self.w, self.h)

    def relative_1d_coord(self, x, y):
        return self.w * y + x

    def relative_2d_coord(self, i):
        (y, x) = divmod(i, self.w)
        return (x, y)

    def out_of_bounds(self, x, y):
        return not (0 <= x < self.w) or not (0 <= y < self.h)

    def layer_out_of_bounds(self, x, y, layer):
        (w, h) = layer.size()
        xmax = x + w - 1
        ymax = y + h - 1
        return any([
            self.out_of_bounds(x, y),
            self.out_of_bounds(xmax, y),
            self.out_of_bounds(x, ymax),
            self.out_of_bounds(xmax, ymax),
        ])

    ####################################
    # iterating over lines
    def yield_rows_with_none(self):
        for y in range(self.h):
            yield (self.points.get((x, y), None) for x in range(self.w))

    def items(self):
        # if wrap:
        #     for ((x,y),p) in self.points.iteritems():
        #         (x,y) = self.convert_to_2d(self.convert_to_1d(x,y))
        #         if self.out_of_bounds(x,y):
        #             continue # because iteritems has no order, we can't break :/
        #         yield (x, y, p)
        # else:
        for ((x, y), p) in self.points.items():
            yield (x, y, p)
