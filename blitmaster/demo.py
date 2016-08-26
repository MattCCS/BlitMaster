
from .layer import Layer

L = Layer("L", (8, 5))
print L.relative_1d_coord(2, 2)
print L.registry
print Layer.get("L")
L.fill('.')
L.fill('*', 1, 1, 5, 3)
L.set(2, 2, 'X')
L.setrange(4, 3, 'Foo!')
print L.debug_render(' ')
