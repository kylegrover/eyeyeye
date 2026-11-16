# eyeyeye

Static site with research notes on the Noita eye messages: <https://eyeyeye.ufffd.com>.

Plain HTML, CSS and one small script; no build step. Serve the folder as-is.

`tools/` holds small Python scripts (standard library only) that reproduce calculations on the
site; put `eyes.json` next to them and run, for example, `python one_shuffle.py`.
`evidence/` holds the recorded outputs the pages link to.

The pages are generated from a separate working repository; edits here may be overwritten.
