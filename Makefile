docker-build:
	docker build -t starter-dashboard .

docker-run:
	docker run --env-file .env -p 5000:80 starter-dashboard

docker: docker-build docker-run

run:
	gunicorn -c gunicorn.py run:app
