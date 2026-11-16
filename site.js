// Hover links inside exhibits (built by tools/build_site.py). Everything here is an enhancement:
// the pages read the same without it.
//   rows:     a cell lights its column in every row; a repeated cell also lights the rest of its
//             repeat (data-k) in every row, and the arc that joins them.
//   message:  a symbol lights its other occurrences in the same message (data-k is the symbol).
(function () {
  for (const pre of document.querySelectorAll('pre.exhibit')) {
    const lit = [];
    const clear = () => { for (const el of lit.splice(0)) el.classList.remove('lit'); };
    const light = sel => { for (const el of pre.querySelectorAll(sel)) { el.classList.add('lit'); lit.push(el); } };
    pre.addEventListener('mouseover', e => {
      const cell = e.target.closest('[data-i], [data-k]');
      clear();
      if (!cell || cell.tagName === 'path') return;
      if (cell.dataset.k !== undefined) light(`[data-k="${cell.dataset.k}"]`);
      if (cell.dataset.i !== undefined) light(`[data-i="${cell.dataset.i}"]`);
    });
    pre.addEventListener('mouseleave', clear);
  }
})();
