import json
import pathlib

import pytest
from app.main import app
from starlette.testclient import TestClient


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(autouse=True)
def test_body(request):
    file = pathlib.Path(request.node.fspath)
    config = file.with_name("body.json")
    with config.open() as fp:
        test_body = json.loads(fp.read())
    return test_body


@pytest.fixture(autouse=True)
def test_response(request):
    file = pathlib.Path(request.node.fspath)
    config = file.with_name("response.json")
    with config.open() as fp:
        test_response = json.loads(fp.read())
    return test_response
