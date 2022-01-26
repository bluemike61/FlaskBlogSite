from app import app



def test1():
    """Thsi function teste that the flask aapplication has a correct response code
    when the application goes live.
    """
    response = app.test_client().get("/")
    assert response.status_code == 200
    
def test2():
    """A dummy docstring."""
    response = app.test_client().get("/info")
    assert response.status_code == 200
    
def test3():
    """A dummy docstring."""
    response = app.test_client().get("/login")
    assert response.status_code == 200


def test4():
    """A dummy docstring."""
    response = app.test_client().get("/register")
    assert response.status_code == 200
