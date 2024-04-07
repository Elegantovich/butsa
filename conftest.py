import pytest
from app.app import App


@pytest.fixture()
def app(request):
    app = App()
    return app
