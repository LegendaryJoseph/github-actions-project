from app import app

def test_add_route():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    assert response.get_json() == {"result": 5}