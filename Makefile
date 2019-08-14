docker-build:
	docker build -t starter-dashboard .

docker-run:
	docker run --env-file .env -p 5000:80 starter-dashboard

docker: docker-build docker-run

run:
	gunicorn -c gunicorn.py run:app

shell:
	export FLASK_APP=run.py && export FLASK_DEBUG=1 && flask shell

run-dev:
	export FLASK_APP=run.py && export FLASK_DEBUG=1 && flask run

init:
	export FLASK_APP=run.py && export FLASK_DEBUG=1 && flask db init


migrate:
	export FLASK_APP=run.py && export FLASK_DEBUG=1 && flask db migrate


upgrade:
	export FLASK_APP=run.py && export FLASK_DEBUG=1 && flask db upgrade

