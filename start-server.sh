#!/bin/sh

uwsgi --http 0.0.0.0:8181 --wsgi-file githubapi/src/app.py --callable app
