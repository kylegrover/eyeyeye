"""Check an isomorph and print its copy map.

  python isomorph.py E3 64 E5 74 25      E3 cells 64.. against E5 cells 74.., 25 cells

Two stretches are isomorphic if one consistent one-to-one map takes each symbol of the first to the
symbol in the same place in the second. Prints the map, marking symbols seen at two or more cells
(those need only assumption R; the rest need W).
"""
import sys
from eyes import MSGS


def copy_map(a, i, b, j, n):
    x, y = MSGS[a][i:i + n], MSGS[b][j:j + n]
    fwd, back, seen = {}, {}, {}
    for k, (s, t) in enumerate(zip(x, y)):
        if fwd.setdefault(s, t) != t or back.setdefault(t, s) != s:
            return None, f'not isomorphic: cell {i + k} of {a} ({s}) breaks the map'
        seen.setdefault(s, []).append(i + k)
    return fwd, seen


if __name__ == '__main__':
    a, i, b, j, n = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
    fwd, seen = copy_map(a, i, b, j, n)
    if fwd is None:
        sys.exit(seen)
    for s in sorted(fwd, key=lambda s: seen[s][0]):
        cells = seen[s]
        print(f'{s:2d} -> {fwd[s]:2d}   at {a} cells {cells}' + ('   (repeat)' if len(cells) > 1 else ''))
