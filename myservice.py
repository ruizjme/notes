import boto3
from flask import Flask, jsonify, render_template, request, session
import flask_misaka
import re
import glob
import requests
import boto3

app = Flask(__name__)
BUCKET_NAME = 'notes-static-content'
S3_URL = "https://s3-ap-southeast-2.amazonaws.com/notes-static-content"


def list_notes():
    """List all available notes with their respective URL"""
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    file_list = []
    for obj in bucket.objects.filter(Prefix="content/"):
         file_list.append(obj.key)
    notes_dict = { ''.join(i.split('/')[-1].split('.')[:-1]).replace('_',' ').title() : ''.join(i.split('/')[-1].split('.')[:-1]) for i in file_list }
    return notes_dict

@app.route("/")
def index():
    return "Index page! Coming soon."

@app.route("/notes/", methods=["GET"])
def notes_menu():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    file_list = []
    for obj in bucket.objects.filter(Prefix="content/"):
         file_list.append(obj.key)
    notes_dict = { ''.join(i.split('/')[-1].split('.')[:-1]).replace('_',' ').title() : ''.join(i.split('/')[-1].split('.')[:-1]) for i in file_list }
    notes_title = "Notes"
    return render_template('notes_menu.html', S3_URL=S3_URL, **locals())

# returns HTML from given template
@app.route("/notes/<string:notes_title>/", methods=["GET"])
def notes(notes_title):
    try:
        r = requests.get('{}/content/{}.md'.format(S3_URL, notes_title))
        if r.status_code == 200:
            md = r.text
            # images are in static/img/
            md = re.sub(r'!\[\]\(assets/', '![]({}/static/img/'.format(S3_URL), md)
            # parse markdown into html
            md = flask_misaka.markdown( md,
                                        space_headers=True,
                                        fenced_code=True,
                                        math=True,
                                        math_explicit=True,
                                        footnotes=False,
                                        smartypants=False,
                                        tables=True)
        else:
            md = r.text

    except Exception as e:
        # output the exception to be rendered
        md = e

    notes_title = notes_title.replace("_"," ").title()
    notes_dict = list_notes()

    return render_template('notes_page.html', S3_URL=S3_URL, **locals())
