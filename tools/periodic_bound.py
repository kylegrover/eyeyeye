"""Periodic substitution: a counting bound that needs no assumption about isomorphs.

If the key repeats with period p and starts again with each message, every cell at position i (counted
from cell 1, the first symbol after cell 0) is encrypted with alphabet number i mod p. One alphabet maps
A letters to at most A symbols. So if some residue class mod p shows more than A distinct symbols, no
key of period p and no plaintext over A letters can produce the messages.

  python periodic_bound.py            prints, for p = 1..20, the most distinct symbols in one class
"""
from eyes import MSGS

BODIES = [m[1:] for m in MSGS.values()]


def most_in_one_class(p):
    classes = [set() for _ in range(p)]
    for body in BODIES:
        for i, s in enumerate(body):
            classes[i % p].add(s)
    return max(len(c) for c in classes)


if __name__ == '__main__':
    for p in range(1, 21):
        print(f'period {p:2d}: some position shows {most_in_one_class(p)} different symbols')
    print('every period 1-10 shows at least', min(most_in_one_class(p) for p in range(1, 11)),
          'so all are excluded for any alphabet of 58 letters or fewer')
