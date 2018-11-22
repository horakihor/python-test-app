FROM python:3.7-slim
RUN pip install -U pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 80
CMD ["gunicorn", "--config", "gunicorn/config.py", "manage:app"]
