@ECHO OFF

set frontRoot=project-front
set backRoot=project-back
set djangoApp=app

cd %frontRoot%
copy /Y dist\index.html ..\%backRoot%\%djangoApp%\templates
del ..\%backRoot%\%djangoApp%\static\%djangoApp%\*.js
copy dist\assets\*.js ..\%backRoot%\%djangoApp%\static\%djangoApp%
cd ..
python index_to_template.py %backRoot% %djangoApp%
