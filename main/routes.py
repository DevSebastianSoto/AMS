import os
from main import app
import main.utils as utils
from main.forms import ContactForm
from flask import redirect, render_template, flash, request, url_for

@app.context_processor
def inject_dict_for_all_templates():
    nav_info = utils.readJson(os.path.join('main', 'content', 'nav.json'))
    return dict(nav_bar=nav_info)


@app.route('/')
def index():
    clients_info = utils.readJson(os.path.join('main', 'content', 'clients.json'))
    carousel_info = utils.readJson(os.path.join('main', 'content', 'index-carousel.json'))
    return render_template('views/index/index.html', index=True,
                           clients=clients_info,carousel_info=carousel_info)


@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('views/about/about.html', dir_title='Sobre \
                           Nosotros')


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()
    if form.validate_on_submit():
        name = f'{form.first_name.data} {form.last_name.data}'
        flash(f'{name}, gracias por contactarnos! Pronto le responderemos',
              'success')
        utils.sendMail(name, form.email.data,
                       form.subject.data, form.message.data)
        return redirect(url_for('index'))

    return render_template('views/contact/contact.html', dir_title='Contact',
                           form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/404.html', dir_title='Not Found'), 404



