import os
import utils
import jinja2
from flask import Flask, render_template, flash, redirect, url_for
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "bda15c5adda26a64d0015dec0788894e"

template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)


@app.context_processor
def inject_dict_for_all_templates():
    nav_info = utils.readJson(os.path.join('content', 'nav.json'))
    return dict(nav_bar=nav_info)


@app.route('/')
def index():
    clients_info = utils.readJson(os.path.join('content', 'clients.json'))
    return render_template('views/index/index.html', index=True, clients=clients_info)


@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('views/about/about.html', dir_title='Sobre Nosotros')


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()
    if form.validate_on_submit():
        name = f'{form.first_name.data} {form.last_name.data}'
        flash(f'{name}, gracias por contactarnos, pronto le responderemos!', 'success')
        utils.sendMail(name, form.email.data,
                       form.subject.data, form.message.data)
        return redirect(url_for('index'))

    return render_template('views/contact/contact.html', dir_title='Contact', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/404.html', dir_title='Not Found'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
