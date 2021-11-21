
# ./run.sh python manage.py runserver 0.0.0.0:8000
# ./run.sh python manage.py startapp blog
docker run --rm -v "$PWD":/usr/src/app -w /usr/src/app -p 8000:8000 --user "$(id -u)":"$(id -g)" testserver:1.1 $@

