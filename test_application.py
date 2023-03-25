from application import application

with application.test_client() as c:
    response = c.get("/")
    assert b"<!DOCTYPE html>" in response.data
    assert response.status_code == 200