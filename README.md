Url : https://fiboseries.herokuapp.com/


The codes are for production environment


Steps to run application locally:

1. cd hub
2. virtualenv -p python3.6 env
3. cd env && source bin/activate && cd ..
4. pip install -r requirements-dev.txt
5. cd /settings
6. uncomment last line in `wsgi.py` in comment the up one just to it.
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver



Url end points.


    visit http://127.0.0.1:8000 for Ui to share input in POST method
    visit http://127.0.0.1:8000/api/ - to get all fibonacci datas from database in json api.
    visit http://127.0.0.1:8000/api/?number=6 - can also create fibonacci using query params.
    visit http://127.0.0.1:8000/table/ - to get all fibonacci datas from database in Ui - table.



Technology used:

    python - django - postgresql
