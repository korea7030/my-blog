#!/bin/bash

NAME="myblog"                              #Name of the application (*)
DJANGODIR=/my-blog/myblog             # Django project directory (*)
SOCKFILE=/run/gunicorn/gunicorn.sock        # we will communicate using this unix socket (*)
USER=root                                        # the user to run as (*)
GROUP=root                                     # the group to run as (*)
NUM_WORKERS=4                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=myblog.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=myblog.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
python manage.py collectstatic --noinput

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
