#!/usr/bin/env python

import socket
import docker


import os
from flask import Flask, Response, render_template


app = Flask(__name__, static_url_path='/static')
cli = docker.Client()
hostname = socket.gethostname()

proxyhost = os.getenv('PROXY_HOST')
proxyport = os.getenv('PROXY_PORT')


@app.after_request
def add_header(r):
    # Disable all caching
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/proxyconfig.pac', methods=['GET'])
def proxyconfig():
    info = cli.inspect_container(hostname)
    networks = info['NetworkSettings']['Networks'].keys()
    tpl = render_template('proxyconfig.pac.tpl', networks = networks, proxyhost = proxyhost, proxyport = proxyport)
    
    return Response(tpl, mimetype='application/x-ns-proxy-autoconfig')


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)
