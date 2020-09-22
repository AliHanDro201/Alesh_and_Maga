#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
#Watching for file changes with StatReloader
#Performing system checks...
#
#System check identified no issues (0 silenced).
#
#You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
#Run 'python manage.py migrate' to apply them.
#September 22, 2020 - 19:27:33
#Django version 3.1.1, using settings 'taskmanager.settings'
#Starting development server at http://127.0.0.1:8000/
#Quit the server with CTRL-BREAK.
#[22/Sep/2020 19:27:49] "GET / HTTP/1.1" 200 16351
#[22/Sep/2020 19:27:49] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
#[22/Sep/2020 19:27:49] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
#[22/Sep/2020 19:27:49] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
#[22/Sep/2020 19:27:49] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
#Not Found: /favicon.ico
#[22/Sep/2020 19:27:49] "GET /favicon.ico HTTP/1.1" 404 1977

