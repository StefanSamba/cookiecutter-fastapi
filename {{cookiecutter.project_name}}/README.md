# {{cookiecutter.project_name}}

## Description

Add description here

### Features

Add features here

## Visuals

Add visuals here

## Installation

To run this service there are 2 ways:

1. Run in a virtual environment
2. Run as Docker container

### Run in virtual environment

Install virtual environment

```bash
virtualenv venv
```

Activate virtual environment

```bash
source venv/bin/activate
```

Install requirements in virtual environment

```bash
pip3 install -r requirements.txt
```

Run the app

```bash
uvicorn app.main:app --host 0.0.0.0 --port 80
```

Now you can use the integrated docs at:

[http://127.0.0.1:80/docs](http://127.0.0.1:80/docs)

### Run as Docker container

Run the app

```bash
docker build -t {{cookiecutter.project_name}} .
```

```bash
docker run --name {{cookiecutter.project_name}}  -e PORT=80 -p 80:80 -d {{cookiecutter.project_name}}:latest
```

or

```bash
docker compose up
```

## Usage

Endpoint when using virtualenv: `http://127.0.0.1:8000/`
Endpoint when using Docker: `http://0.0.0.0:80/`

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/v1/{{cookiecutter.endpoint_name}}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "utterances": [
    {
      "text": "Can you recommend some gyms in Amsterdam?"
    }
  ]
}'
```

Returns:

```json
{
  "utterances": [
    {
      "text": "Can you recommend some gyms in Amsterdam?"
    }
  ]
}
```

## Schema

utterances: List of dict. E.g. {"text": "sample text"}

```python
utterances: List[Dict]
```

## Considerations & Limitations

Add Considerations & Limitations here

## Roadmap

Add Roadmap here

## Contributing & Support

Add Contributing & Support here

## Authors and acknowledgment

Add Authors and acknowledgment here
