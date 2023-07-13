import app

def test_hello():
    response = app.app.test_client().get('/')
    assert response.data == b'Hello, Flask!'
    assert response.status_code == 200
