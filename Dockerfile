FROM python

WORKDIR app

COPY . .

RUN apt-get update && pip install -r requirements.txt

CMD [ "gunicorn", "-c", "gunicorn.py", "run:app" ]
