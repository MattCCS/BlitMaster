
import abc

from . import recursivelayer


class RenderLayer(recursivelayer.RecursiveLayer):

    __metaclass__ = abc.ABCMeta

    def __init__(self, dims, name=None, sublayers=None):
        recursivelayer.RecursiveLayer.__init__(self, dims, name=name, sublayers=sublayers)

    ####################################
    # rendering
    def self_items(self):
        for ((x, y), p) in self.points.items():
            yield (x, y, p)

    def render_dict(self):
        points = {}

        # render sub-layers, in order
        for (ox, oy, layer) in list(self.layers.values()):
            for (x, y, point) in layer.render_to(ox, oy):
                if self.out_of_bounds(x, y):
                    continue
                points[(x, y)] = point

        # render self on top
        for (x, y, point) in self.self_items():
            # if self.wrap:  # TODO: wrapping?
            #     (x, y) = self.convert_to_2d(self.convert_to_1d(x, y))
            if self.out_of_bounds(x, y):
                continue
            points[(x, y)] = point

        return points

    def items(self, wrap=None):
        # if wrap:
        #     for ((x,y),p) in self.points.iteritems():
        #         (x,y) = self.convert_to_2d(self.convert_to_1d(x,y))
        #         if self.out_of_bounds(x,y):
        #             continue # because iteritems has no order, we can't break :/
        #         yield (x, y, p)
        # else:
        for ((x, y), p) in self.render_dict().items():
            yield (x, y, p)

    def render_to(self, ox, oy, wrap=None):
        for (x, y, point) in self.items(wrap=wrap):
            yield (x + ox, y + oy, point)

    ####################################
    # debug functions
    def debug_layers(self):
        for (name, (x, y, layer)) in list(self.layers.items()):
            print(("{}: pos={}/{} dims={}".format(name, x, y, layer.size())))

    def yield_rows_with_none(self):
        points = self.render_dict()
        for y in range(self.h):
            yield (points.get((x, y), None) for x in range(self.w))

    def debug_render_rows(self, joiner=''):
        for row in self.yield_rows_with_none():
            yield joiner.join((p[0] if p is not None else ' ') for p in row)

    def debug_render(self, joiner=''):
        return '\n'.join(self.debug_render_rows(joiner=joiner))
