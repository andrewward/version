from config import apps_template, generate_mappings, generate_hosts
from requests import get
from flask import  render_template
from app import app

apps = generate_hosts(apps_template)
site_mappings = generate_mappings(apps_template)
@app.route('/')
def index():
    return render_template('index.html', site_mappings = site_mappings)

@app.route('/version/<site>')
def version(site):
    new_dict = {}
    if apps[site]:
        new_dict[site] = {}
        new_dict[site]['atl'] = {}
        new_dict[site]['lax'] = {}
        for server in apps[site]['atl']:
            new_dict[site]['atl'][server] = get('http://' + server + '/ops/version.json').json()['version']
        for server in apps[site]['lax']:
            if apps[site]['lax'][0] == 'none':
               new_dict[site]['lax'][server] = 'none'
            else:
               new_dict[site]['lax'][server] = get('http://' + server + '/ops/version.json').json()['version']
        return render_template('modal_view.html', info=new_dict, site=site_mappings[site], id=site)
    else:
        return "Site not found"
