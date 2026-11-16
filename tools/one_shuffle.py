"""K = 1 is impossible: three isomorphs give incompatible powers of one shuffle (needs R).

Assume a common starting deck/phase in every message, fixed letter read positions, one fixed shuffle
per step, and cell 0 outside encryption. A copy at shift d sends each symbol x to Q^d(x) for one fixed
permutation Q of the symbols. R supplies equal plaintext across copies at the repeat-supported cells.
Each fact below is seen at two cells of its isomorph.
"""
from isomorph import copy_map

facts = [('W1', 70, 'E2', 80, 8, 68, 10),   # W1 -> E2, shift 10: 68 -> 41
         ('E4', 54, 'E5', 55, 9, 68, 1),    # E4 -> E5, shift 1:  68 -> 30
         ('E3', 81, 'E4', 90, 5, 30, 9)]    # E3 -> E4, shift 9:  30 -> 26
got = {}
for a, i, b, j, n, x, d in facts:
    fwd, seen = copy_map(a, i, b, j, n)
    assert fwd is not None and len(seen[x]) >= 2
    got[d] = (x, fwd[x])
    print(f'{a} -> {b}, shift {d:2d}: Q^{d}({x}) = {fwd[x]}  (cells {seen[x]})')
q1 = got[1][1]
assert got[9][0] == q1
print(f'Q^10(68) = {got[10][1]}, but Q^10(68) = Q^9(Q(68)) = Q^9({q1}) = {got[9][1]}: contradiction, so K >= 2')
