#!/bin/sh

spawn ssh root@192.168.100.19
expect "password:"
send "vagrant\r"
interact <<EOF
  cd /home/ducdh/app/CICD-Django/cicd
  source ../env/bin/activate
  git pull
  pip install -r requirements.txt
  python manage.py migrate
  exit
EOF