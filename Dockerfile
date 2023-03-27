FROM python:3.10-buster

ENV PYTHONBUFFERED=1

ENV DJANGO_SETTINGS_MODULE API_Project.settings

WORKDIR /api_project

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000