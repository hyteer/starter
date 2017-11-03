title ytapp
@echo off
call workon micro
cd %cd%\main
set FLASK_APP=__init__.py
flask run --reload --with-threads
CMD
