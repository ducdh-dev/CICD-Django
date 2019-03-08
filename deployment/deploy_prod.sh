#!/bin/sh
whoami
cd /home/ducdh/app/CICD-Django/cicd
source ../env/bin/activate
git pull
pip install -r requirements.txt
python manage.py migrate
exit