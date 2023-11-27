import math

SQRT2 = math.sqrt(2)

def backtrace(node):
    path = [(node.x, node.y)]
    while node.parent:
        node = node.parent
        path.append((node.x, node.y))
    path.reverse()
    return path

def bi_backtrace(node_a, node_b):
    path_a = backtrace(node_a)
    path_b = backtrace(node_b)
    path_b.reverse()
    return path_a + path_b
