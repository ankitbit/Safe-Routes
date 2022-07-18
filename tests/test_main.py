"""
CLASS DOCSTRING
"""
from fastapi import FastAPI
from fastapi.testclient import TestClient


class TestMain:
    """
    CLASS DOCSTRING
    """

    app = FastAPI()
    client = TestClient(app)

    def url(self):
        """
        METHOD DOCSTRING
        """
        assert str(1) == "1"

    def test_main_returns(self):
        """
        METHOD DOCSTRING
        """
        response = self.client.get("/")
        assert response.status_code == 404
