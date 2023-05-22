import os

import jinja2
from flask import Flask, flash, redirect, render_template, url_for

app = Flask(__name__)


@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN,www.facebook.com"
    return response


app.config['SECRET_KEY'] = "bda15c5adda26a64d0015dec0788894e"

template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

from main import routes

