# Notes

Automation to render my university notes as a webpage.

## Dependencies

Notes written in `markdown` using `atom`:

* [markdown-preview-plus](https://atom.io/packages/markdown-preview-plus)
* [atom-image-assistant](https://atom.io/packages/markdown-image-assistant)

Stored in `AWS S3` and rendered with `python` in `AWS Lambda`:

* Deployed with [Zappa](https://www.zappa.io/)

Python packages:

* [Flask-Misaka](https://flask-misaka.readthedocs.io/en/latest/)

Web libraries:

* [MathJax](https://www.mathjax.org)
* [HighlightJS](https://highlightjs.org/usage/)
* [TocBot](https://tscanlin.github.io/tocbot/)

Example [here](https://nnconv4jg1.execute-api.ap-southeast-2.amazonaws.com/dev/notes/machine_dynamics/) :point_left:
