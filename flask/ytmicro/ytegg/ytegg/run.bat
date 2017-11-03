title YTEgg
call workon ytegg
echo current path %cd%
%pause%
cd %cd%
dir
set FLASK_APP=app.py
set FLASK_DEBUG=1
echo %FLASK_APP%
pause
flask run
CMD
