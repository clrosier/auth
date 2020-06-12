rm -rf migrations/

python manage.py db init
python manage.py db migrate --message "initial db migration"
python manage.py db upgrade

gunicorn --config gunicorn_conf.py manage:app