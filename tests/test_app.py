def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, World!"

def test_get_home_with_name_arg(web_client):
    response = web_client.get("/?name=Joe")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, Joe!"
