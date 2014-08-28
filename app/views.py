from config import apps, site_mappings
from requests import get
from flask import  render_template, jsonify
from app import app

@app.route('/')
def index():
    return render_template('index.html', site_mappings = site_mappings)

@app.route('/version/<site>')
def version(site):
    new_dict = {}
    if apps[site]:
        new_dict[site] = {}
        for server in apps[site]:
            new_dict[site][server] = get('http://' + server + '/ops/version.json').json()['version']
        return render_template('modal_view.html', info=new_dict, site=site_mappings[site])
    else:
        return "Site not found"
