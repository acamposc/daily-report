#!/bin/bash
#########################################################

## run in cloud build
 pip3 install google-cloud-bigquery
 pip3 install matplotlib pandas numpy discord-web

source env.sh
# run anywhere
PYTHONIOENCODING=utf-8 python3.8 app.py