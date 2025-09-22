front_root=project-front
back_root=project-back
django_app=app

cd $front_root
npm run build
cp dist/index.html ../$back_root/$django_app/templates
rm ../$back_root/$django_app/static/$django_app/*.js
cp dist/assets/*.js ../$back_root/$django_app/static/$django_app
cd ..
python3 index_to_template.py $back_root $django_app
