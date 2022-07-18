import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


class TestMain:
    app = FastAPI()
    client = TestClient(app)

    def test_main_returns(self):
        response = self.client.get("/")
        import ipdb

        ipdb.set_trace()
        assert response.status_code == 404
        assert response.json() == {"message": "Hello World", "source": "Undisclosed"}
