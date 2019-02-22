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

Sources:

* [Infra tutorial](https://medium.freecodecamp.org/how-to-create-a-serverless-service-in-15-minutes-b63af8c892e5)
* [Code tutorial](https://pythonspot.com/flask-web-app-with-python/)

Example [here](https://notes.ruizj.me/) :point_left:
