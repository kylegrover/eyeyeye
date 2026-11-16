// Eye-glyph page background: draws one seamless tile on a canvas and tiles it with CSS.
// Geometry from the in-game eye walls: eye 11x7 px, horizontal pitch 12, rows 7 px apart,
// odd rows shifted 6 px. The pupil is a 5-px plus looking centre, up, right, down or left.
// Usage: <script src="eyes-bg.js" data-mode="random|pattern"></script>; colour from CSS --eye-ink.
(function () {
  const SCALE = 4;                                    // sharp nearest-neighbour zoom
  const OUTLINE = [[0, [4, 5, 6]], [1, [2, 3, 7, 8]], [2, [1, 9]], [3, [0, 10]],
                   [4, [1, 9]], [5, [2, 3, 7, 8]], [6, [4, 5, 6]]];
  const LOOKS = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]];
  const PLUS = [[0, -1], [-1, 0], [0, 0], [1, 0], [0, 1]];

  function draw(mode, ink) {
    // random: a large tile, so the repeat is hard to spot; pattern: 5 eyes wide, looks cycle diagonally
    const cols = mode === 'pattern' ? 5 : 20, rowPairs = mode === 'pattern' ? 1 : 6;
    const W = cols * 12, H = rowPairs * 14;
    const c = document.createElement('canvas');
    c.width = W * SCALE; c.height = H * SCALE;
    const g = c.getContext('2d');
    g.fillStyle = ink;
    const px = (x, y) => g.fillRect(((x % W) + W) % W * SCALE, ((y % H) + H) % H * SCALE, SCALE, SCALE);
    for (let row = 0; row < rowPairs * 2; row++) {
      for (let col = 0; col < cols; col++) {
        const x0 = col * 12 + (row % 2 ? 6 : 0), y0 = row * 7;
        for (const [dy, xs] of OUTLINE) for (const dx of xs) px(x0 + dx, y0 + dy);
        const look = mode === 'pattern' ? (col + 2 * row) % 5 : Math.floor(Math.random() * 5);
        const [lx, ly] = LOOKS[look];
        for (const [dx, dy] of PLUS) px(x0 + 5 + lx + dx, y0 + 3 + ly + dy);
      }
    }
    // data: URL, not blob:, so a Content-Security-Policy with img-src 'self' data: allows it
    const s = document.body.style;
    s.backgroundImage = `url(${c.toDataURL('image/png')})`;
    s.backgroundSize = `${W * SCALE}px ${H * SCALE}px`;
    s.imageRendering = 'pixelated';
  }

  window.drawEyes = draw;
  const tag = document.currentScript;
  const ink = getComputedStyle(document.documentElement).getPropertyValue('--eye-ink').trim() || '#e8e5dc';
  draw((tag && tag.dataset.mode) || 'random', ink);
})();
