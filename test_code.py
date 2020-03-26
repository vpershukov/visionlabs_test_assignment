import pytest
import requests
import random


# Test data
username_data = ["username", "123", " ", "{}}(", ["username"], {"username": "username"}]
post_id_data = ["post_id", "{}}(", ["post_id"], {"post_id": "post_id"}]


# Tests for the first method: GET /
def test_index_method():
    """Test for the first method with valid data"""
    url = "http://0.0.0.0:6000/"
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"
    assert response.text == '{\n  "key": "value"\n}\n', "Test failed. We got: {}".format(response.text)

def test_index_method_as_post():
    """Test for the first method with invalid http method"""
    url = "http://0.0.0.0:6000/"
    response = requests.post(url)
    assert response.status_code == 405, "Test failed: wrong http method"


# Tests for the second method: GET /user/<username>
def test_user_method():
    """Test for the second method with valid data"""
    url = "http://0.0.0.0:6000/user/Jake"
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"
    assert response.text == '{\n  "User": "Jake"\n}\n', "Test failed. We got: {}".format(response.text)

def test_user_method_with_random_string_as_username():
    """Test for the second method with random string as username"""
    username = random.choice(username_data)
    url = "http://0.0.0.0:6000/user/{}".format(username)
    response = requests.get(url)
    assert response.status_code == 200, "Test failed. We sent: {}".format(username)

def test_user_method_with_too_long_username():
    """Test for the second method with too long username"""
    username = "username"*1000
    url = "http://0.0.0.0:6000/user/{}".format(username)
    response = requests.get(url)
    assert response.status_code == 200, "Test failed: too long username"

def test_user_method_without_username():
    """Test for the second method without username"""
    url = "http://0.0.0.0:6000/user/"
    response = requests.get(url)
    assert response.status_code == 404, "Test failed: there is no username"

def test_user_method_as_post():
    """Test for the second method with invalid http method"""
    url = "http://0.0.0.0:6000/user/Jake"
    response = requests.post(url)
    assert response.status_code == 405, "Test failed: wrong http method"


# Tests for the third method: GET /post/<int:post_id>
def test_post_method():
    """Test for the third method with valid data"""
    url = "http://0.0.0.0:6000/post/1"
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"
    assert response.text == '{\n  "post": 1\n}\n', "Test failed. We got: {}".format(response.text)

def test_post_method_with_too_long_post_id():
    """Test for the third method with too long post_id"""
    post_id = "10000001"*1000
    url = "http://0.0.0.0:6000/post/{}".format(post_id)
    response = requests.get(url)
    assert response.status_code == 200, "Test failed: too long post_id"

def test_post_method_without_post_id():
    """Test for the third method without post_id"""
    url = "http://0.0.0.0:6000/post/"
    response = requests.get(url)
    assert response.status_code == 404, "Test failed: there is no post_id"

def test_post_method_with_invalid_post_id():
    """Test for the third method with invalid post_id"""
    post_id = random.choice(post_id_data)
    url = "http://0.0.0.0:6000/post/{}".format(post_id)
    response = requests.get(url)
    assert response.status_code == 404, "Test failed: invalid post_id. We sent: {}".format(post_id)

def test_post_method_as_post():
    """Test for the third method with invalid http method"""
    url = "http://0.0.0.0:6000/post/1"
    response = requests.post(url)
    assert response.status_code == 405, "Test failed: wrong http method"


# Tests for non existent endpoint
def test_for_non_existent_endpoint():
    """Test for non existent endpoint"""
    url = "http://0.0.0.0:6000/test"
    response = requests.get(url)
    assert response.status_code == 404, "Test failed: non existent endpoint"
