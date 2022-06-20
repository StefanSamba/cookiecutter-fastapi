FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --upgrade pip

COPY requirements.txt .
COPY app app
COPY tests tests

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN flake8 app/
RUN pytest

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port", "80"]
