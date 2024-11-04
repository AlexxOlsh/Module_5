# FROM python:3.11-slim
#
# WORKDIR /usr/src/app
#
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
#
# RUN pip install --upgrade pip
#
# COPY ./requirements.txt /usr/src/app
#
# RUN pip install -r requirements.txt
#
# COPY . /usr/src/app
#
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.12-slim

RUN apt-get update

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["bash", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]