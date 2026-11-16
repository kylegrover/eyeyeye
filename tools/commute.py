"""Two copy maps from one E3 passage do not commute (needs W).

E3 64-88 matches E5 ten cells later (map A) and W4 twelve cells later (map B). Under W, these
are plaintext copies. The witness excludes mechanisms requiring both copy maps to be rotations of
one fixed ring, since rotations commute. That property must be established for the mechanism;
it is not automatic for every position-dependent or additive cipher.
"""
from isomorph import copy_map

A, _ = copy_map('E3', 64, 'E5', 74, 25)
B, _ = copy_map('E3', 64, 'W4', 76, 25)
s = 58
print(f'A then B: {s} -> {A[s]} -> {B[A[s]]}')
print(f'B then A: {s} -> {B[s]} -> {A[B[s]]}')
