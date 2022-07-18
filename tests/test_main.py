import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


class TestMain:
    app = FastAPI()
    client = TestClient(app)

    def test_main_returns(self):
        response = self.client.get("/")
        assert response.status_code == 404
