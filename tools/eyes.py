"""Load the nine eye messages from eyes.json (same folder, or one level up on the site).

Each message has `rows` (the raw eye directions, one string of digits 0-4 per row of eyes: centre, up,
right, down, left) and `trigrams` (the symbols 0-82). Cell 0 is a message's first symbol.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
_path = next(p for p in (HERE / 'eyes.json', HERE.parent / 'eyes.json') if p.exists())
DATA = json.loads(_path.read_text(encoding='utf-8'))
NAMES = [m['name'] for m in DATA]
MSGS = dict(zip(NAMES, (m['trigrams'] for m in DATA)))


def decode(rows):
    """Rebuild the symbols from the eye rows. Rows go in pairs; each pair interlocks into triangles.
    Up triangle: top-left, top-right, bottom. Down triangle: bottom-right, bottom-left, top. Base 5."""
    out = []
    for p in range(0, len(rows), 2):
        top, bot = rows[p], rows[p + 1]
        for x in range(0, len(top), 3):
            if x + 1 < len(top) and x < len(bot):
                out.append(int(top[x]) * 25 + int(top[x + 1]) * 5 + int(bot[x]))
            if x + 2 < len(bot) and x + 2 < len(top):
                out.append(int(bot[x + 2]) * 25 + int(bot[x + 1]) * 5 + int(top[x + 2]))
    return out


if __name__ == '__main__':
    for m in DATA:
        assert decode(m['rows']) == m['trigrams'], m['name']
    print('all nine messages decode from their eye rows')
