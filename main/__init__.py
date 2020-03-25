import os
import jinja2
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "bda15c5adda26a64d0015dec0788894e"

template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

from main import routes
