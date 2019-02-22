# Notes

Automation to render my university notes as a webpage.

## Check it out

:point_right: [here!](https://notes.ruizj.me/) :point_left:

## Dependencies

Notes written in `markdown` using the `atom` text editor:

* [atom](https://atom.io/)
* [markdown-preview-plus](https://atom.io/packages/markdown-preview-plus)
* [atom-image-assistant](https://atom.io/packages/markdown-image-assistant)

Markdown is stored in `AWS S3` and rendered with `python` in `AWS Lambda`. Deployed with [Zappa](https://www.zappa.io/).

Python packages:

* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
* [flask](http://flask.pocoo.org/)
* [flask_misaka](https://flask-misaka.readthedocs.io/en/latest/)

Web libraries:

* [MathJax](https://www.mathjax.org)
* [HighlightJS](https://highlightjs.org/usage/)
* [TocBot](https://tscanlin.github.io/tocbot/)

Sources of inspiration:

* [Infra tutorial](https://medium.freecodecamp.org/how-to-create-a-serverless-service-in-15-minutes-b63af8c892e5)
* [Flask tutorial](https://pythonspot.com/flask-web-app-with-python/)

## Usage

I have set an alias `upnotes` which basically calls `s3_upload.py` to upload all `.md` and image files to the S3 bucket that holds the static content.

I may need to change the behaviour of this down the line if there are a lot of images. Potentially check for existing images in the bucket and only upload any missing ones. Maybe diff existing ones?

Running `upnotes css` uploads the custom `.css` files for when I make changes to the styling.

If any changes are made to the `.html` templates, the app has to be re-deployed via `zappa update dev`.
